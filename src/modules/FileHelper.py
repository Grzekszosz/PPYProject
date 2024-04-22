class FileHelper:
    name = ''
    pat = ''

    def __init__(self, name, pat):
        self.name = name
        self.pat = pat

    def __del__(self):
        pass

    def write_to_file(self, content):
        with open(self.pat, 'a') as file:
            file.writelines(content)
    def read_file_all(self):
        with open(self.pat, 'r') as file:
            return file.read()

