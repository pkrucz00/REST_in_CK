import os
import time
from pathlib import Path

import screen_control_utils as scu

GAME_PATH = Path(r"C:\Users\pawel\Documents\STUDIA\magisterka\ck3_debug.exe.lnk")
GAME_START_TIME = 60 #[s]

def start_game() -> bool:
    os.startfile(GAME_PATH)
    time.sleep(GAME_START_TIME)
    
    try:
        scu.find_button("src/static/locate_pics/main_logo.png")
        scu.activate_ck3_window()
    except (RuntimeError, AssertionError) as err:
        print("Game did not start successfully.")
        print(err)
        raise err   
        
def prepare_debug_mode() -> None:
    scu.press("`", direct_x=True)
    
        
def main():
    start_game()
    prepare_debug_mode()
    

    
if __name__=="__main__":
    main()
    
    
    
    
    