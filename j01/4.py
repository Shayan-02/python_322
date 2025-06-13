a = 10
b = 20
c = 30

if a > b and b < c:  # f , t
    print(1)
if a < b and b > c:  # t , f
    print(2)
if a < b and b < c:  # t , t -> bargharar
    print(3)
# -----------------
if a < b or b > c:  # t | f -> bargharar
    print(4)
