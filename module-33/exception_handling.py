# try:if here is no error then it will work
# except:if error found
# else:if there is no error
# finaly:will always execute
# we can see an example

try:
    x=10/2
    print(x)
except ValueError:
    print("ValueError found")
except ZeroDivisionError:
    print("zeroDivisionError found")
else:
    print("no error found")
finally:
    print("I will be always printed")


