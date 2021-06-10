#Python Task Q3 Shubhang
def palindrome(name):
    if len(name)<=1:
        return True
    elif name[0]==name[-1]:
            return palindrome(name[1:-1])
    else:
        return False
def listtostring(s):
    for x in s:
        print("", x+':',hex(ord(x)))
y=str(input('enter string:'))
z=list(y)
w=len(z)
print ("\n")
if palindrome(z):
    print('it is palindrome')
    print ("\n")
    print ("\n")
    listtostring(z)
    print ("\n")
    print ("\n")
    print ("\n")
else:
    print ("\n")
    print ("\n")
    print('not palindrome')
    print ("\n")
    print ("\n")
    z.reverse()
    x=z[1:w] + z[w-1:0:-1]
    y=len(''.join(x))
    for i in range(1,w):
        print(' '.join(z[w-1:w-i:-1]+z[w-i:w]).center(y,' '))
    for i in range(w,0,-1):
        print(' '.join(z[w-1:w-i:-1]+z[w-i:w]).center(y,' '))
