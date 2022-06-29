import os
from urllib.parse import urljoin, urlparse

from flask import Flask, redirect, request, url_for, render_template

from forms import PassageForm
from get_title import get_title
from get_abstract import get_abstract

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='hello', **kwargs):
    """

    :param default: 获取信息失败时的返回值
    :param kwargs: 可选参数，作用同上
    :return: 重定向到上一个界面，如过无法获取上一个界面则返回default
    """
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
