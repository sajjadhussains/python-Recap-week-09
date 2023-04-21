#int,float
#string,tuple,list
#dictionary,set
# a=1200000023423423.23442387475
# print(a+1) in c or c++ big number calculation is difficult but python makes it easy

# lst = [1,2,3,4,5,6,7,8,9,10]
# print(lst[-10])  #python allows negetive indexing for array

# lst1=[1,2,3,4]
# lst2=[5,6,7,8]
# lst3=[9,10,11]
# print(lst1+lst2+lst3) #two or more list adding is easier in python

# lst=[1,2,3,4,5,6,[7,8,[11,12,[13,14]]]]
# print(lst[6][2][2][1]) #in a complex list accessing element is easier in python

# lst=[1,2,3,[4,5]]
# lst.extend([10,20,30])
# print(lst) # using extend function we can add more element in a list

# ----------------Tuple--------------
tp=(1,2,3,4,5,[5,10,15])
# tp[0]=2   --we can't change tuple element after declaring
# tp[5][2]=50 --if in a tuple any list have,then we can change list element only within a tuple
# print(tp[5])
# --------------Dictionary------------
dct={"rahim":12000,"karim":20000}
# print(dct.get("rahim",False))--this tecniqu handles errors
# print(dct["halim"])-->if there is no key found by this name,then error comes

child1={
    "name":"jack",
    "year":2002
}
child2={
    "name":"emila",
    "year":2004
}
child3={
    "name":"kaniz",
    "year":2006
}
myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
# print(myfamily["child2"]["year"])
# print(myfamily.get("child2",False).get("name",False))

# converting list of tuple to a dictionary
a=[(1,'A'),(2,'B'),(3,'C'),(4,'D')]
output=dict(a)
# output.pop(3)
# print(output.keys())
# print(output.values())
# for key,values in output.items():
#     print(f'Key: {key}: Value:{values}')

# list2=[12,13,14]
# print(14 in list2)
# ---------------Set----------
# st={1,2,2,3,3,3}
# print(st)
# ----------------String-----------
s="3 I love python"
# print(s[::-1])----reverse string by single line of litle code
# print(s[0].isalpha())
print(s[0].isalnum())