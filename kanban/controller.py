from model import Board

KB_DELETED = 0
KB_TODO = 1
KB_DOING = 2
KB_DONE = 3
KB_PARKED = 4
KB_INIT = -1

class KanBan:
    def __init__(self, filename=r'/usr/local/var/kanban_app/kbboard.db'):
        self.kbboard = Board(filename)

    def getToDo(self):
        return self.kbboard.getState(KB_TODO)

    def newItem(self, title):
        self.kbboard.newItem(title, KB_TODO)

    def doItem(self, id):
        self.kbboard.moveItem(KB_DOING, id)

    def doneItem(self, id):
        self.kbboard.moveItem(KB_DONE, id)

    def parkItem(self, id):
        self.kbboard.moveItem(KB_PARKED, id)

    def delItem(self, id):
        self.kbboard.moveItem(KB_DELETED, id)

    def getDoing(self):
        return self.kbboard.getState(KB_DOING)

    def getDone(self):
        return self.kbboard.getState(KB_DONE)

    def getParked(self):
        return self.kbboard.getState(KB_PARKED)

    def unParkItem(self, id):
        self.kbboard.moveItem(KB_DOING, id)

    def unDoItem(self, id):
        self.kbboard.moveItem(KB_TODO, id)
