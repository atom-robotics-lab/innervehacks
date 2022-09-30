from time import time
from unicodedata import category
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200))
    category=db.Column(db.String)
    # date=db.column(db.Date)
    # time=db.column(db.Time)
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ewaste')
def ewaste():
    tasks2 = Todo.query.filter_by(category='E-waste').all()
    return render_template('ewaste.html',tasks=tasks2)

@app.route('/nonbio')
def nonbio():
    tasks2 = Todo.query.filter_by(category='Non-Bio-Degradable').all()
    return render_template('nonbio.html',tasks=tasks2)

@app.route('/bio')
def bio():
    tasks2 = Todo.query.filter_by(category='Bio-Degradable').all()
    return render_template('bio.html',tasks=tasks2)

@app.route('/route')
def route():
    return render_template('route.html')

@app.route('/records')
def records():
    tasks = Todo.query.order_by(Todo.firstname).all()
    return render_template('records.html', tasks=tasks)

@app.route('/schedule2',methods=['POST','GET'])
def schedule2():
    if request.method == 'POST':
        task_content = request.form['firstname']
        task_content2 = request.form['address']
        task_content_5=request.form['waste']
        # task_content3= request.form['date']
        # task_content4= request.form['time']
        # date_value = "%s"%task_content3
        # print(task_content3)
        # print(date_value)
        new_task = Todo(firstname=task_content,address=task_content2,category=task_content_5)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/schedule2')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.firstname).all()
        return render_template('schedule2.html', tasks=tasks)


@app.route('/trucker')
def trucker():
    return render_template('trucker.html')


if __name__=="__main__":
    app.run(debug=True)
