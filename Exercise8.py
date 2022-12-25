# count "h" from your name
name=input("enter your name: ")
temp=""   # temp means we have counted it once so no need to count it twice
i=0
while i <len(name):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i+=1