from Die import rollFairDie as rfd
from Die import rollUnfairDie as rud
def main():
    rolls = 1000
    counts = [0] * 6

    for _ in range(rolls):
        value = rfd()
        counts [value - 1] +=1

    print("After rolling the fair die 1000 times:")
    for i in range(6):
        print(f"Probability of rolling a {i+1}: {counts[i]/rolls:.4f}")

def main2():
    rolls = 10000
    counts = [0] * 6

    for _ in range(rolls):
        value = rfd()
        counts[value-1] +=1

    print("\nAfter rolling the fair die 10,000 times:")
    for i in range(6):
        print(f"Probability of rolling a {i+1}: {counts[i]/rolls:.4f}")

def main3():
    rolls = 10000
    counts = [0] * 6

    for _ in range(rolls):
        value = rud()
        counts[value-1] +=1

    print("\nAfter rolling the unfair die 10,000 times:")
    for i in range(6):
        print(f"Probability of rolling a {i+1}: {counts[i]/rolls:.4f}")

if __name__ == "__main__":
    main()
    main2()
    main3()