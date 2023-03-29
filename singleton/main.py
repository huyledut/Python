class Singleton:
    __instance = None
    __name = "huy"
    __count = 0

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

    @classmethod
    def getCount(cls):
        cls.__count += 1
        return cls.__count

    @classmethod
    def getName(cls):
        return cls.__name
   
    @classmethod
    def setAttrs(cls, *args, **kwargs):
        for i in kwargs.keys():
            if i == "name":
                cls.__name = kwargs[i]
            if i == "count":
                cls.__count = kwargs[i]
              
    @staticmethod
    def toString():
        return f"Ten la: {Singleton.__name}, So dem: {Singleton.__count}"


def main():
    object = {"name": "huy new", "count": 1000, "test": 123333}
    Singleton.setAttrs(**object)
    print(Singleton.toString())

if __name__ == "__main__":
    main()