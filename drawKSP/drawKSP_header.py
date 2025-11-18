# Launch KSP and start a server using the kRPC ingame icon in flight
# I recommend using a separate Python environment
#
#           >> python -m venv krpc
#           >> krpc/Scripts/activate.ps1 
#           >> pip install krpc
#           >> pip install keyboard
#   (krpc)  >> python drawKSP_app.py
#
# Dependencies: 
# - kRPC (KSP mod: https://krpc.github.io/krpc/) 
# - Powershell 7.x on Windows for compatibility with terminal specific commands 
#
# kRPC Docs: https://krpc.github.io/krpc/
#
# Origin: https://github.com/KsNewSpace/Ks_kRPC_Scripts

def connect_to_ksp():
    # Connects to KSP (kRPC) and returns useful objects
    # to view ingame data and control crafts
    import krpc
    ksp = krpc.connect(name="@KsNewSpace")
    gui = ksp.drawing
    vessel = ksp.space_center.active_vessel
    controller = vessel.control
    telem = vessel.flight(vessel.surface_reference_frame)
    return (vessel, telem, controller, gui)

class keys:
    # Handles key press delays
    delay = 0
    def add_delay(keys):
        keys.delay = 5
    def update(keys):
        if keys.delay > 0:
            keys.delay -= 1

def cursor_move(n, direction):
    #   Oldschool terminal code to control cursor position 
    # and visibility for Powershell 7.x on Windows
    #   Purpose is to rewrite lines instead of clearing screen
    # to prevent flicker
    if direction == 'up':
        print(f"\033[{n}F \033[?25l")
    elif direction == 'down':
        print(f"\033[{n}B \033[?25h")
