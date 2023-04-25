# eiample-1

# lst=["hello","world","python"]
# new_lst=[i.upper() for i in lst]
# print(new_lst)

# eiample-2
# x=[i for i in range(1,10)]
# # print(x)
# y=list(range(1,10))
# print(y)
# example-3

# x="hello"
# # y=[i for i in x]
# y=list(x)
# print(y)

# example-4
# x=[i for i in range(1,20) if i % 2==0]
# print(x)

# example-5-double condition
# x=[i for i in range(100) if i%3==0 if i%5==0]
# print(x)

# example-6
# x=["even" if x%2==0 else "odd" for x in range(1,100)]
# print(x)

# example-7
# x=[(x,y) for x in [1,2,3,4,5] for y in [4,5,6,7,8] if x!=y]
# print(x)

# --------------dictionary comprehension---------
# example-1
# dct={i:i+5 for i in range(10)}
# print(dct)

# example-2
# dct={"jack":30,"hablu":23,"kablu":25}
# new_dct={k:v for k,v in dct.items() if v%2==0}
# print(new_dct)

# example-3
# dct={"jack":30,"hablu":22,"kablu":25}
# new_dct={k:v for k,v in dct.items() if v%2!=0 and v>18}
# print(new_dct)

# example-4
# dct={"jack":60,"karim":30,"rahim":40}
# new_dct={k:("Old" if v>50 else "young") for k,v in dct.items()}
# print(new_dct)

# example-5
dct={k1:{k2:k1*k2} for k2 in range(6) for k1 in range(5)}
print(dct)

# In summary--if there is any else condition then the condition will be in the right side ,otherwise the nested condition will be in the right side