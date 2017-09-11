# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
daily_hours = 6
weeks = 17
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
workdays = 5
coding_hours = daily_hours * weeks * workdays
print(coding_hours)
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52
weekly_hours = 52
print(coding_hours / (weekly_hours * weeks))

