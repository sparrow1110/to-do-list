from flask import request, render_template, redirect, url_for
from todo import create_app, db
from todo.models import ToDo

app = create_app()


@app.get('/')
def home():
    todo_list = ToDo.query.order_by(ToDo.is_complete.asc(), ToDo.id.asc()).all()
    return render_template('todo/index.html', todo_list=todo_list, title='Главная страница')


@app.post('/add')
def add():
    title = request.form.get('title')
    new_todo = ToDo(title=title, is_complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/update/<int:todo_id>')
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    todo.is_complete = not todo.is_complete
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/delete/<int:todo_id>')
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))
