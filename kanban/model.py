import simplejson
import os

KB_DELETED = 0
KB_TODO = 1
KB_DOING = 2
KB_DONE = 3
KB_PARKED = 4
KB_INIT = -1

class Board:
    def __init__(self, file=r'kbboard.json'):
        self.file = file
        if(os.path.isfile(f)):
            with open(file, mode='r') as f:
                self.kb = simplejson.loads(f.read())
        else:
            with open(file, mode='w+') as f:
                f.write('')
                self.kb = {KB_DELETED: {0: {}},
                           KB_TODO: {0: {}},
                           KB_DOING: {0: {}},
                           KB_DONE: {0: {}},
                           KB_PARKED: {0: {}}}

    def writeBoard(self):
        with open(self.file, mode='w') as f:
            f.write(simplejson.dumps(self.kb))

    def newItem(self, title, notes, state=KB_TODO):
        currentMax = max(self.kb[state])
        itemDict = {'title': title, 'notes': notes}
        self.kb[state][currentMax+1] = itemDict
        self.writeBoard()

    def getState(self, state):
        return self.kb[state]

    def moveItem(self, initState, newState, id):
        tempDict = self.kb[initState].pop(id)
        currentMax