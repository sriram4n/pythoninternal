class ClassA():
    def m(self):
        print("inside class A")

class ClassB(ClassA):
    def m(self):
        print("inside class B")

class ClassC(ClassB):
    def m(self):
        print("inside class C")

class ClassD(ClassC, ClassB):
    def m(self):
        print("inside class D")
        ClassB.m(self)
        ClassC.m(self)
        ClassA.m(self)

obj = ClassD()
obj.m()