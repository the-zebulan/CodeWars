def class_name_changer(cls, new_name) :
    if not new_name[0].isupper() or not new_name.isalnum():
        raise NameError('Invalid class name!')
    cls.__name__ = new_name


# solution is above, testing is below
class MyClass(object):
    def __str__(self):
        return str(type(self))


myObject = MyClass()
assert str(MyClass) == "<class '__main__.MyClass'>"

class_name_changer(MyClass, "UsefulClass")
assert str(MyClass) == "<class '__main__.UsefulClass'>"

class_name_changer(MyClass, "SecondUsefulClass")
assert str(MyClass) == "<class '__main__.SecondUsefulClass'>"
