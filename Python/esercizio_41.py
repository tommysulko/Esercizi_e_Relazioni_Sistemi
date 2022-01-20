def main():
    def fattoriale(n):
        if n==0:
            return 1
        else:
            return n*fattoriale(n-1)

    n = int(input('Inserire il numero: '))
    print (f"Il fattoriale è {fattoriale(n)}")

if __name__ == "__main__":
    main()