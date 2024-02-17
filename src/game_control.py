import os
import psutil
import time
from pathlib import Path

import screen_control_utils as scu

GAME_TASK_NAME = "ck3.exe"
GAME_PATH = Path(r"C:\Users\pawel\Documents\STUDIA\magisterka\ck3_debug.exe.lnk")
GAME_START_TIME = 30 #[s]

def game_has_been_started() -> bool:
    return GAME_TASK_NAME in (p.name() for p in psutil.process_iter())

def start_game() -> None:
    if game_has_been_started():
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
        
        
def open_debug_mode() -> None:
    scu.press("`", direct_x=True)   # open debug panel
    scu.find_and_click("portrait_editor")
    scu.press("`", direct_x=True)   # close debug panel
   
   
def stabilize_heads() -> None:
    scu.find_and_click("head_state")
    scu.press("1", direct_x=True)
    scu.find_and_click("torso_state")
    scu.press("1", direct_x=True)
      
        
def main():
    start_game()
    open_debug_mode()
    stabilize_heads()
    

    
if __name__=="__main__":
    main()
    
    
    
    
    