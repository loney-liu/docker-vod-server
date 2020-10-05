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
