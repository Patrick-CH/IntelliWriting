import argparse
from fileinput import filename
import io
import os
from pkgutil import extend_path
from urllib.parse import urljoin, urlparse

from flask import Flask, make_response, redirect, request, send_file, send_from_directory, url_for, render_template
from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename
from docx import Document

from forms import PassageForm
from get_title import get_title
from get_abstract import get_abstract
from get_sim import get_sim_title
from generate_title import generate
from get_w_cloud import generate_wcloud

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
    title = get_title(context)
    if USE_GPT2:
        extend_title = generate(title)
        title += extend_title
    abstract = get_abstract(context, num_sentence)
    file_name = generate_wcloud(context)

    data = {'title': title, 'abstract': abstract, 'sim_title': get_sim_title(title), 'pic': file_name}
    if len(history) < 3:
        history.append(data)
    else:
        history.pop(0)
        history.append(data)
    return data


@app.route('/api/history', methods=['POST'])
def api_history():
    msg = request.form['msg']
    if msg == "history":
        return {"history": history}
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
                print(run.text) 
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
        print("Predicted Chars:", res)
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
