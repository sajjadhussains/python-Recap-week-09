# lst=[[j for j in range(3)] for i in range(4)]
# print(lst)

# this will create problem,because memory location allocated same for all the number 1 columns
# r,c=(5,5)
# lst=[[0]*c]*r
# lst[0][0]=1
# print(id(lst[0]))
# print(id(lst[1]))

# we will do
# lst=[[0 for i in range(5)] for i in range(3)]
# print(lst)

# lst =[[1,2,3],[4,5],[6,7,8]]
# new_lst=[sublist for val in lst for sublist in val]
# print(new_lst)

lst =[["hello","python"],["programmer","worker"],["ma","banana"]]
new_lst=[sublist for val in lst for sublist in val if len(sublist)>3]
print(new_lst)