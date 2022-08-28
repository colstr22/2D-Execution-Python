import math
import csv

with open('input.csv','r') as file:
    code = [line.rstrip().split(',') for line in file]

ptr = [0,0,0] # [X position of cursor, Y position of cursor, Orientation of cursor]
special = {
        'R':math.pi / 2,
        'L':-1 * math.pi / 2,
        'U':math.pi,
        'S':0
        }

def travel(ptr):
    ptr[0] += round(math.cos(ptr[2]))
    ptr[1] += round(math.sin(ptr[2]))
    return ptr
def run(ptr_i, sqr):
    if len(sqr) == 1:
        if sqr == 'S':
            travel(ptr)
        else:
            ptr_i[2] += special[sqr]        
    else:
        exec(sqr, globals())
    return ptr_i
#Runtime
while True:
    ins = code[ptr[1]][ptr[0]]
    if ptr[0] * ptr[1] < 0:
        exit()
    ptr = run(ptr, ins)
    ptr = travel(ptr)
