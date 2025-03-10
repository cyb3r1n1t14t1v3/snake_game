import os
import msvcrt

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def key_pressed():
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8').lower()

        return key

def control_detection(current_direction, key_map, key):
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    new_direction = current_direction

    if key and (key in key_map and current_direction != opposites[key_map[key]]):
        new_direction = key_map[key]

    return new_direction