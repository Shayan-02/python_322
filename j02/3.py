majmoo = 0
tedad = 0
while True:
    num = int(input("یک عدد وارد کنید: "))
    if num == 0:
        break
    tedad += 1
    majmoo += num
print(majmoo / tedad)
