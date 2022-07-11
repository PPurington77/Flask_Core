from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def home_page():

    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html', name = session['name'], location = session['location'], language = session['language'], comments = session['comments'])

@app.route('/processing', methods=['POST'])
def processing():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    return redirect('/result')

@app.route('/returnhome')
def return_home():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)