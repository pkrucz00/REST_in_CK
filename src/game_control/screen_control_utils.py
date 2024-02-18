import os
import time
from pathlib import Path

import pyautogui as pag
import pydirectinput as pdag

PICS_FOLDER = Path(os.path.dirname(__file__)) / "../static/locate_pics"

def activate_ck3_window() -> None:
    title = "Crusader Kings III"
    ck3_windows = pag.getWindowsWithTitle(title)
    if ck3_windows:
        ck3_win = ck3_windows[0]
        if ck3_win.isActive: return
        
        try:
            ck3_win.activate()
        except:
            ck3_win.minimize()
            ck3_win.maximize()
            
    ck3_win.activate()
    active_window = pag.getActiveWindow()
    
    assert active_window, "No active window. Activation of CK III window failed"
    assert active_window.title == title, f"The {title} is not active"


def find_button(pic_name: str) -> pag.Point:
    confidence = 0.95
    
    pic_path = f"{PICS_FOLDER.as_posix()}/{pic_name}.png"    
    button_placement = pag.locateOnScreen(pic_path, confidence=confidence)
    if not button_placement:
        raise RuntimeError("Button placement not found")
    
    return pag.center(button_placement)


def safe_click(coords: pag.Point) -> None:
    wait_time = 0.00001   #the game is sometimes too slow for an immediate response, this slows clicking a little
    
    pag.moveTo(coords.x, coords.y)
    time.sleep(wait_time)
    pag.click()
    

def find_and_click(pic_name: str) -> None:
    button_center = find_button(pic_name)
    safe_click(button_center)
        

def press(key: pag.KEYBOARD_KEYS, direct_x: bool = False) -> None:
    pdag.press(key) if direct_x else pag.press(key)
    

def screenshot_face(region: tuple[int, int, int, int], output_folder: str) -> None:
    output_path = output_folder / "img.jpg"
    pag.screenshot(output_path, region=region)