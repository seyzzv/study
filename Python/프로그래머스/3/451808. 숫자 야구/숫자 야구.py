from itertools import permutations

def solution(n, submit):
    candidates = list(permutations('123456789', 4))
    guesses = [tuple(str(i)) for i in range(1000, 10000)]

    def get_result(guess, password):
        strike = sum(a == b for a, b in zip(guess, password))
        ball = sum(x in password for x in guess) - strike
        return strike, ball

    first = tuple('1123')
    s, b = map(int, submit(int(''.join(first))).replace('S', '').replace('B', '').split())
    candidates = [p for p in candidates if get_result(first, p) == (s, b)]

    for _ in range(n - 1):
        if len(candidates) == 1:
            return int(''.join(candidates[0]))

        best_guess = None
        best_score = (float('inf'), float('inf'))

        for guess in guesses:
            counts = [0] * 25

            for password in candidates:
                strike, ball = get_result(guess, password)
                counts[strike * 5 + ball] += 1

            score = (max(counts), sum(x * x for x in counts))

            if score < best_score:
                best_score = score
                best_guess = guess

        s, b = map(int, submit(int(''.join(best_guess))).replace('S', '').replace('B', '').split())
        candidates = [
            p for p in candidates
            if get_result(best_guess, p) == (s, b)
        ]

    return int(''.join(candidates[0]))