# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

def create_new_verbs(given_list, pre):
    new_verbs = [ pre for i in range(len(given_list))]
    for i in range(len(new_verbs)):
        new_verbs[i] = new_verbs[i] + given_list[i]
    
    print(new_verbs)

create_new_verbs(verbs, preverb)