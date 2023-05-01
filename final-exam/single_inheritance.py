# single inheritance
# class Boro_Vai:
#     def __init__(self,name,father_name,mother_name,house_no,age) -> None:
#         self.name=name
#         self.father_name=father_name
#         self.mother_name=mother_name
#         self.house_no=house_no
#         self.age=age
#     def get_house_no(self):
#         return self.house_no
# class Mejo_vai(Boro_Vai):
#     def __init__(self, name, father_name, mother_name, house_no, reading_table) -> None:
#         super().__init__(name, father_name, mother_name, house_no, reading_table)

# multilevel inheritance

class Boro_Vai:
    def __init__(self,name,father_name,mother_name,house_no,age) -> None:
        self.name=name
        self.father_name=father_name
        self.mother_name=mother_name
        self.house_no=house_no
        self.age=age
        self.string1="I am boro vai"
    def get_house_no(self):
        return self.house_no

class Mejo_vai:
    def __init__(self) -> None:
        self.string="I am Mejo vai"

class Soto_bon(Boro_Vai,Mejo_vai):
    def __init__(self):
        self.string="I am soto bon"
        Boro_Vai.__init__(self)
        Mejo_vai.__init__(self)

# multi level inheritance
class Boro_Vai:
    def __init__(self,name,father_name,mother_name,house_no,age) -> None:
        self.name=name
        self.father_name=father_name
        self.mother_name=mother_name
        self.house_no=house_no
        self.age=age
        self.string1="I am boro vai"
    def get_house_no(self):
        return self.house_no
    
class Mejo_vai(Boro_Vai):
    def __init__(self) -> None:
        self.string="I am Mejo vai"
    super().__init__()
class Soto_bon(Mejo_vai):
    def __init__(self):
        self.string="I am soto bon"
        Mejo_vai.__init__(self)
        Boro_Vai.__init__(self)
