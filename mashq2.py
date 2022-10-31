try:
    def mashq2():
        integ = int(input("""1-kalkulyator
2-toq sonlar
3-juft sonlar
4-ohiri 2ta 0 bilan tugaydigan sonlar: """))

        if integ == 1:
            def calc():
                print("Kalkulyatorga hush kelibsiz")
                a = int(input("1-son: "))
                amal = input("Amalni kiriting: ")
                b = int(input("2-son: "))

                if amal == "+":
                    print(a+b)
                elif amal == "-":
                    print(a-b)
                elif amal == "*":
                    print(a*b)
                elif amal == "/":
                    print(a/b)
                else:
                    print("Xatolik")

            calc()

        elif integ == 2:
            a = -1
            while a < 999:
                a += 2
                print(a)

        elif integ == 3:
            b = 0
            while b < 999:
                b += 2
                print(b)

        elif integ == 4:
            c = 0
            while c < 999:
                c += 100
                print(c)

    mashq2()

except ValueError:
    print("Siz string kirityapsiz intejer kiriting")
except:
    print("Xatolik bor")
