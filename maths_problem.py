def number_swapping(a, b, c):

    print("Inițial:     ", a, b, c)
    

    while a != b or a != c or b != c:

        if (a % 2 == b % 2) or (a % 2 == c % 2) or (b % 2 == c % 2):

            if a % 2 == b % 2:
                a = int(a)
                b = int(b)
                c = int(c)
                if a < b:
                    a = int((a + b) / 2)
                    print("După un pas: ", a, b, c)
                    a = int(a)
                    b = int(b)
                    c = int(c)
                if b < a :
                    b = int((a + b) / 2)
                    print("După un pas: ", a, b, c)
                    a = int(a)
                    b = int(b)
                    c = int(c)
            if b % 2 == c % 2:
                a = int(a)
                b = int(b)
                c = int(c)
                if b < c:
                    a = int(a)
                    b = int(b)
                    c = int(c)
                    b = int((b + c) / 2)
                    print("După un pas: ", a, b, c)
                if c < b:
                    a = int(a)
                    b = int(b)
                    c = int(c)
                    c = int((c + b) / 2)
                    print("După un pas: ", a, b, c)
            if a % 2 == c % 2:
                a = int(a)
                b = int(b)
                c = int(c)
                if (a + c) / 2 == b:
                    a = int(a)
                    b = int(b)
                    c = int(c)
                a = int(a)
                b = int(b)
                c = int(c)
                if (a + c) / 2 < b:
                    a = (a + c) / 2
                    a = int(a)
                    b = int(b)
                    c = int(c)
                    print("După un pas: ", a, b, c)
                a = int(a)
                b = int(b)
                c = int(c)
                if (a + c) / 2 > b:
                    c = int((a + c) / 2)
                    a = int(a)
                    b = int(b)
                    c = int(c)
                    print("După un pas: ", a, b, c)
                a = int(a)
                b = int(b)
                c = int(c)
        if  a % 2 == b % 2 == c % 2:
            a = int(a)
            b = int(b)
            c = int(c) 

            a = int(a)
            b = int(b)
            c = int(c)
            print("După un pas: ", a, b, c)
            a = int(a)
            b = int(b)
            c = int(c)
        if a == b - 1 == c - 2:
            a = (a + c) / 2
            a = int(a)
        if a == b or b == c or c == a:
            for i in range(1): 
                print("Final:       ", a, b, c)
            a = None
            b = None
            c = None

x = int(input("Care este valoarea primului număr? "))
y = int(input("Care este valoarea celui de-al doilea număr? "))
z = int(input("Care este valoarea celui de-al treilea număr? "))

number_swapping(x, y, z)
