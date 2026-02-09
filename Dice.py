from Die import rollFairDie, rollUnfairDie

def rollDice(N=1):
    """
    Rolls N fair dice and returns the total score.
    :param N: number of dice to roll
    :return: total sum of the dice
    """
    total = 0
    for _ in range(N):
        total += rollFairDie()
    return total

def rollUnfairDice(N=1):
    """
    Rolls N unfair dice and returns the total score.
    """
    total = 0
    for _ in range(N):
        total += rollUnfairDie()
    return total