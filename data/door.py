from model.door import Door


testdata = [
    Door(name="Key1", relay=1),
    Door(name="Key1", relay=2)
   ]
# def __repr__(self):
#    return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

# def __eq__(self, other):
#   return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name