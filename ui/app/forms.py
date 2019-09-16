from flask_wtf import FlaskForm  #通过flask_<name> 来导入flask的插件
from wtforms import TextAreaField, PasswordField, BooleanField, SubmitField  #导入四个表示表单字段的类
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    Ori_Text = TextAreaField('源文本', validators=[DataRequired()])  #每个类接收一个别名作为第一个参数，并生成实例作为LoginForm的类属性
    Result = TextAreaField('分类结果')  #可选参数validators验证字段是否符合预期
    submit = SubmitField('分类')