

""" name ="Tolga"

print(name[0])

# Define a list
names=["tolga","neso","ipo","nazo"]
print(names)
print(names[0])
names.append("deneme")
print(names)
names.sort()
print(names)


#Create Set
s = set()
s.add("tolga")
s.add("neso")
s.add("nazo")
s.add("ipo")
s.add(1)
# no twice element in set
s.add(1)
print(s)
s.remove(1)
print(s)
print(F"the set has {len(s)} elements")

"""




""" n = int(input("Number : "))

if n>0 :
    print("n is positive")
elif n<0:
    print("n is negative")
else:
    print("n is zero")
    print("deneme1")

for i in range(n):
    print(i) """


#list
""" names = ["tolga","neso","ipo","nazo"] 
for name in names:
    print(name) """
#dict
houses = {"neso":"mkp ioo","ipo":"bhyal","nazo":"okyanus"}
houses["tolga"] = "house"

for s in houses:
    print(s +" : " + houses[s])


