# def greet():
#     print('good morning')
# greet()
# a=labda arg:expression
# a=lambda:print('hello good morning')
# a()
# example-1:
reverse_string=lambda string:string.upper()[::-1]
# print(reverse_string("shuvo"))
# example-2:
mx=lambda a,b:a if a>b else b
# print(mx(40,50))

lst=[1,2,3,4,5,6,7]
# new_lst=[lambda arg=x:arg*2 for x in lst]
# for i in new_lst:
#     print(i())
def a(x):
    return 2*x
# for i in lst:
#     print(a(i))

# filter,map,reduce-------example-4
# filter
# my_list=[1,2,3,4,5,6,7,8]
# my_new_list=list(filter(lambda x:(x%2==0),my_list))
# print(my_new_list)
# ---------map-----
# string_list=["hi","hello","bye"]
# new_list=list(map(lambda x:x.upper()[::-1],string_list))
# print(new_list)

# Reduce function
from functools import reduce
lst=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in range(len(lst)):
#     sum+=lst[i]
# print(sum)
sum=reduce(lambda a,b:(a+b),lst)
print(sum)