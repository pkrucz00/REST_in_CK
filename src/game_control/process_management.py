import os
import psutil
import time
from pathlib import Path

import game_control.screen_control_utils as scu

GAME_TASK_NAME = "ck3.exe"
GAME_PATH = Path(r"C:\Users\pawel\Documents\STUDIA\magisterka\ck3_debug.exe.lnk")
GAME_START_TIME = 30 #[s]

def game_has_been_started() -> bool:
    return GAME_TASK_NAME in (p.name() for p in psutil.process_iter())

def start_game() -> None:
    if game_has_been_started():
        scu.activate_ck3_window()
        print("Game has already been started. Aborting another game start.")
        return
    
    os.startfile(GAME_PATH)
    time.sleep(GAME_START_TIME)
    try:
        scu.find_button("main_logo")
        scu.activate_ck3_window()
    except (RuntimeError, AssertionError) as err:
        print("Game did not start successfully.")
        print(err)
        raise err   


def end_game():
    for p in psutil.process_iter():
        if p.name() == GAME_TASK_NAME:
            p.kill() 
        
        

    

    
    