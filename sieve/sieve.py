def primes(limit):
    result = []
    for n in range(2, limit+1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            result.append(n)
    return result
