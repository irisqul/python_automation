from model.intercom import Intercom


testdata = [
    Intercom(name="Key1", mac_address="00-14-22-01-23-45", password="admin", username=3456),
    Intercom(name="Key1", mac_address="00-14-22-01-23-45", password="admin", username=3456)
]
# def __repr__(self):
#    return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

# def __eq__(self, other):
#   return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name