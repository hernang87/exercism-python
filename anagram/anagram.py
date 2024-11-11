def find_anagrams(word, candidates):
    letters = sorted([c.lower() for c in word])
    results = []
    for candidate in candidates:
        candidates_letters = sorted([c.lower() for c in candidate])
        if letters == candidates_letters and word.lower() != candidate.lower():
            results.append(candidate)
    return results