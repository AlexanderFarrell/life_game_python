import random
import datetime
from engine import *

# Variables for the entire game
grocery_cost = 100
groceries_per_visit = 100

# The player and all their skills and attributes
class Player:
    def __init__(self):
        self.money = 0
        self.food = 100
        self.job = None

        # Skills
        self.intelligence = 1
        self.fitness = 1
        self.social = 1
        self.art = 1

# A job the player can have
class Job:
    def __init__(self, name, salary, intelligence, fitness, social, art):
        self.name = name
        self.salary = salary 
        self.intelligence = intelligence
        self.fitness = fitness
        self.social = social
        self.art = art

# Variables for the game
player = Player()
jobs = [
    Job("Underwater Basket Weaver", 500, 10, 15, 1, 20),
    Job("Penguin Zoologist", 250, 15, 5, 10, 1),
    Job("File Clerk", 100, 1, 1, 1, 1)
]
date = datetime.date(2023, 11, 1)

# Each function below is a part of the game. Everything starts at the while loop at the end.

def begin_day():
    global player
    narrate(date.strftime("%A, %m %d, %Y"))
    narrate("You wake up")
    player.food -= 10
    narrate(f"You eat breakfast, and now you have {player.food} food left")


def shop():
    global player
    narrate("You decide to go downtown to a shopping center")
    choice = choose(['shop for groceries', 'go home'])
    if choice == "shop for groceries":
        player.money -= grocery_cost
        player.food += groceries_per_visit
        narrate(f"You go grocery shopping. It cost you {grocery_cost}, and you now have ${player.money}. You now have {player.food} food")
        
    elif choice == 'go home':
        narrate("You decide to go home instead")


def job_search():
    global jobs, player

    # Find all the available jobs
    available_jobs = []
    for j in jobs:
        if j.art <= player.art and j.fitness <= player.fitness and j.intelligence <= player.intelligence and j.social <= player.social:
            available_jobs.append(j)
    
    # Options - Find all the names of available jobs
    options = []
    for j in available_jobs:
        options.append(j.name)

    # Add quit as an option
    options.append('quit')

    # Actually ask the user what they'd like to do
    choice = choose(options)

    if choice == 'quit':
        # If the player wants to quit the job search
        narrate("You decide against any jobs currently available")
        return
    else:
        # Find the job that the player chose
        for j in jobs:
            if j.name == choice:
                player.job = j
                narrate(f"Congratulations, you were hired as a {j.name}")


def day_off():
    global player
    narrate("You decide what you want to do today")
    choice = choose(['read', 'shop', 'job search', 'exercise', 'play guitar'])
    if choice == 'read':
        player.intelligence += 1
        narrate(f"You read for the day, and your intelligence is now {player.intelligence}")
    elif choice == 'shop':
        shop()
    elif choice == 'job search':
        job_search()
    elif choice == 'exercise':
        player.fitness += 1
        narrate(f"You decide to work out, and your fitness is now {player.fitness}")
    elif choice == 'play guitar':
        player.art += 1
        narrate(f"You decide to play guitar, and your artistic abilities are now level {player.art}")


def work():
    global player
    narrate(f"You go to your job as a {player.job.name}")
    player.money += player.job.salary
    narrate(f"You make ${player.job.salary}, and now have ${player.money}")



def decide():
    global date, player
    if date.weekday() == 5 or date.weekday() == 6:
        # Weekend
        day_off()
    else:
        # Weekday
        if player.job is not None:
            choice = choose(['work', 'quit job'])
            if choice == "work":
                work()
            else:
                narrate("You quit your job")
                player.job = None
                day_off()
        else:
            day_off()


def end_day():
    global player
    narrate("You had a long day")
    player.food -= 10
    narrate(f"You eat dinnner, and now you have {player.food} food left")
    narrate("You go to sleep\n")

while True:
    begin_day()
    decide()
    end_day()
    date = date + datetime.timedelta(days=1)
