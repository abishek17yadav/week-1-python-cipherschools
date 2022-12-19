#elif - for multiple condition
# show tickets
# 1-3 free
# 4-10 (100)
# 11-60 (500)
# above 60 (10)

age=int(input("enter your age:"))
if 0<age<=3:
    print("ticket price : free")
elif 4<age<=10:
    print("ticket price : 100") 
elif 11<age<=60:
    print("ticket price : 500")
else:
    print("ticket price : 10") 

