#!/usr/bin/env python
import sys
from terminaltables import PorcelainTable
from kanban.controller import KanBan

def getItemStr(item):
    return '%03d (%s) %s' % (item['id'], item['created'], item['title'])

def printBoard(kbBoard):
    todo = kbBoard.getToDo()
    doing = kbBoard.getDoing()
    done = kbBoard.getDone()
    parked = kbBoard.getParked()


    lengthTodo = len(todo)
    lengthDoing = len(doing)
    lengthDone = len(done)
    #lengthParked = len(parked)

    largest = max(lengthTodo, lengthDoing, lengthDone)

    table = [['To Do', 'Doing', 'Done'],]
    print '--Parking-Lot--------------------'
    for item in parked:
        print getItemStr(item)
    print '---------------------------------\n'
    for i, _ in enumerate(range(0, largest)):
        if lengthTodo > i:
            td_it = getItemStr(todo[i])
        else:
            td_it = ''
        if lengthDoing > i:
            dg_it = getItemStr(doing[i])
        else:
            dg_it = ''
        if lengthDone > i:
            dn_it = getItemStr(done[i])
        else:
            dn_it = ''
#        if lengthParked > i:
#            pk_it = getItemStr(parked[i])
#        else:
#            pk_it = ''
        table.append([td_it, dg_it, dn_it])
    print PorcelainTable(table).table


def main():
    if len(sys.argv) < 2:
        print 'Invalid Arguments\nkanban.py [command]'
    else:
        kbBoard = KanBan()
        if sys.argv[1] == 'list':
            printBoard(kbBoard)
        elif sys.argv[1] == 'new':
            title = ''
            for arg in sys.argv[2:]:
                title += '%s ' % arg
            kbBoard.newItem(title.strip())
            print 'Item Added'
        elif sys.argv[1] == 'do':
            id = int(sys.argv[2])
            kbBoard.doItem(id)
            print 'Doing Item %s' % id
        elif sys.argv[1] == 'done':
            id = int(sys.argv[2])
            kbBoard.doneItem(id)
            print 'Completing Item %s' % id
        elif sys.argv[1] == 'park':
            id = int(sys.argv[2])
            kbBoard.parkItem(id)
            print 'Parking Item %s' % id
        elif sys.argv[1] == 'del':
            id = int(sys.argv[2])
            kbBoard.delItem(id)
            print 'Deleting Item %s' % id
        elif sys.argv[1] == 'undo':
            id = int(sys.argv[2])
            kbBoard.unDoItem(id)
            print 'Returning item %s to ToDo' % id
        elif sys.argv[1] == 'unpark':
            id = int(sys.argv[2])
            kbBoard.unParkItem(id)
            print 'Returning item %s to ToDo' % id
        else:
            print 'Current Supported Commands:'
            print 'list, new, do, done, park, del, undo, unpark'
    return

if __name__ == '__main__':
    main()