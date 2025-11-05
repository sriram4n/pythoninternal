class ClassA:
    def m(self):
        print("in class A")
    
class ClassB(ClassA):
    def m(self):
        print("in class B")

class ClassC(ClassB):
    def m(self):
        print("in class c")

class ClassD(ClassC , ClassB):
    def m(self):
        print("In class D")
        ClassB.m(self)
        ClassC.m(self)
        ClassA.m(self)

obj = ClassD()
obj.m()