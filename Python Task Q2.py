#Python Task Q2 
list = [2,7,5,4,5,2,8,9,1,2]
print ("Original: " + str(list))
res = []
for i in list:
	if i not in res:
		res.append(i)
print ("\n")
print ("New : " + str(res))

def add_tuple(x):
    sum=0
    for y in x:
      sum +=y

    return sum
print ("\n")

sum_tuple = add_tuple(res)
print("sum=", sum_tuple)
