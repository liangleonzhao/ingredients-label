from flask import (
        Flask, Blueprint, render_template, flash, redirect, url_for,
        request
)
from werkzeug.utils import secure_filename
import ingredients.ImageConverter.imageToText as imageToText

bp = Blueprint('label', __name__, url_prefix='/label')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/analyze', methods=['GET', 'POST'])
def ai_analyze():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('index'))
        
        
        picture_file = request.files['file']
        
        # if user does not select file, browser also
        # submit an empty part without filename
        if picture_file.filename == '':
            flash('No selected file')
            return redirect(url_for('index'))
        
        analysis = imageToText.Store_Data(picture_file, 'test food')
        
        print(analysis.dictionary_add())

        return 'Analysis Successful'
    # Catch-all return for errors
    return 'An error has occurred'
