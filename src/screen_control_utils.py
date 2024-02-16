import pyautogui as pag
import pydirectinput as pdag


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
    button_placement = pag.locateOnScreen(pic_name, confidence=confidence)
    if not button_placement:
        raise RuntimeError("Button placement not found")
    
    return pag.center(button_placement)


# def find_and_click()

def press(key: pag.KEYBOARD_KEYS, direct_x: bool = False) -> None:
    pdag.press(key) if direct_x else pag.press(key)