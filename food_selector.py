def food_selection(**kwargs):
    """
    The following code randomly selects a list of recipes for the user to buy ingredients on a per week basis.

    Returns a JSON-serializable object that implements the configured data paths:
        food_1
        list_1
        food_2
        list_2
        food_3
        list_3
        food_4
        list_4
        food_5
        list_5
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    # import phantom.rules as phantom
    import random

    food = {
        "Hibachi": ['chicken breast', 'shrimp sauce', 'zucchini', 'red onion', 'yellow squash', 'shredded carrots'],
        "Cheese Burger": ['hamburger patties', 'buns', 'french fries'],
        "Chicken Tomato Squash": ['cherry tomato', 'spaghetti squach', 'grilled chicken', 'basil'],
        "Steak & Baked Potato": ['Newyork strip', 'potato'],
        "Chicken Parm Sliders": ['chicken', 'mozzarella cheese', 'sweet rolls', 'pine nuts', 'basil', 'garlic'],
        "Chicken Brian": ['white wine', 'chicken strips', 'goat cheese', 'lemond', 'butter', 'sundried tomato',
                          'olive oil', 'garlic', 'basil', 'red onion'],
        "Grilled Pizza": ['pizza crust', 'pineapple', 'bbq sauce', 'grilled chicken', 'mozzarella'],
        "Spaghetti": ['ground beef', 'spaghetti sauce', 'spaghetti noogles'],
        "Grilled  Asparagus & Lemon Chicken": ['asparagus', 'lemond', 'italian herbs', 'garlic'],
        "Jamaican Chicken Jerk Taco": ['grilled chiken', 'smoked spice', 'pineapple', 'red onion', 'cilantro',
                                       'taco shells'],
        "Mexican Street Taco": [],
        "Zucchini Chicken": ['olive oil', 'chicken breast', 'zucchini', 'yellow squash', 'red onion', 'garlic'],
        "Avocado Smothered Chicken": ['avocado', 'pepper jack', 'salsa', 'cilantro'],
        "Beef Ribs & Sweet Potato": ['beef ribs', 'rib rub', 'sweet potato', 'bbq sauce'],
        "Jerk Chicken Rice Bowl": ['chicken thighs', '1/2  yellow onion', 'garlic', '1 cup  white rice',
                                   'One 15 ounce can red kidney beans', '1 cup chicken broth', '1 can coconut milk',
                                   'Couple sprigs of fresh thyme', '1 bunch green onion', 'ginger', '3-4 jalapeno',
                                   'lemond', 'lime'],
        "BBQ Chicken w/ Sweet Rolls": ['bbq sauce', 'chicken thighs', 'sweet rolls']}
    key1 = random.choice(list(food.keys()))
    key2 = random.choice(list(food.keys()))
    while key1 == key2:
        key2 = random.choice(list(food.keys()))

    key3 = random.choice(list(food.keys()))
    while key1 == key3 or key2 == key3:
        key3 = random.choice(list(food.keys()))

    key4 = random.choice(list(food.keys()))
    while key1 == key4 or key2 == key4 or key3 == key4:
        key4 = random.choice(list(food.keys()))

    key5 = random.choice(list(food.keys()))
    while key1 == key5 or key2 == key5 or key3 == key5 or key4 == key5:
        key5 = random.choice(list(food.keys()))

    f1 = food[key1]
    list_1 = '\n'.join(map(str, f1))
    f2 = food[key2]
    list_2 = '\n'.join(map(str, f2))
    f3 = food[key3]
    list_3 = '\n'.join(map(str, f3))
    f4 = food[key4]
    list_4 = '\n'.join(map(str, f4))
    f5 = food[key5]
    list_5 = '\n'.join(map(str, f5))
    outputs = {
        'food_1': key1,
        'list_1': list_1,
        'food_2': key2,
        'list_2': list_2,
        'food_3': key3,
        'list_3': list_3,
        'food_4': key4,
        'list_4': list_4,
    }

    # Write your custom code here...

    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
