from flask import Flask,render_template,url_for
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule2')
def schedule2():
    return render_template('schedule2.html')


if __name__=="__main__":
    app.run(debug=True)
