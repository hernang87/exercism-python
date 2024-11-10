def sum_of_multiples(limit, multiples):
    result = set()
    for m in multiples:
        for n in range(1, limit):
            value = n * m
            if value > limit:
                break
            if value < limit:
                result.add(value)

    return sum(result)
