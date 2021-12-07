import sys
from typing import List, Optional


class Event:
    def __init__(self, text: List[str], choices: List[str],
                 next_events: Optional[List['Event']], parent = Optional['Event']):
        self.text = text
        self.choices = choices
        self.next_events = next_events
        self.parent = parent

    def play(self):
        print("* ----------------- *")
        for line in self.text:
            print(line)
        print()

        print(f"Choices: ", end="")
        for i in self.choices:
            print(i, end=" ")
        print()

        if not self.choices:
            input("press [enter] to exit")
            sys.exit()

        choice = "not a choice 8379vngu2drf255"
        while choice not in self.choices:
            choice = input("Your choice: ")
            if choice not in self.choices:
                print("~that is not an option~")
        next = self.choices.index(choice)
        self.next_events[next].play()


event_death = Event(["YOU HAVE DIED"], [], None)

example_story = Event(["prvy event", "text k tomu", "dalsi text k tomu"], ["moznost1", "moznost2"],
                      [Event(["druhy event 1"], [], None),
                       event_death])

intro = ["You have boarded an aeroplane just like any other time.",
         "It takes off, no problem.",
         "Three hours into the flight, you hear your captain speaking:",
         "\"Dear passengers, I regret to inform you, but the plane ",
         "is having unexpected difficulties concerning three out of four engines.",
         "This is the best time to call your family.\"",
         "As if on cue, there is a sudden bang, as one of the engines engine rips itself to shreds.",
         "The plane starts to dip towards the ground .."]

preberie_sa_z_lietadla = Event(["You wake up.",
                                "It is quiet, it seems you are the only survivor.",
                                "You notice that your arm is bleeding.",
                                "If you do not stop the bleeding, you may bleed out",
                                "You see a glowing hot piece of metal, and a first-aid kit nearby"],
                               ["Cauterize the wound with the hot piece of metal",
                                "Patch it up using the first aid kit"], CHILDREN, None)

strati_vedomie_a_skape = Event(["As you press the piece of metal against the wound,",
                                "the pain turns your mind blank and you lose consciousness.",
                                "The wound was not yet sealed properly.",
                                "You have died .."], [], None, preberie_sa_z_lietadla)

zafacuje_to = Event([""], ["", ""], CHILDREN, preberie_sa_z_lietadla)


example_story.play()
