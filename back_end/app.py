import argparse
from fileinput import filename
import io
import os
from pkgutil import extend_path
from urllib.parse import urljoin, urlparse

from flask import Flask, make_response, redirect, request, send_file, send_from_directory, url_for, render_template
import sqlalchemy
from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename
from docx import Document

from forms import PassageForm
from get_title import get_title
from get_abstract import get_abstract
from get_sim import get_sim_title
from generate_title import generate
from get_w_cloud import generate_wcloud

from db_connection.database import engine
from db_connection.models import users, User, passages, Passage
from sqlalchemy.orm import Session
from sqlalchemy import select

parser = argparse.ArgumentParser()
parser.add_argument('--use_gpt2', default=False, help="Use GPT2 model if set to True")
args = parser.parse_args()
USE_GPT2 = args.use_gpt2

history = []

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


@app.route('/', methods=['POST', 'GET'])
def index():
    form = PassageForm()
    if form.submit.data and form.validate():
        context = form.context.data
        title = get_title(context)
        abstract = get_abstract(context)
        data = {'title': title, 'abstract': abstract}   
        return render_template("main.html", passageForm=form, data=data)
    return render_template('main.html', passageForm=form)


@app.route('/api/title', methods=['POST'])
def api_title():
    context = request.form['context']
    num_sentence = int(request.form['num_sentence'])
    use_wordcloud = True if 'use_wordcloud' in request.form else False
    title = get_title(context)
    if USE_GPT2:
        extend_title = generate(title)
        title += extend_title
    abstract = get_abstract(context, num_sentence)
    file_name = ''
    if use_wordcloud:
        file_name = generate_wcloud(context)

    data = {'title': title, 'abstract': abstract, 'sim_title': get_sim_title(title), 'pic': file_name}

    # 保存历史记录
    if 'user' in request.form:
        username = request.form['user']
        p = Passage(title, abstract, context, username, file_name)
        with Session(engine) as session:
            session.add_all([p])
            session.commit()
    return data


@app.route('/api/history', methods=['POST'])
def api_history():
    msg = request.form['msg']
    session = Session(engine)
    if msg == "history":
        if "user" in request.form:
            username = request.form['user']
            stmt = select(User).where(User.name == username)
            try:
                u = session.scalars(stmt).one()
                sql = select(Passage).where(Passage.username == username)
                p_list = session.scalars(sql).all()
                return {"history": [i.to_dict() for i in p_list]}
            except sqlalchemy.exc.NoResultFound:
                raise HTTPException(404)
    else:
        raise HTTPException(404)


@app.route('/api/file', methods=['POST'])
def api_file():
    file = request.files['file']
    if file is None:# 表示没有发送文件
        return { 'msg': "文件上传失败" }
    else:
        filename = secure_filename(file.filename)
        save_path = os.path.join(os.path.dirname(__file__), "upload_file/")
        doc_path = os.path.join(save_path, filename)
        file.save(doc_path)
        document = Document(doc_path)
        text = ""
        all_paragraphs = document.paragraphs
        for paragraph in all_paragraphs:
            for run in paragraph.runs:
                text += run.text
        return { "msg": "上传成功" , "context": text}


@app.route('/api/ocr', methods=['POST'])
def api_ocr():
    file = request.files['file']
    if file is None:# 表示没有发送文件
        return { 'msg': "文件上传失败" }
    else:
        filename = secure_filename(file.filename)
        save_path = os.path.join(os.path.dirname(__file__), "upload_file/")
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        doc_path = os.path.join(save_path, filename)
        file.save(doc_path)
        from cnocr import CnOcr
        ocr = CnOcr()
        res = ocr.ocr(doc_path)
        text = ""
        for c, s in res:
            text += c
        return { "msg": "上传成功" , "context": text}


@app.route("/api/wpic/<file_name>", methods=['GET'])
def get_pic_file(file_name):
    try:
        return send_file(
            f"wcloud_pics/{file_name}",
            mimetype='image/png',
            as_attachment=False
        )
    except Exception as e:
        return f"文件读取异常{e}"


@app.route("/users/login", methods=['POST'])
def user_login():
    name = request.form['name']
    passwd = request.form['passwd']
    session = Session(engine)
    stmt = select(User).where(User.name == name)
    try:
        u = session.scalars(stmt).one()
        if u.passwd == passwd:
            return {"success": True}
        else:
            return {"success": False}
    except sqlalchemy.exc.NoResultFound:
        return {"success": False}


@app.route("/users/register", methods=['POST'])
def user_register():
    name = request.form['name']
    passwd = request.form['passwd']
    email = request.form['email']
    session = Session(engine)
    stmt = select(User).where(User.name == name)
    try:
        u = session.scalars(stmt).one()
        return {"success": False}
    except sqlalchemy.exc.NoResultFound:
        with Session(engine) as session:
            u = User(name=name, email=email, passwd=passwd)
            session.add_all([u])
            session.commit()
        return {"success": True}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
