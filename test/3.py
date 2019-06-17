class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class A(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name


a1 = A(2)
a2 = A(3)
if id(a1) != id(a2):
    print("111")
else:
    print("222")
