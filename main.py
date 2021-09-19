from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os

app = Flask('app')
app.config['UPLOAD_FOLDER'] = "tmp"

app.config['SECRET_KEY'] = 'my super secret key'.encode('utf8')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/run_model')
def run_model():
    return render_template('index.html')
    
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # INSERT LINK TO TENSORFLOW HERE
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return

app.run(host='0.0.0.0', port=8080)