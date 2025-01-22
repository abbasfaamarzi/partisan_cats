# This is a generated file.
class CatSetMagics:
    def __init__(self, initial_list):
        self.data = CatListTool(list(dict.fromkeys(initial_list)))

    def __str__(self):
        return str(self.data)
