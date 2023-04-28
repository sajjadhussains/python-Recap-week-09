# single inheritance
# multiple inheritance
# multilevel inheritance

# multilevel inheritance
# class GrandParent:
#     def __init__(self) -> None:
#         self.string="I am grandparent"

# class Parent:
#     def __init__(self) -> None:
#         self.string1="I am parent"
# class Child(Parent,GrandParent):
#     def __init__(self) -> None:
#         self.string2="I am Child"
#         super().__init__()
#         GrandParent.__init__(self)

# c=Child()
# print(c.string)

# multiple inheritance
class GrandParent:
    def __init__(self) -> None:
        self.string="I am grandparent"

class Parent(GrandParent):
    def __init__(self):
        self.string="I am parent"
        super().__init__()
    
class Child(Parent):
    def __init__(self):
        # self.string="I am child"
        Parent().__init__(self)

c=Child()
print(c.string)