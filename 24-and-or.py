# and,or -yo check 2 conditions at once
name="abc"
age=19
if name=="abc" and age==19:
    print("yo r right")
else:
    print("false")    
#----------------------
    name="abc"
age=19
if name=="abjc" and age==190:
    print("yo r right")
else:
    print("false")  

# or - any one should be true
name="abc"
age=19
if name=="abc" or age==10:
    print("yo r right")
else:
    print("false")   