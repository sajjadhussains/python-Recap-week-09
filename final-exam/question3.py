a=5 #global scope

def outer():
    a=6 #local variable or scope,which can't change global scope
    def inner_outer():
        a=7 #enclosed variable or scope,which can't cange it's outer scope
        print(a)
    inner_outer()
outer()
print(a)


