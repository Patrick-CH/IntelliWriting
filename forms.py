from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PassageForm(FlaskForm):
    context = TextAreaField('', validators=[DataRequired()], render_kw={'placeholder': '请输入文章内容'})
    submit = SubmitField('提交', render_kw={"class": "submit_btn"})
