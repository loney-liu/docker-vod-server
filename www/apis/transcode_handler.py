from flask import flash
import datetime
import subprocess
from werkzeug.utils import secure_filename
# from pypinyin import lazy_pinyin
import os
import cv2

class transcode_handler:
    def __init__(self, config,req_form, req_file):
        print("init model: ", type(self).__name__, flush = True)
        self.config = config
        self.req_form = req_form
        self.req_file = req_file

        self.data = {}
        self.data['project_name'] = req_form.get('project_name', None)
        self.data['project_id'] = req_form.get('project_id', None)
        self.data['entity_type'] = req_form.get('entity_type', None)
        self.data['entity_name'] = req_form.get('entity_name', None)
        self.data['entity_id'] = req_form.get('entity_id', None)
        self.data['task_id'] = req_form.get('task_id', None)
        self.data['use_diy'] = req_form.get('use_diy', None)

    def validate_file(self):
        if 'file' not in self.req_file:
            flash('No file part')
            print("request form: ", self.req_file, flush=True)
            return False
        self.file = self.req_file['file']

        if self.file.filename == '':
            flash('No selected file')
            return False
        
        self.filename =  self.file.filename
        self.data['uploaded_filename'] = self.filename
        print("filename: ", self.filename, flush=True)
        return True

    def validate_ext(self):
        '''
        Only accept obj and revit file
        '''
        return '.' in self.filename and self.filename.rsplit('.', 1)[1].lower() in self.config['media_type']

    def get_subfolder(self):
        sub_folder = "{}/{}".format(self.data["entity_id"], datetime.datetime.now().strftime("%y%m%d%H%M%S"))
        self.data['full_folder'] = "{}/{}".format(self.config['data_folder'], sub_folder)
        cmd="mkdir -p %s && ls -lrt %s"%(self.data['full_folder'],self.data['full_folder'])
        output = subprocess.Popen([cmd], shell=True,  stdout = subprocess.PIPE).communicate()[0]

        if "total 0" in str(output):
            print("Success: Created Directory %s"%(self.data['full_folder']), flush=True)
            path, file_full_name = os.path.split(self.data['uploaded_filename'])
            file_full_without_ext= file_full_name.split(".")[0]
            file_ext= file_full_name.split(".")[1]
            self.data['just_file_name'] = file_full_name
            self.data['full_src_file_path'] = '{}/{}'.format(self.data['full_folder'], self.data['uploaded_filename'])
            self.data['file_ext'] = file_ext
            self.data['full_dest_file_path'] = '{}/review_{}.mp4'.format(self.data['full_folder'], file_full_without_ext)
            self.data['full_dest_file_path_2'] = '{}/review_{}_2.mp4'.format(self.data['full_folder'], file_full_without_ext)
            self.data['full_dest_thumbnail'] = '{}/thumbnail_{}.jpeg'.format(self.data['full_folder'], file_full_without_ext)
            self.data['vod_file_path'] = '{}/{}/review_{}.mp4'.format(self.config['vod_url'], sub_folder, file_full_without_ext)
        else:
            print("Failure: Failed to Create a Directory (or) Directory already Exists",self.data['full_folder'], flush=True)
    
    def upload_media(self):
        self.get_subfolder()
        self.file.save(self.data['full_src_file_path'])
        self.data['frame_rate']=25.0
        if self.data['file_ext'] == 'mp4':
            cap=cv2.VideoCapture(self.data['full_src_file_path'])
            fps = cap.get(cv2.CAP_PROP_FPS)
            self.data['frame_rate']=float(fps)
        return self.data

    def transcode_mp4(self):
        ffmpeg_cmd = self.config['ffmpeg_mp4'].format(self.data['full_src_file_path'],self.data['full_dest_file_path'])
        print("ffmpeg cmd: ", ffmpeg_cmd, flush=True)
        cmd = ffmpeg_cmd.split(',')
        print("ffmpeg cmd: ", cmd, flush=True)
        output = subprocess.Popen([ffmpeg_cmd], shell=True,  stdout = subprocess.PIPE)

    def copy_media(self):
        cmd="cp -rf {} {}".format(self.data['full_src_file_path'], self.data['full_dest_file_path'])
        output = subprocess.Popen([cmd], shell=True,  stdout = subprocess.PIPE).communicate()[0]

    def generate_thumbnail(self):
        ffmpeg_cmd = self.config['ffmpeg_thumbnail'].format(self.data['full_src_file_path'],self.data['full_dest_thumbnail'])
        cmd = ffmpeg_cmd.split(',')
        print("thumbnail cmd: ", cmd, flush=True)
        subprocess.call(cmd)