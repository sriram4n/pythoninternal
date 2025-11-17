class ClassA():
    def m(self):
        print("inside class A")

class ClassB(ClassA):
    def m(self):
        print("inside class B")

class ClassC(ClassA):
    def m(self):
        print("inside class C")

class ClassD(ClassB, ClassC):
    def m(self):
        print("inside class D")
        ClassB.m(self)
        ClassC.m(self)
        ClassA.m(self)

obj = ClassD()
obj.m()