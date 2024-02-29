import game_control.api as game
import json
from time import time
import traceback

import click

"""
As for now this file serves as a test for the whole pipeline.
The only responsibility of this file for now is to:
1. Open the game.
2. Iterate through a mock request.
3. Close the game.

To see the results, check your RESULT (env var) folder, to see if the pipeline has worked correctly.
"""

REQUEST = {"small_forehead": {"head_height": 0},
           "big_forehead": {"head_height": 255},
           "multiple_arguments": {"forehead_height": 0, "eye_distance": 255}}

@click.command()
@click.option("--resolution", type=(int, int), default=(1920, 1080), help="Resolution of the game")
def main(resolution):
    with open("./src/REST_in_CK/static/requests/head_genes.json", "r") as file: 
        request = json.load(file)
    
    print(f"Number of faces to generate: {len(request)}")
    print(resolution)
    try:
        game.prepare()
        
        t1 = time()
        freddie_dna_text = game.load_face("freddie_mercury")
        game.process_face(freddie_dna_text, REQUEST)
        print(f"Time taken: {time() - t1} [s]")
    except Exception:
        print("There was an error: ")
        print(traceback.format_exc())
    finally:
        game.terminate()
        

if __name__=="__main__":
    main()