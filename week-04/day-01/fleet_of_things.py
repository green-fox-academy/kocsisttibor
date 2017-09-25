from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

eat = Thing("Eat fruit")
walk = Thing("Walk")
train = Thing("Train")
sleep = Thing("Sleep")

eat.complete()
walk.complete()

fleet.add(eat)
fleet.add(walk)
fleet.add(train)
fleet.add(sleep)


print(fleet)