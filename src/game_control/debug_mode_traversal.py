import game_control.screen_control_utils as scu


def open_debug_mode() -> None:
    scu.press("`", direct_x=True)   # open debug panel
    scu.find_and_click("portrait_editor")
    scu.press("`", direct_x=True)   # close debug panel   
   
   
def stabilize_heads() -> None:
    scu.find_and_click("head_state")
    scu.press("1", direct_x=True)
    scu.find_and_click("torso_state")
    scu.press("1", direct_x=True)

