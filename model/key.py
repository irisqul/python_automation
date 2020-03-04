class Key:

    def __init__(self, name=None, number=None, code=None, keyset=None, contact=None):
        self.name = name
        self.number = number
        self.code = code
        self.keyset = keyset
        self.contact = contact

    #def __repr__(self):
    #    return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    #def __eq__(self, other):
     #   return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name