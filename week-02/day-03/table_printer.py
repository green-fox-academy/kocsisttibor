# Create a function that prints the ingredient list of dictionaries to the 
# console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ 'vodka': 1, 'needs_cooling': True },
	{ 'coffee_liqueur': 0, 'needs_cooling': True },
	{ 'fresh_cream': 1, 'needs_cooling': True },
	{ 'captain_morgan_rum': 2, 'needs_cooling': True },
	{ 'mint_leaves': 0, 'needs_cooling': False },
	{ 'sugar': 100, 'needs_cooling': False },
	{ 'lime juice': 10, 'needs_cooling': True },
	{ 'soda': 100, 'needs_cooling': True }
]
lengths = []
for i in range(len(ingredients)):
    temp_list = list(ingredients[i].keys())
    lengths.append(len(temp_list[0]))
width = max(lengths) + 2

def table_printer(given_list):
    print("+" + "-" * (width) + "+---------------+----------+")
    print("| Ingredient" + " " * (width - len(" Ingredient")) + 
    "| Needs cooling | In stock |" )
    print("+" + "-" * (width) + "+---------------+----------+")
    for i in range(len(given_list)):
        temp_list = list(ingredients[i].keys())
        if ingredients[i]["needs_cooling"]:
            cool = "Yes"
        else:
            cool = "No"
        print("| " + temp_list[0] + " " * (width - len(temp_list[0]) - 1) 
        + "| " + cool + " " * (14 - len(cool)) + "| " 
        + str(ingredients[i][temp_list[0]]) + " " * 
        (9 - len(str(ingredients[i][temp_list[0]]))) + "|")
    print("+" + "-" * (width) + "+---------------+----------+")

table_printer(ingredients)
