def part1(size):
    recipes = list()
    recipes.append(3)
    recipes.append(7)
    e1 = 0
    e2 = 1

    while len(recipes) - 10 < size:
        new_recipe = recipes[e1] + recipes[e2]
        if new_recipe > 9:
            recipes.append(1)
        recipes.append(new_recipe % 10)
        e1 = (1 + e1 + recipes[e1]) % len(recipes)
        e2 = (1 + e2 + recipes[e2]) % len(recipes)
    sub_list = recipes[size:size + 10]
    return reduce(lambda x, y: str(x) + str(y), sub_list)


def part2(val):
    input_recipe = map(int, str(val))
    offset = len(input_recipe)
    recipes = list()
    recipes.append(3)
    recipes.append(7)
    e1 = 0
    e2 = 1

    while True:
        new_recipe = recipes[e1] + recipes[e2]
        if new_recipe > 9:
            recipes.append(1)
        recipes.append(new_recipe % 10)
        num_recipes = len(recipes)
        e1 = (1 + e1 + recipes[e1]) % num_recipes
        e2 = (1 + e2 + recipes[e2]) % num_recipes
        if recipes[num_recipes - offset:] == input_recipe:
            return num_recipes - offset
        if recipes[num_recipes - offset - 1:num_recipes - 1] == input_recipe:
            return num_recipes - offset - 1


# 7861362411
print part1(919901)

# 20203532
print part2(919901)
