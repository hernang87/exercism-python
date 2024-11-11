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
def value(colors):
    dec = colors[0]
    uni = colors[1]
    return colors_dict[dec] * 10 + colors_dict[uni]
