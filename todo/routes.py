from flask import request, render_template, redirect, url_for, flash, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user
from todo import create_app, db, login_manager
from todo.models import ToDo, User
from todo.forms import LoginForm, RegistrationForm

app = create_app()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Пользователь с таким email уже существует')
            return redirect(url_for('register'))
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно!')
        return redirect(url_for('login'))
    return render_template('todo/register.html', form=form, title='Регистрация')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неверное имя пользователя или пароль')
            return redirect(url_for('login'))
        rm = form.remember.data
        login_user(user, remember=rm)
        return redirect(url_for('home'))
    return render_template('todo/login.html', form=form, title='Вход')


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('home'))


@app.get('/')
@login_required
def home():
    todo_list = ToDo.query.filter_by(user_id=current_user.id).order_by(ToDo.is_complete.asc(), ToDo.id.asc()).all()
    return render_template('todo/index.html', todo_list=todo_list, title='Главная страница')


@app.post('/todos/add')
@login_required
def add():
    title = request.form.get('title')
    if not title:
        flash('Название задачи не может быть пустым')
        return redirect(url_for('home'))
    new_todo = ToDo(title=title, is_complete=False, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))


@app.post('/todos/update/<int:todo_id>')
@login_required
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        flash('Задача не найдена')
        return redirect(url_for('home'))
    todo.is_complete = not todo.is_complete
    db.session.commit()
    return redirect(url_for('home'))


@app.post('/todos/delete/<int:todo_id>')
@login_required
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        flash('Задача не найдена')
        return redirect(url_for('home'))
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/static/img/logo3.webp')
def serve_logo():
    response = send_from_directory('static/img', 'logo3.webp')
    response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'  # 1 год
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('todo/page404.html', title="Страница не найдена"), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('todo/page500.html', title="Ошибка сервера"), 500
