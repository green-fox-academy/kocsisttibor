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


def width(in_list):             #column-width?
    lengths = []
    for i in range(len(in_list)):
        temp_list = list(in_list[i].keys())
        lengths.append(len(temp_list[0]))
    return max(lengths) + 2


def table_header(in_list):
    print("+" + "-" * width(in_list) + "+---------------+----------+")
    print("| Ingredient" + " " * (width(in_list) - len(" Ingredient")) + 
    "| Needs cooling | In stock |" )
    print("+" + "-" * width(in_list) + "+---------------+----------+")    # separator (use also for footer)


def table_body(in_list):
    for i in range(len(in_list)):                   #only in_list
        temp_list = list(in_list[i].keys())
        if in_list[i]["needs_cooling"]:
            cool = "Yes"
        else:
            cool = "No"
        print("| " + temp_list[0] + " " * (width(in_list) - len(temp_list[0]) - 1) 
        + "| " + cool + " " * (14 - len(cool)) + "| " 
        + str(in_list[i][temp_list[0]]) + " " * 
        (9 - len(str(in_list[i][temp_list[0]]))) + "|")             #create variables before, not in print
    print("+" + "-" * width(in_list) + "+---------------+----------+")


def table_printer(in_list):
    table_header(in_list)
    table_body(in_list)

table_printer(ingredients)
