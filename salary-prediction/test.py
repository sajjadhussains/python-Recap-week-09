import pandas as pd
import math
import json
import matplotlib.pyplot as plt

data=pd.read_csv("./datasets/salary.csv")
headers=data.columns.values

X=data[headers[0]]
Y=data[headers[1]]
X=X.truncate(4900,4999)
Y=Y.truncate(4900,4999)

with open("./datasets/trained_data.txt",'r') as file:
    data=file.read()
    converted=json.loads(data)
    
m=converted["m"]
c=converted["c"]
Y_mean=converted["Y_mean"]
Y_predicted_list=[]
r_upper=0
r_lower=0

for indx in range(len(X)):
    Y_predicted=(m*X[indx+4900])+c
    Y_predicted_list.append(Y_predicted)
    r_upper+=math.pow((Y[indx+4900]-Y_predicted),2)
    r_lower+=math.pow((Y[indx+4900]-Y_mean),2)

r_square=1-(r_upper/r_lower)
print(r_square)

inp=int(input("Enter Year of Experience: "))
predicted=m*inp+c
print(predicted)
# for val in X:
#     Y_predicted=(m*val)+c
#     Y_predicted_list.append(Y_predicted)

# plt.scatter(X,Y,color="g")
# plt.plot(X,Y_predicted_list,color="r")
# plt.show()