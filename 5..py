a = int (input ("enter a no:"))
if a>0 and a<100:
    if a>90 and a<100:
        print("super smart")
    if a>80 and a<90:
        print("smart")
    if a>70 and a<80:
        print("smart enough")
    if a>60 and a<70:
        print("just smart")
    if a>35 and a<60:
        print("no smart")
    if a>0 and a<35:
        print("dumb")
else:
    print("invalid number")
