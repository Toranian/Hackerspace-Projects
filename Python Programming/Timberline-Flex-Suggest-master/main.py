# Isaac Morrow, 2018
# Suggests a flex event to a student using tags


class MakeEvent:
    """The teacher makes an event with a name and tags that relate to that
    flex event."""

    def __init__(self, name, *args):
        self.name = name
        self.tags = args
        self.score = 0


class Student:
    """Holds the students tags."""

    def __init__(self, *args):
        self.tags = list(args)

    def select_event(self, event):
        for tag in event.tags:
            self.tags.append(tag)

    def get_tags(self):
        print(self.tags)
        return self.tags

    def find(self, ls):
        tmp = 0
        for i in ls:
            if i.score > tmp:
                tmp = i.score
        out.append(i.name)
        print(i.score)
        i.score = 0

    def suggest(self, event_list, suggest_amount):
        self.suggest_amount = suggest_amount
        self.event_scores = []

        # Make the score for the flex events
        for event in event_list:
            self.score = 0
            for event_tag in event.tags:
                for student_tag in self.tags:
                    if student_tag == event_tag:
                        self.score += 1
                    else:
                        pass
            event.score = self.score
            self.event_scores.append(event)

        # Show scores
        for i in self.event_scores:
            print("{} | {}".format(i.name, i.score))

        # Find the highest scoring events
        out = []
        for _ in range(self.suggest_amount):
            tmp = 0
            index = 0
            for i in self.event_scores:
                index += 1
                if i.score > tmp:
                    tmp = i.score
            out.append(i.name)
            # self.event_scores[index-1].score = 0
        print(out)

hackerspace = MakeEvent("Hackerspace", "wrk")
at_issue = MakeEvent("At Issue", "crt")
learningco = MakeEvent("Learning Commons", "lc")
events = [learningco, hackerspace, at_issue]

isaac = Student(events)


isaac.select_event(learningco)
isaac.get_tags()
# isaac.suggest(events, 2)
