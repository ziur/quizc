from json import JSONEncoder


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


myclass = MyClass(4, 5)
json = MyEncoder().encode(myclass)
f = open("myform.json", "w")
f.write(json)
f.close()
