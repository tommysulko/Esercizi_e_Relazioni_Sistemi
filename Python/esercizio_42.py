def main():
    def fibonacci(n,nScelto):
        for _ in range(1,nScelto):
            if n <= 1:
                return n
            else:
                return fibonacci(n-1,nScelto) + fibonacci(n-2, nScelto)

    limite = int(input("Inserisci il numero massimo oltre cui i valori della serie non vengono stampati: "))

    for num in range(1, limite+1):
        print(fibonacci(num,limite))

if __name__ == "__main__":
    main()