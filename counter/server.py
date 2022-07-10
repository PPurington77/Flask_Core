from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'this is the secret key'

@app.route('/')
def home_page():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html', count = session['count'])

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/addtwo')
def addtwo():
    session['count'] += 1
    return redirect('/')

@app.route('/deletesession')
def delete():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)