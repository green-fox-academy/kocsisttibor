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
	{ 'captain_morgan_spiced_rum': 2, 'needs_cooling': True },
	{ 'mint_leaves': 0, 'needs_cooling': False },
	{ 'sugar': 100, 'needs_cooling': False },
	{ 'lime juice': 10, 'needs_cooling': True },
	{ 'soda': 100, 'needs_cooling': True }
]


def col_width(content_list):
    lengths = []
    for i in range(len(content_list)):
        temp_list = list(content_list[i].keys())
        lengths.append(len(temp_list[0]))
    return max(lengths) + 2


def table_header(content_list):
    print("+" + "-" * col_width(content_list) + "+---------------+----------+")
    print("| Ingredient" + " " * (col_width(content_list) - len(" Ingredient"))
     + "| Needs cooling | In stock |" )


def separator(content_list):
    print("+" + "-" * col_width(content_list) + "+---------------+----------+")    


def table_body(content_list):
    for i in range(len(content_list)):                   
        keys = list(content_list[i].keys())

        if content_list[i]["needs_cooling"]:
            cool = "Yes"
        else:
            cool = "No"
        
        first_col = col_width(content_list) - len(keys[0]) - 1
        second_col = 14 - len(cool)
        stock = str(content_list[i][keys[0]])
        third_col = 9 - len(stock)

        print("| " + keys[0] + " " * first_col + "| " + cool + " " * second_col
         + "| " + stock + " " * third_col + "|")           
 
 
def table_printer(content_list):
    table_header(content_list)
    separator(content_list)
    table_body(content_list)
    separator(content_list)

table_printer(ingredients)
