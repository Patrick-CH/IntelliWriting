import os
from urllib.parse import urljoin, urlparse

from flask import Flask, redirect, request, url_for, render_template

from forms import PassageForm
from get_title import get_title
from get_abstract import get_abstract

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
    title = get_title(context)
    abstract = get_abstract(context)
    data = {'title': title, 'abstract': abstract}
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
