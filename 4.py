from collections import Counter
f = open("D:/Yash.txt","r")
a=list((f.read().lower()).split(" "))
print(a)
length=len(a)
print(length)
mydict= Counter(a)
print(mydict)
max_value=max(mydict.values())
print(max_value)
print("Most frequent words in the text files are:")
for i in mydict:
    if mydict[i]==max_value:
        print(i,"occuring",mydict[i],"times")
f.close()