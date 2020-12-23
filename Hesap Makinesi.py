giriş = """
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
(5) Kare Hesaplama
(6) Karekök Hesaplama
(7) Çıkış
"""

print(giriş)

while True:
    soru = input("Yapmak istediğiniz işlemin numarası: ")

    if soru == "7":
        print("Güle güle")
        break

    elif soru == "1":
        sayı1 = int(input("İlk sayı: "))
        sayı2 = int(input("İkinci sayı: "))
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

    elif soru == "2":
        sayı3 = int(input("İlk sayı: "))
        sayı4 = int(input("İkinci sayı: "))
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

    elif soru == "3":
        sayı5 = int(input("İlk sayı: "))
        sayı6 = int(input("İkinci sayı: "))
        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

    elif soru == "4":
        sayı7 = int(input("İlk sayı: "))
        sayı8 = int(input("İkinci sayı: "))
        print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

    elif soru == "5":
        sayı9 = int(input("Sayı: "))
        print(sayı9, "sayısının karesi =", sayı9 ** 2)

    elif soru == "6":
        sayı10 = int(input("Sayı: "))
        print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

    else:
        print("Hatalı giriş, lütfen tekrar deneyiniz.")
        print(giriş)
