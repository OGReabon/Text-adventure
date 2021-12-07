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
         "As you fly over a group of islands, you hear your captain speaking:",
         "\"Dear passengers, I regret to inform you, but the plane ",
         "is having unexpected difficulties concerning three out of four engines.",
         "This may be the best time to call your family.\"",
         "As if on cue, there is a sudden bang, as one of the engines engine rips itself to shreds.",
         "The plane starts to dip towards the ground .."]

# TODO link all events after all are declared, add pictures

preberie_sa_z_lietadla = Event(["You wake up.",
                                "It is quiet, it seems you are the only survivor.",
                                "You notice that your arm is bleeding.",
                                "If you do not stop the bleeding, you may bleed out.",
                                "You see a glowing hot piece of metal, and a first-aid kit nearby"],
                               ["Cauterize the wound with the hot piece of metal",
                                "Patch it up using the first aid kit"], [], None)

strati_vedomie_a_skape = Event(["As you press the piece of metal against the wound,",
                                "the pain turns your mind blank and you lose consciousness.",
                                "The wound was not yet sealed properly.",
                                "You have died .."], [], None, None)

zafacuje_to = Event(["You bandage your arm, it seems to have helped tremendously.",
                     "What now?"],
                    ["Explore the island along the shore",
                     "Explore the island - head inland"], [], None)

stmieva_sa = Event(["So far you have found nothing of interest.",
                    "It is getting dark very fast, and you see a glimmer of light in the distance.",
                    "Or is it yor mind playing tricks?"],
                   ["Set up a shelter for the night",
                    "Go towards the light"], [], None)

urobi_si_shelter = Event(["You wake up in your shelter,",
                          "but you notice that you seem to be missing a kidney.",
                          "There is a line of stitches just where your kidney should have been,",
                          "and it hurts quite a bit.",
                          "You notice footprints in the soft soil."],
                         ["Follow the footprints",
                          "Do not follow the footprints, go the opposite direction"], [], None)

nasleduje_stopy = Event(["Tou follow the footprints for quite a while.",
                         "Finally, you notice a large field of what seems like marijuana, tall as a person.",
                         "There are guards patrolling the edges if the field.",
                         "Behind the field there are several buildings, and one as big as a plane hangar"],
                        ["Sneak by the guards into the field",
                         "Pacify a guard and take his equipment"], [], None)

spacifikuje_straz = Event(["You ambush one of the patrolling guards.",
                           "In the struggle you get shot several times as you have no training",
                           "You have died .."], [], [], None)

vplizi_sa_dnu = Event(["You sneak into the field when no one can see you.",
                       "The wound where your kidney was starts to hurt quite considerably."],
                      ["Make a joint and continue",
                       "Do not make a joint and continue"], [], None)

nezrobi_si_joint = Event(["You choose not to make a joint.",
                          "The spiking pain gets grows in intensity,",
                          "to the point when you are not able to suppress a scream.",
                          "You hear barking of dogs, it gets closer and closer by the second.",
                          "You are devoured by a pack of hounds.",
                          "You have died .."], [""], [], None)

zrobi_si_joint = Event(["You decide to roll a joint from the plants around you.",
                        ""], [""], [], None)


example_story.play()
