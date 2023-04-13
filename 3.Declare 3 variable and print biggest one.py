a= int(input("Enter no 1: ") )
b= int(input("Enter no 2: ") )
c= int(input("Enter no 3: ") )
biggest=0

if a>b or a>c:
    biggest = a
if b>c or b>a:
    biggest = b
if c>a or c>b:
    biggest = c
print(f"biggest no is :{biggest}")
