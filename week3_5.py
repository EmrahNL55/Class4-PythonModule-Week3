def palindrom(a):
    a = a.lower()
    if a == a[::-1]:
        print(True)
    else:
        print(False)

palindrom(input("lutfen bir kelime giriniz:"))