from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def firstAttempt():
    return render_template('index.html', rows=8, cols=8)
@app.route('/<int:x>')
def secondAttempt(x):
    return render_template('index.html', rows=8, cols=x)
@app.route('/<int:x>/<int:y>')
def thirdAttempt(x,y):
    return render_template('index.html', rows=y, cols=x)
if __name__=="__main__":
    app.run(debug=True)