from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    password = PasswordField("Пароль: ", validators=[DataRequired("Необходимо ввести пароль"),
                                                     Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")])
    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")


class RegistrationForm(FlaskForm):
    username = StringField("Имя: ", validators=[DataRequired("Поле имени обязательно"),
                                                Length(min=2, max=100, message="Имя должно быть от 2 до 100 символов")])
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    password = PasswordField("Пароль: ", validators=[DataRequired("Необходимо ввести пароль"),
                                                     Length(min=4, max=100, message="Пароль должен быть от 4 до 100 символов")])
    password2 = PasswordField("Повторите пароль: ", validators=[DataRequired(),
                                                                EqualTo('password', message="Пароли не совпадают")])
    submit = SubmitField("Зарегистрироваться")
