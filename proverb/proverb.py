def proverb(*args, **kwargs):
    if len(args) == 0:
        return []

    result = []

    qualifier = kwargs.get("qualifier")
    if qualifier != None:
        qualifier += " "
    else:
        qualifier = ""

    for n in range(len(args) - 1):
        result.append(f"For want of a {args[n]} the {args[n + 1]} was lost.")

    result.append(f"And all for the want of a {qualifier}{args[0]}.")
    return result
