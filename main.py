import sys
from typing import List, Optional


class Event:
    def __init__(self, text: List[str], choices: List[str], next_events: Optional[List['Event']]):
        self.text = text
        self.choices = choices
        self.next_events = next_events

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
        next = self.choices.index(choice)
        self.next_events[next].play()


event_death = Event(["YOU HAVE DIED"], [], None)

example_story = Event(["prvy event", "text k tomu", "dalsi text k tomu"], ["moznost1", "moznost2"],
                      [Event(["druhy event 1"], [], None),
                       event_death])


example_story.play()
