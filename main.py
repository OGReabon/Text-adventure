import sys
from typing import List, Optional


class Events:
    def __init__(self, text: str, choices: List[str], next_events: Optional[List['Events']]):
        self.text = text
        self.choices = choices
        self.next_events = next_events

    def play(self):
        print("* ----------------- *")
        print(self.text)
        print()
        print(f"Choices: ", end="")
        for i in self.choices:
            print(i, end=" ")
        print()
        choice = "not a choice 8379vngu2rf255"

        if not self.choices:
            input("press [enter] to exit")
            sys.exit()

        while choice not in self.choices:
            choice = input("Your choice: ")
        next = self.choices.index(choice)
        self.next_events[next].play()


example_story = Events("prvy event", ["moznost1", "moznost2"],
                       [Events("druhy event 1", [], None),
                        Events("druhy event 2", [], None)])


example_story.play()
