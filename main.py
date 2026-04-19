def hisobla():
    sonlar = []
    n = int(input("List uchun necha son kiriting: "))
    for i in range(n):
        son = int(input(f"{i+1}-sonni kiriting: "))
        sonlar.append(son)
    print("Siz kiritgan sonlar:", sonlar)

    yigindi = sum(sonlar)
    print("Sonlar yig'indisi:", yigindi)

    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    print("Sonlar kopaytmasi:", kopaytma)

    max_son = max(sonlar)
    min_son = min(sonlar)
    print("Eng katta son:", max_son)
    print("Eng kichik son:", min_son)

    sonlar.sort()
    print("Kichidan kattagacha tartiblangan sonlar:", sonlar)
    sonlar.sort(reverse=True)
    print("Kattadan kichikgacha tartiblangan sonlar:", sonlar)

    juft_sonlar = [son for son in sonlar if son % 2 == 0]
    toq_sonlar = [son for son in sonlar if son % 2 != 0]
    print("Juft sonlar:", juft_sonlar)
    print("Toq sonlar:", toq_sonlar)

hisobla()

def list_boshi():
    sonlar = [12, 45, 7, 23, 56, 89, 34]
    print("List:", sonlar)
    yigindi = sum(sonlar)
    print("Yig'indisi:", yigindi)
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    print("Kopaytmasi:", kopaytma)

list_boshi()

def list_oxiri():
    sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("List:", sonlar)
    yigindi = sum(sonlar)
    print("Yig'indisi:", yigindi)
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    print("Kopaytmasi:", kopaytma)

list_oxiri()