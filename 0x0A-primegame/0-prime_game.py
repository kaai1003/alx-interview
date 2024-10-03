#!/usr/bin/python3
"""Prime Game Module
"""
def isWinner(x, nums):
    """check winner of the game"""
    if x <= 0 or not nums:
        return None
    if x > len(nums):
        rounds = len(nums)
    rounds = x
    maria_wins = 0
    ben_wins = 0
    for i in range(rounds):
        n = nums[i]
        moves = 0
        remaining = set(range(2, n + 1))
        primes = prime_sieve(n)
        for prime in primes:
            if prime > n:
                break
            if prime in remaining:
                moves += 1
                multi = prime
                while multi <= n:
                    if multi in remaining:
                        remaining.remove(multi)
                    multi += prime
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return 'Ben'
    return None

def prime_sieve(n):
    """rime numbers func"""
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [j for j in range(2, n + 1) if primes[j]]
