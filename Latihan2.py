a = 0
while True:
    n = int(input("Masukkan bilangan: "))
    if a < n :
        a = n
    elif n == 0:
        break
print("Bilangan terbesar adalah: ",a)