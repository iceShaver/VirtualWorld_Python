from Organisms.Organism import Organism


class Reporter:
    def __init__(self):
        self.messages = []

    def new_message(self, message, main_organism=None, other_organism=None):
        self.messages.append(str(main_organism) + ': ' + message + (str(other_organism) if other_organism is not None else ''))
        print(self.messages[-1])