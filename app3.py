import os
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './tmp'
ALLOWED_EXTENSIONS = set(['mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/favicon.ico')
def favicon():
    with open("favicon.ico", "rb") as f:
        return send_file(io.BytesIO(f.read()),
            attachment_filename='favicon.ico',
            mimetype='image/x-icon')

@app.route('/key.png')
def key_image():
    with open("key.png", "rb") as f:
        return send_file(io.BytesIO(f.read()),
            attachment_filename='key.png',
            mimetype='image/png')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        print(len(file.read()))
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    #with open("index.html", "r") as f:
    #    return f.read()
    return ""
