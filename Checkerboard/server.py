from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight():
    return render_template('index.html')

@app.route('/4')
def fourByEight():
    return render_template('8by4.html')

@app.route('/<int:num>')
def rowsOnly(num):
    return render_template('rows.html', num = num)

@app.route('/(<int:x>)(<int:y>)')
def xy(x, y):
    return render_template('xy.html', x = x, y = y)

if __name__=="__main__":
    app.run(debug=True)