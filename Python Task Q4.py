#Python Task Q4
import csv

with open('names.csv', 'w', newline='') as g:
    thewriter = csv.writer(g)
    thewriter.writerow(['xyq',2])
    thewriter.writerow(['rit', 3])
    thewriter.writerow(['tuH', 4])
import operator
sample = open('names.csv', 'r')
csvl= csv.reader(sample, delimiter=',')
sort= sorted(csvl, key= operator.itemgetter(1))
for x in sort:
    print(x)
sort1=list(sort)
for y in sort1:
    for a in y[1]:
        a=int(a)
        if a%2==0:
            print(y)
str1=''
for z in sort1:
    b=z[0]
    str1=str1+b
print(str1)
for t in str1:
    print(hex(ord(t)))
str2=[]
for m in str1:
    for n in str1:
        if m!=n:
            asciidiff=(str(abs((ord(m)-ord(n)))))
            str2.append(asciidiff)
            for i in range(0, len(str2)):
                str2[i]=int(str2[i])
            small=min(str2)
            if small:
                one=m
                two=n
print(min(str2))
