from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os

app = Flask('app')
app.config['UPLOAD_FOLDER'] = "tmp"

app.config['SECRET_KEY'] = 'my super secret key'.encode('utf8')

@app.route('/')
def on_load():
    generate_suggestions("dataset/pfp.jpg")
    return render_template('index.html')


# method that handles image_load    
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

            # not sure if image needs to be saved or not
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # call tensorflow
            generate_suggestions(filename)

            # stay on main page
            return redirect(request.referrer)

def generate_suggestions(filename):
    print("generating suggestions for file:", filename)
    # modify html here
    # generate suggestions here



app.run(host='0.0.0.0', port=8080)