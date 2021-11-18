import random
Alice = 0
Bob = 0

Alice = random.randint(1,6)
Bob = random.randint(1,6)
print(f"Dado Alice: {Alice}")
print(f"Dado Bob: {Bob}")
if Alice > Bob:
    print(f"Ha vinto Alice con {Alice}")
elif Alice == Bob:
        print(f"Pareggio")
else:
    print(f"Ha vinto Bob con {Bob}")