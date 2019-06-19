from objects import *

hackerspace = Event(
    "Hackerspace", 
    "Come get your hack on", 
    ["tec", "crt", "ct", "cmn",],
)

at_issue = Event(
    "At Issue", 
    "Come learn about stuff!",
    ["crt", "ct",],
)

events = [hackerspace, at_issue]

isaac = User()
isaac.add_event(hackerspace)
isaac.display()
x = isaac.recommend(events)
print(x)