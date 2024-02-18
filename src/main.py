import game_control.api as game

"""
As for now this file only serves as a test if the whole pipeline can be run on the client. The only responsibility of this file for now is to:
1. Open the game.
2. Iterate through a mock request.
3. Close the game.
"""

REQUEST = {"small_forehead": {"head_height": 0},
           "big_forehead": {"head_height": 255},
           "multiple_arguments": {"forehead_height": 0, "eye_distance": 255}}

def main():
    game.prepare()
    freddie_dna_text = game.load_face("freddie_mercury")
    game.process_face(freddie_dna_text, REQUEST)
    # game.terminate()

if __name__=="__main__":
    main()