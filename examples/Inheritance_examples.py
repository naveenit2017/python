'''
1.Single Level Inheritance(Parent-->Child)
2.Multi Level Inheritance(Grand Father-Parent-Child)
3.Multipule Inheritance(F,M--Child)
4.Hierarchal Inheritance(F--C1,C2) it is possible only python
'''
# class Parent:
#     def pout(self):
#         print("I am from Parent")
# class child(Parent):
#     def cout(self):
#         print("I am from the child")

# c1=child()
# c1.cout()
# c1.pout
# class GrandFather(): #Multi Level
#     def gout(self):
#         print("I am the GF")
# class Parent(GrandFather):
#     def pout(self):
#         print("I am the Parent")
# class child(Parent):
#     def cout(self):
#         print("I am the child")
# c1=child()
# c1.cout()
# c1.pout()
# c1.gout()
# class Father():
#     def fout(self):
#         print("I am the Father")
# class Mother():
#     def mout(self):
#         print("I am the mother")
# class Child(Father,Mother):
#     def cout(self):
#         print("I am the child")
# c=Child()
# c.cout()
# c.fout()
# c.mout()
class Father():
    def fout(self):
        print("I am the father")
class child1(Father):
    def c1out(self):
        print("I am from C1")
class child2(Father):
    def c2out(self):
        print("I am from c2")
c1=child1()
c1.c1out()
c1.fout()
c2=child2()
c2.c2out()
c2.fout()