i = 3
correct = 50
while i > 0:
    ans = int(input("یک عدد وارد کنید: "))
    if ans == correct:
        print("بردی")
        break
    else:
        if ans < correct:
            print("یک عدد بزرگتر انتخاب کن")
        else:
            print("یک عدد کوچکتر انتخاب کن")
        i -= 1
else:
    print(f"{correct} درست بود")
    print("باختی")
