# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

missing = "always takes longer than"

quote = quote.replace("It you", "It " + missing + " you")
print(quote)

