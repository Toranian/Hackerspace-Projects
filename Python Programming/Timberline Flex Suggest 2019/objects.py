class User:

    def __init__(self, *args):
        self.tags = list(args)

    def add_tags(self, *args):
        self.tags.append(args)
    
    def recommend(self, events):
        event_scores = {}
        for event in events:
            score = 0
            
            for tag in event.tags:
                if tag in self.tags:
                    score += 1
            event_scores[event] = score
        
        print(event_scores)
        return event_scores
    
    def add_events(self, events):
        for event in events:
            for tag in event.tags:
                self.tags.append(tag)
    
    def add_event(self, event):
        for tag in event.tags:
            self.tags.append(tag)

    def display(self):
        print(self.tags)


class Event:

    def __init__(self, title, description, tags):
        self.title = title
        self.description = description
        self.tags = tags
    
    def add_events(self, *args):
        self.tags.append(args)
    
    def display(self):
        print(self.title.center(50, '_'))
        print(self.description)
        print(self.tags)

    def __repr__(self):
        return self.title