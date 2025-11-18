# standard modules (ship with Python)
from time import sleep
from os import system
from math import sin, cos, pi
# non-standard modules (need to be installed or created)
from keyboard import is_pressed as key_pressed
from drawKSP_header import keys, cursor_move, connect_to_ksp

system("cls")
print("")

(vessel, telem, controller, gui) = connect_to_ksp() # kRPC stuff

class shared:
    is_quit = False
    printed_lines = 5
    
    timer = 0.0
    dt = 0.05 # poll rate 1/dt = 20 Hz (Don't get too close to ingame fps)

#### DEMO FOR 3D-SPACE UI ELEMENTS
#### get occluded by stock IVA view sadly
origin = (0.0, 3.4, -0.8) # shifting origin from vessel -> cockpit

# create a bunch of lines with 0 length infront of the cockpit
lines = []
for i in range(0,20):
    # (start vector),(end vector),(ref_frame)
    lines.append(gui.add_line(
            (origin[0]+0.5-i/20, origin[1], origin[2]),
            (origin[0]+0.5-i/20, origin[1], origin[2]),
            vessel.reference_frame
        ))
    lines[i].color = (1.0-i/20, 0.5, i/20)
    lines[i].thickness = 0.02

###
###


# main program loop
# --> calculate stuff -> display stuff -> check if key pressed -> sleep
# <--------------------------------------------------------------------
while not shared.is_quit:
    
    # Updating length of lines to follow some periodical curve
    # press keys 9 or 0 to change height
    for i in range(0,20):
        lines[i].end = (origin[0]+0.5-i/20,
                        origin[1],
                        origin[2]-0.25+0.1*sin(2*pi*1*shared.timer+i/5)
                        + 0.1*cos(2*pi*1.44*shared.timer+i/5)
                        + 0.05*sin(2*pi*2.33*shared.timer+i/5)
                        )

    print( " |----------------------------------->  ")
    print(f" | Vessel: {vessel.name}    ")
    print( " |----------------------------------->  ")
    print(f" | Timer:         {shared.timer:10.1f} s   ")
    cursor_move(shared.printed_lines+1, 'up')

    if key_pressed('ESC'):
        cursor_move(shared.printed_lines+2, 'down')
        shared.is_quit = True
    elif key_pressed('9') and keys.delay == 0:
        origin = (origin[0], origin[1], origin[2]-0.1)
        keys.delay += 5
    elif key_pressed('0') and keys.delay == 0:
        origin = (origin[0], origin[1], origin[2]+0.1) 
        keys.delay += 5

    keys.update(keys)
    shared.timer += shared.dt
    sleep(shared.dt)
