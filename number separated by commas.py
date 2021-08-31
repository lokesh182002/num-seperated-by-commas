num=int(input("enter a number"))
sa=str(num)
for i in range(len(sa)-3,0,-3):
    sa=sa[:i]+','+sa[i:]
print("the number separated with commas is",sa)    
