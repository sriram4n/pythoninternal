class Animal():
    def sound(self):
        print("animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

obj = Dog()
obj.sound()

#multi inherit

class ClassA():
    def showA(self):
        print("im class A")

class ClassB():
    def showB(self):
        print("im class B")

class ClassC(ClassA, ClassB):
    def showC(self):
        print("im class C")

aobject = ClassC()
aobject.showA()
aobject.showB()
aobject.showC()