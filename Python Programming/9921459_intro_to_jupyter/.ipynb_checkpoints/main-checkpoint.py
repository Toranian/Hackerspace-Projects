{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Flex suggest program\n",
    "This program lets users to add flex events to their profiles, and then have flex events recommended to them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## User Class\n",
    "This class creates a user class, which takes \"tags\" as arguments. These are added to self.tags. When the recommend() fucntion is run, it goes through the Event() class' tags. For every user tag that is in the Event() tag, the score of that event is increased by one. The recommend() function returns a dictionary with the name of the event and the score attributed to it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "class User:\n",
    "\n",
    "    def __init__(self, *args):\n",
    "        self.tags = list(args)\n",
    "\n",
    "    def add_tags(self, *args):\n",
    "        self.tags.append(args)\n",
    "    \n",
    "    def recommend(self, events, display=False):\n",
    "        event_scores = {}\n",
    "        for event in events:\n",
    "            score = 0\n",
    "            for tag in event.tags:\n",
    "                if tag in self.tags:\n",
    "                    score += 1\n",
    "            if display:\n",
    "                event_scores[event.title] = score\n",
    "            else:\n",
    "                event_scores[event] = score\n",
    "\n",
    "        return event_scores\n",
    "    \n",
    "    def add_events(self, events):\n",
    "        for event in events:\n",
    "            for tag in event.tags:\n",
    "                self.tags.append(tag)\n",
    "    \n",
    "    def add_event(self, event):\n",
    "        for tag in event.tags:\n",
    "            self.tags.append(tag)\n",
    "\n",
    "    def display(self):\n",
    "        print(self.tags)\n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Event Class\n",
    "This class just holds the tags of the event."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Event:\n",
    "\n",
    "    def __init__(self, title, description, tags):\n",
    "        self.title = title\n",
    "        self.description = description\n",
    "        self.tags = tags\n",
    "    \n",
    "    def add_events(self, *args):\n",
    "        self.tags.append(args)\n",
    "    \n",
    "    def display(self):\n",
    "        print(self.title.center(50, '_'))\n",
    "        print(self.description)\n",
    "        print(self.tags)\n",
    "    \n",
    "    def __str__(self):\n",
    "        print(self.title)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Code in action\n",
    "Two events are created and then put into a list. This list is then later passed through the student.recommend() function. This function returns a dictionary of key value pairs, where there is the event object and the event score."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['tec', 'crt', 'ct', 'cmn']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'Hackerspace': 4, 'At issue': 2}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Two events are created. The last arguments passed  are the tags.\n",
    "hackerspace = Event(\"Hackerspace\", \"Come get your hack on!\", [\"tec\", \"crt\", \"ct\", \"cmn\"])\n",
    "at_issue = Event(\"At issue\", \"Come learn about stuff\", [\"crt\", \"ct\"])\n",
    "\n",
    "# Put the events into a list\n",
    "events = [hackerspace, at_issue]\n",
    "\n",
    "# Create a user\n",
    "student = User()\n",
    "student.add_event(hackerspace)\n",
    "student.display()\n",
    "student.recommend(events, True)\n",
    "# student.recommend(events) Run this to get the values in OBJECT form.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
