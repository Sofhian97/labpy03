a = 100000000
for i in range(1, 9):
    if (i >= 1 and i <= 2):
        b = a * 0
        print("Laba bulan ke- " , i , "sebesar" ,b)
    if (i >= 3 and i <= 4):
        c = a * 0.01
        print("Laba bulan ke- ",i , "sebesar", c)
    if (i >= 5 and i <= 7):
        d = a * 0.05
        print("Laba bulan ke- ", i, "sebesar", d)
    if (i == 8):
        e = a * 0.03
        print("Laba bulan ke- ", i, "sebesar", e)
        total = b + b + c + c + d + d + d - e
        print("Total laba adalah ", total)