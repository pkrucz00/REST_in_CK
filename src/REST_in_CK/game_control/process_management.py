import os
import psutil
import time
from pathlib import Path

from dotenv import load_dotenv
import game_control.screen_control_utils as scu

load_dotenv()

GAME_TASK_NAME = os.getenv("GAME_TASK_NAME")
GAME_PATH = Path(os.getenv("GAME_PATH"))
GAME_START_TIME = int(os.getenv("GAME_START_TIME")) #[s]

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
        scu.find_button("main_menu_indicator")
        scu.activate_ck3_window()
        scu.move_ck3_to_corner()
    except (RuntimeError, AssertionError) as err:
        print("Game did not start successfully.")
        print(err)
        raise err   


def end_game():
    for p in psutil.process_iter():
        if p.name() == GAME_TASK_NAME:
            p.kill() 
        
        

    

    
    