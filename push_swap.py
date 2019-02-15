#! /usr/bin/env python3

import sys
del sys.argv[0]
#action = [(a) for a in input().split()]
la = sys.argv
la = [int(n) for n in la]
lb = []
actions = ''

def sa():

    global actions
    if len(la) >= 2:
        swap = la[0]
        la[0] = la[1]
        la[1] = swap
        actions = actions + 'sa '
    else:
        pass

def sb():

    global actions
    if len(lb) > 2:
        swap = lb[0]
        lb[0] = lb[1]
        lb[1] = swap
        actions = actions + 'sb '
    else:
        pass

def sc():

    global actions
    sa()
    sb()
    actions = actions + 'sc '

def pa():

    global actions
    if len(lb) >= 1:
        la.insert(0, lb[0])
        del lb[0]
        actions = actions + 'pa '
    else:
        pass

def pb():

    global actions
    if len(la) >= 1:
        lb.insert(0, la[0])
        del la[0]
        actions = actions + 'pb '
    else:
        pass

def ra():

    global actions
    if len(la) >= 2:
        swap = la[0]
        del la[0]
        la.append(swap)
        actions = actions + 'ra '
    else:
        pass


def rb():

    global actions
    if len(lb) >= 2:
        swap = lb[0]
        del lb[0]
        lb.append(swap)
        actions = actions + 'rb '
    else:
        pass

def rr():

    global actions
    ra()
    rb()
    actions = actions + 'rr '

def rra():

    global actions
    if len(la) >= 2:
        lgn = len(la) - 1
        swap = la[lgn]
        del la[lgn]
        la.insert(0, swap)
        actions = actions + 'rra '
    else:
        pass

def rrb():

    global actions
    if len(lb) >= 2:
        lgn = len(lb) - 1
        swap = lb[lgn]
        del lb[lgn]
        lb.insert(0, swap)
        actions = actions + 'rrb '
    else:
        pass

def rrr():

    global actions
    rra()
    rrb()
    actions = actions + 'rrr '

def sort_array():
    for n in la:
        if n == min(la):
            index = la.index(n)
            leng = (len(la) - 1)
            dist = leng - index
            if dist <= index:
                while la.index(n) != 0:
                    rra()
                    dist = dist - 1
            if dist > index:
                while la.index(n) != 0:
                    ra()
                    dist = dist - 1
    pb()

if len(la) > 1 and sorted(la) != la:
    if len(la) == 2 and la != sorted(la):
        sa()
    else :
        while len(la) > 0:
            sort_array()
        while len(lb) != 0:
            pa()
        print(la)
else:
    print(la)
actions = actions.strip()
print("\033[1;34;40m" + actions)
act = len(actions.split())
string = 'actions : '
print("\033[1;31;40m" + string + str(act))
