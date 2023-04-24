# namespace,scope
x=5
x=4
y=2
# def f():
#     print("")

# import numpy as np
# np.f()

# uses of namespaces are in three areas:local,global,enclosing
# LEGB
# L=locals
# E=Enclosed
# G=global
# B=Built in
# Local scope
# s="I am global"

# def f():
#     s="I am local"
#     print(s)
# f()
# print(s)
# Local value can't change global

# s="I am global"
# def outer_scope():
#     s="I am local"
#     def inner_scope():
#         s="I am enclosed"
#         print(s)
#     inner_scope()
#     print(s)
# print(s)
# outer_scope()
# print(s)
# local,global,builtIn,enclosed

# enclosed>local>global>built_in
from math import pi
# print(pi)
pi=34.11
print(pi)

def outer():
    pi=33.11
    def inner():
        pi=32.11
        print(pi)
    inner()
    print(pi)
outer()
print(pi)