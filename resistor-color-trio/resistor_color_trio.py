colors_dict = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}

unit_dict = {
    1000: 'kiloohms',
    1000000: 'megaohms',
    1000000000: 'gigaohms',
}

def label(colors):
    dec = colors_dict[colors[0]] * 10
    uni = colors_dict[colors[1]]
    zeros = colors_dict[colors[2]]
    ohms = (dec + uni) * 10 ** zeros

    keys = list(reversed(unit_dict.keys()))

    for key in keys:
        if ohms // key > 0:
            return f"{ohms // key} {unit_dict[key]}"
    return f"{ohms} ohms"
