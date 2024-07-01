#!/usr/bin/python3

def isWinner(x, nums):
    def sieve(n):
        """
        Returns a list of primes up to n
        (inclusive) using the Sieve of Eratosthenes
        """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def simulate_game(n):
        """
        Simulates the game and returns the
        winner ('Maria' or 'Ben') for a given n
        """
        primes = sieve(n)
        numbers = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while True:
            available_primes = [p for p in primes if p in numbers]
            if not available_primes:
                return 'Ben' if turn == 0 else 'Maria'

            chosen_prime = available_primes[0]
            to_remove = set()
            for multiple in range(chosen_prime, n + 1, chosen_prime):
                if multiple in numbers:
                    to_remove.add(multiple)

            numbers -= to_remove
            turn = 1 - turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
