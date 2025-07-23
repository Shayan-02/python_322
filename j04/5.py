lst = []

a = "hello"
print(len(a))

for i in range(4):
    a = int(input("nomreh: "))
    lst.append(a)

print(sum(lst)/len(lst))