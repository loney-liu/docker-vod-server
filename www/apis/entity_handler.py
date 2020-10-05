class entity_handler:
    def __init__(self, config, data):
        print("init model: ", type(self).__name__, flush = True)
        self.sg = config['sg']
        self.data = data
        print("data: ", self.data, flush = True)
    
    def get_entity_name(self):
        filters = [
            ["project.Project.id", "is", int(self.data["project_id"])], 
            [ 'id', "is", int(self.data['entity_id'])]
            ]
        
        print("filters: ", filters, flush = True)
        if self.data["entity_type"] == "Task":
            fields = ['id', 'content']
        else:
            fields = ['id', 'code']

        entity = self.sg.find_one(self.data["entity_type"], filters,fields)


        if self.data["entity_type"] == "Task":
            return entity['content']
        else:
            return entity['code']

    def get_tasks(self):
        filters = [
            ["project.Project.id", "is", int(self.data["project_id"])], 
            [ 'entity', "is", {'type': self.data["entity_type"], 'id': int(self.data['entity_id'])}]
            ]
        
        print("filters: ", filters, flush = True)
        tasks = self.sg.find("Task", filters,['id', 'content'])

        return tasks

    def create_version(self):
        if self.data['task_id'] != None:
            data = { 
                'code': self.data['just_file_name'],
                'project': {'type': 'Project','id': int(self.data['project_id'])},
                'entity': {'type': self.data['entity_type'], 'id': int(self.data['entity_id'])},
                'sg_task': {'type': 'Task', 'id': int(self.data['task_id'])},
                'sg_uploaded_movie_mp4': {
                           'name': self.data['just_file_name'],
                            'url': self.data['vod_file_path']
                           }
            }
        else:
            link_entity = self.sg.find_one(self.data['entity_type'], [['id', 'is', int(self.data['entity_id'])]], ['id', 'entity'])
            data = { 
                'code': self.data['just_file_name'],
                'project': {'type': 'Project','id': int(self.data['project_id'])},
                'entity': link_entity['entity'],
                'sg_task': {'type': self.data['entity_type'], 'id': int(self.data['entity_id'])},
                'sg_uploaded_movie_mp4': {
                           'name': self.data['just_file_name'],
                            'url': self.data['vod_file_path']
                           }
            }

        version = self.sg.create('Version', data)

        self.sg.upload_thumbnail("Version", version['id'], self.data['full_dest_thumbnail'])
        print("version: ", version, flush = True)
