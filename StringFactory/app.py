template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(values):
    for idx, value in enumerate(values):
        values[idx] = template.format(**value)
    return values

values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
print string_factory(values)
