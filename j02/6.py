i = 0
while i < 10:
    print(i)
    i += 1

print("--------------")

for i in range(1, 110, 2):
    if i == 51:
        i += 10
        continue
    else:
        print(i)
