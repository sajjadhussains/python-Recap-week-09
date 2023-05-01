n=int(input("Please Enter an Integer Input: "))

new_list=[i for i in range(1,n+1)]
def print_lst(lst):
    for i in lst:
        print(i,end='')
    print("")
for i in range(n):
    if i==0:
        print_lst(new_list)
    else:
        copy_num=new_list[i]
        new_list[i]=new_list[i-1]
        new_list[i-1]=copy_num
        print_lst(new_list)

