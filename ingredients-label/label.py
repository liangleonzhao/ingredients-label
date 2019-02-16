
import os
from flask import (
        Flask, Blueprint, render_template, request
)
from werkzeug.utils import secure_filename

bp = Blueprint('label', __name__, url_prefix='/label')



@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/uploader', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(secure_filename(file.filename))
            return 'file uploaded successfully'
    return "no file"
