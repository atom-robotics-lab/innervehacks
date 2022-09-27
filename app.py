from flask import Flask,render_template,url_for
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule2')
def schedule2():
    return render_template('schedule2.html')

@app.route('/trucker')
def trucker():
    return render_template('trucker.html')


if __name__=="__main__":
    app.run(debug=True)
