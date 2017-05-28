class Reporter:
    def __init__(self, refresh):
        self.messages = []
        self.refresh = refresh

    def new_message(self, message, main_organism=None, other_organism=None):
        self.messages.append(main_organism + ': ' + message + other_organism)
        self.refresh()
