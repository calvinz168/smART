from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload_image')
def upload_image():
    return render_template('index.html')

@app.route('/run_model')
def run_model():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080)