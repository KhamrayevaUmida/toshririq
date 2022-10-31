def mashq1():
    print("Siz string bo'limiga o'tdingiz!!!")
    a = int(input("""Kerakli raqamni kiriting:
    1-O'zingiz haqingizda ma'lumot: 
    2-registratsiya bo'limi: """))

    class Person:
        def __init__(self, ism, familiya, otchestvo, yosh):
            self.ism = ism
            self.familiya = familiya
            self.otchestvo = otchestvo
            self.yosh = yosh
        def seal(self):
            print("Ismi:", self.ism, ", Familiyasi:", self.familiya, ", Sharifi:", self.otchestvo, ", Yoshi:", self.yosh)
    
    odam1 = Person("Umida", "Hamrayeva", "Aliyevna", 19)


    if a == 1:
        print(odam1.seal())

    elif a == 2:
        b = int(input("Registratsiya uchun 1ni kiriting, kirish uchun 2ni kiriting: "))

        if b == 1:
            name = input("Ism va familiyangizni kiriting: ")
            parol1 = input("Kerakli parol uylab toping: ")
            print(name, "siz muvoffaqiyatli registratsiyadan utdingiz")

        elif b ==2:
            login = input("Loginingizni kiriting: ")
            parol2 = int(input("Parolni kiriting: "))

            if login == "Umida" and parol2 == 1234:
                print(login, "siz muvofaqqiyatli kirdingiz")
            elif login != "Umida" and parol2 == 1234:
                print("Login xato")
            elif login == "Umida" and parol2 != 1234:
                print("Parol xato")
            else:
                print("Xatolik")

        else:
            print("Xatolik")

    else:
        print("Xatolik")

    


mashq1()