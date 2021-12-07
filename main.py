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
                          "Do not follow the footprints, go in a different direction"], [], None)

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
                          "You have died .."], [], [], None)

zrobi_si_joint = Event(["You decide to roll a joint from the plants around you.",
                        "The pain fades away, as if it was never there.",
                        "From there you continue into the nearest building.",
                        "It seems to be a dressing room for the mercenaries working there.",
                        "There are several sets of extra uniforms and other gear"],
                       ["Dress as a guard",
                        "Do not dress a guard, continue as you are now"], [], None)

neprezlecie_sa = Event(["As you try to exit the room, another guard sees you.",
                        "You are executed.",
                        "You have died .."], [], [], None)

prezlecie_sa = Event(["You dress up as a guard. You fit in quite well.",
                      "As you take a look around, a man orders you",
                      "to execute a slave that has not fulfilled his quota.",
                      "He looks to be the chief around here."],
                     ["Comply", "Refuse, give alternate options."], [], None)

nepopravi_typka = Event(["You have chosen to refuse the order you have been given",
                         "and you give alternate solutions.",
                         "You are executed on basis of disobedience",
                         "You have died .."], [], [], None)

popravi_typka = Event(["You have complied with the order, executing the slave.",
                       "You are given a pass to go home for the weekend directly by the chief.",
                       "YOU HAVE WON", "",
                       "~but at what price?"], [], [], None)

ide_za_svetlom = Event(["You decide to follow the shimmering light in the distance.",
                        "On the way, you stumble across a patch of magic mushrooms."],
                       ["Eat some",
                        "Leave them be"], [], None)

nezje_lysohlavku = Event(["As you get closer to the light, there seem to be some buildings there.",
                          "On what looks like a small runway is a small plane,",
                          "it doesn't look like it is in the best condition."
                          "Several people are strolling about"],
                         ["Sneak onto the plane and hide",
                          "Ask one of the people there for help"], [], None)

poziada_o_pomoc = Event(["You decide to ask one of the people there for help.",
                         "They look like mercenaries and take you to their headquarters.",
                         "You are questioned and ultimately shot on basis of",
                         "being a spy or working with the government.",
                         "You have died .."], [], [], None)

infiltruje_lietadlo = Event(["You decide to infiltrate the plane.",
                             "It goes without problems, and you hide among the cargo of plastic-wrapped packages.",
                             "Soon enough, the plane takes off.",
                             "Several minutes after takeoff you smell smoke.",
                             "The plane starts to dip towards the ground .."], [], [], None)  # ->preberie_sa_z_lietadla

zje_lysohlavku = Event(["You take eat half a basket worth of mushrooms.", "",
                        "You have entered the world of fantasy and wonder.",
                        "You see a fat dragon to your left and a skinny griffin to your right"],
                       ["Go towards the dragon",
                        "Go towards the griffin"], [], None)

ide_za_griffinom = Event(["You decide to go towards the griffin.",
                          "It looks very skinny, as if it hasn't eaten is quite some time.",
                          "You are eaten by the griffin.",
                          "You have died .."], [], [], None)

ide_za_drakom = Event(["You decide to go towards the dragon.",
                       "The dragon tells you that he will eat you unless you answer his riddle correctly.",
                       "<If you had five mangoes and two bananas in one hand and two mangoes and four bananas",
                       "in the other hand, what would you have?>"],
                      ["Very large hands",
                       "Seven mangoes and six bananas"], [], None)

spocita_to = Event(["You have given your answer.",
                    "The dragon looks displeased by your answer.",
                    "You are eaten by the dragon",
                    "You have died .."], [], [], None)

spravna_odpoved = Event(["You have given your answer.",
                         "The dragon looks pleased by your answer and lets you go onward.",
                         "Soon, a pixie approaches you.",
                         "She offers you some pixie dust. ",
                         "She claims it will teleport you home. Will you accept?"],
                        ["Accept", "Decline"], [], None)

nezoberie_pixie_dust = Event(["You decline the offfer.",
                              "As soon as you do, the pixie and all other fantastical beasts",
                              "around you start to disappear.",
                              "", "You are surrounded by a tribe od indigenous people."],
                             ["Surrender",
                              "Try to escape"], [], None)


example_story.play()
