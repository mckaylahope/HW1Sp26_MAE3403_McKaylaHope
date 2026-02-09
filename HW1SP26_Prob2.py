from Dice import rollDice, rollUnfairDice

def main():
    n = 3
    trials = 1000

    min_score = n
    max_score = 6 * n

    counts = {}
    for score in range(min_score, max_score + 1):
        counts[score] = 0

    for _ in range(trials):
        total = rollDice(N=n)
        counts[total] += 1

    print(f"After rolling {n} fair dice {trials} times:")
    for score in range(min_score, max_score +1):
        print(f"Probability of rolling {score}: {counts[score]/trials}")

def main2():
    n = 5
    trials = 1000

    min_score = n
    max_score = 6 * n

    counts = {}
    for score in range(min_score, max_score + 1):
        counts[score] = 0

    for _ in range(trials):
        total = rollUnfairDice(N=n)
        counts[total] += 1

    print(f"\nAfter rolling {n} unfair dice {trials} times:")
    for score in range(min_score, max_score +1):
        print(f"Probability of rolling {score}: {counts[score]/trials:.4f}")


if __name__ == "__main__":
    main()
    main2()