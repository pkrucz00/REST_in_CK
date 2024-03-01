import os
import psutil
import time
import re
from pathlib import Path

from dotenv import load_dotenv
import game_control.screen_control_utils as scu

load_dotenv()

SETTINGS_FILE_PATH = Path(os.getenv("SETTINGS_FILE"))
GAME_TASK_NAME = os.getenv("GAME_TASK_NAME")
GAME_PATH = Path(os.getenv("GAME_PATH"))
GAME_START_TIME = int(os.getenv("GAME_START_TIME")) #[s]


def game_has_been_started() -> bool:
    return GAME_TASK_NAME in (p.name() for p in psutil.process_iter())

def _change_value(settings_lines, arg_idx, new_value) -> None:
    line_to_change = settings_lines[arg_idx+2]
    changed_line = re.sub(r'".+"', f'"{new_value}"', line_to_change)
    settings_lines[arg_idx+2] = changed_line   # not too elegant but why not
      

def change_game_resolution(resolution: tuple[int, int]) -> None:
    if game_has_been_started():
        raise Exception("Cannot change the resolution when the game has already started")
    
    resolution_str = f"{resolution[0]}x{resolution[1]}"
    with open(SETTINGS_FILE_PATH, "r", encoding="UTF-8") as settings_file:
        settings_lines = settings_file.readlines()
        
    for idx, line in enumerate(settings_lines):
        if "\"display_mode\"" in line:
            print("Changing display mode")
            _change_value(settings_lines, idx, "windowed")
        if "\"windowed_resolution\"" in line:
            print("Changing windowed resolution")
            _change_value(settings_lines, idx, resolution_str)
        if "\"scale\"" in line:  # changing gui scale to 100%
            print("Changing scale")
            _change_value(settings_lines, idx, "1")
    
    with open(SETTINGS_FILE_PATH, "w", encoding="UTF-8") as settings_file:
        for line in settings_lines:
            settings_file.write(line)
            
    
    

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
        
        

    

    
    