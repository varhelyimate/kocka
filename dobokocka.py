import random

def dobas():
    return random.randint(1, 6)

def main():
    print("🎲 Kockadobó szimulátor 🎲")
    while True:
        input("Nyomj Entert a dobáshoz...")
        eredmeny = dobas()
        print(f"A dobás eredménye: {eredmeny}")
        
        ujra = input("Szeretnél újra dobni? (i/n): ").lower()
        if ujra != "i":
            print("Köszönöm a játékot! 👋")
            break

if __name__ == "__main__":
    main()
