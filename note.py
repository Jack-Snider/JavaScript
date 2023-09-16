



def hello(a:int):

    if not isinstance(a, int):
        raise TypeError("the parameter should be Integer")

    return a


def aaa(a:int = 'a'):
    return a



class Test():

    def __init__(self, name:str = "None", age:int = 0):

        if not isinstance(name,str) or not isinstance(age,int):
            raise TypeError("wrong data type")

        self.name = name
        self.age = age
        
    def introduce(self):
        print(f'Hello, I am {self.name} and i am {self.age} years old.')

    def __str__(self) -> str: # str Type으로 반환한다.(Type hint)
        return f'{self.name}'


person = Test("영훈",13)
person.introduce()
print(person)




