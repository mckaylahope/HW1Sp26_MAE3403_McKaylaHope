from random import normalvariate
import math


def main():
    # Given parameters
    mu = 10.0       # mean
    sigma = 2.0     # standard deviation
    N = 1000        # sample size

    # Generate normally distributed data
    data = []
    for _ in range(N):
        data.append(normalvariate(mu, sigma))

    # Sample mean
    sample_mean = sum(data) / N

    # Sample standard deviation
    variance = 0
    for x in data:
        variance += (x - sample_mean) ** 2
    variance /= N
    sample_std = math.sqrt(variance)

    print(f"Sample mean: {sample_mean:.4f}")
    print(f"Sample standard deciation: {sample_std:.4f}")

    # Standard deviation criteria
    count_1 = 0
    count_2 = 0
    count_3 = 0

    for x in data:
        if abs(x - sample_mean) <= sample_std:
            count_1 += 1
        if abs(x - sample_mean) <= 2 * sample_std:
            count_2 += 1
        if abs(x - sample_mean) <= 3 * sample_std:
            count_3 += 1

    print("\nStandard deviation criteria:")
    print(f"Within 1σ: {count_1 / N:.4f}")
    print(f"Within 2σ: {count_2 / N:.4f}")
    print(f"Within 3σ: {count_3 / N:.4f}")

if __name__ == "__main__":
    main()