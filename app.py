from flask import Flask, request, send_file, redirect, url_for, send_from_directory
import io
import os
import os.path
from copykey import runner
from threading import Thread
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = './tmp'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

unique_num = 0

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

@app.route('/upload', methods=['POST'])
def upload():
    global unique_num
    if not 'file' in request.files:
        return "Please add a file."
    file = request.files['file']
    if file.filename == "":
        return "Please add a nonempty file."
    if not file.filename.endswith(".mp4"):
        return "Please upload a .mp4"
    savename = secure_filename(str(unique_num) + "_" + file.filename)
    fullpath = os.path.join(app.config['UPLOAD_FOLDER'], savename)
    outputname = secure_filename(os.path.basename(str(unique_num) + "_" + file.filename) + ".jpg")
    file.save(fullpath)
    unique_num += 1
    Thread(target=runner.run, args=(fullpath,os.path.join('out', outputname), "error.png")).start()
    return redirect(url_for('get_file', filename=outputname))

@app.route('/get/<filename>')
def get_file(filename):
    if os.path.isfile(os.path.join('out', filename)):
        return send_from_directory("out", filename)
    else:
        with open("poll.html", "r") as f:
            return f.read()

@app.route('/')
def index():
	with open("index.html", "r") as f:
		return f.read()
