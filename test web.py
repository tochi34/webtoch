from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/addition', methods=['POST'])
def addition():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2
    return render_template('index.html', result=result)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
