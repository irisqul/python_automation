class House:

    def __init__(self, name=None, address=None, description=None, id=None, deleteLink=None, editLink=None):
        self.name = name
        self.address = address
        self.description = description
        self.id = id
        self.deleteLink = deleteLink
        self.editLink = editLink


class Premise:

    def __init__(self, name=None, address=None, id=None, deleteLink=None, editLink=None):
        self.name = name
        self.address = address
        self.id = id
        self.deleteLink = deleteLink
        self.editLink = editLink
