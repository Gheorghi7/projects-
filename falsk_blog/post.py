class Post:
    def __init__(self, data):
        self.data = data

    def check_first_id(self):
        for i in self.data:
            if i['id'] == 1:
                return self.data[i - 1]['title']

    def check_second_id(self):
        for i in self.data:
            if i['id'] == 2:
                return self.data[i - 1]['title']
