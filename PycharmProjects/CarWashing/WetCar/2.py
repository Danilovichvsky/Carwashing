class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        # Сохранить все атрибуты, которые не начинаются с '__'
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        # Преобразовать имена атрибутов в верхний регистр
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        # Добавить атрибут `attrs` в новый класс
        uppercase_attr["ATTRS"] = list(uppercase_attr.keys())
        # Создать новый класс
        return super().__new__(cls, name, bases, {**dct, **uppercase_attr})


class MyClass(metaclass=UpperAttrMetaclass):
    attribute_one = "value1"
    attribute_two = "value2"


# Проверка
print(hasattr(MyClass, "attribute_one"))  # False
print(hasattr(MyClass, "ATTRIBUTE_ONE"))  # True
obj = MyClass()
print(MyClass.ATTRS)  # ['ATTRIBUTE_ONE', 'ATTRIBUTE_TWO']
