from flask import flash
from werkzeug.utils import secure_filename

class transcode_handler:
    def __init__(self, config,req_form, req_file):
        print("init model: ", type(self).__name__, flush = True)
        self.config = config
        self.req_form = req_form
        self.req_file = req_file

    def validate_file(self):
        if 'file' not in self.req_file:
            flash('No file part')
            print("request form: ", self.req_file, flush=True)
            return False
        file = self.req_file['file']

        if file.filename == '':
            flash('No selected file')
            return False

        self.filename = secure_filename(file.filename)
        print("filename: ", self.filename, flush=True)
        return True

    def validate_ext(self):
        '''
        Only accept obj and revit file
        '''
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in config['media_type']

    def upload_media(self):
        pass