with open ("aa.txt",'r',encoding= "utf-8") as f:
    a = f.readlines()
x = int(a[0])
y = int(a[1])
print(x*y)