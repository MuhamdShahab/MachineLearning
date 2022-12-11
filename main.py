x = int(input())
y = int(input())
z = int(input())
n = int(input())
list1 = [x, y, z]
mylist = []
seclist = []
x1 = x
y1 = y
z1 = z
var = 0
while x1 >= 0:
    while y1 >= 0:
        while z1 >= 0:
            list1 = [x1, y1, z1]
            mylist.append(list1)
            for i in range(0,len(list1)):
                var = var+list1[i]
            if var != n:
                seclist.append(list1)
            z1 = z1 - 1
            var = 0
        z1 = z
        y1 = y1 - 1
    y1 = y
    x1 = x1 - 1
mylist.reverse()
print(mylist)
seclist.reverse()
print(seclist)
