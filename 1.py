def najwiekszy_wspolny_dzielnik(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
        
    nwd = najwiekszy_wspolny_dzielnik(liczba1, liczba2)
    print("Największy wspólny dzielnik liczb", liczba1, "i", liczba2, "to:", nwd)
       
    

if __name__ == "__main__":
    main()

print(main)