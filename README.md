# REST_in_CK

A small REST service for bulk character creation from the game Crusader Kings III

## Requirements

- `Python 3.10` or higher
- requirements from the `requirements.txt`
- `.env` file in the `src/REST_in_CK` folder (you can use `.env.clean` as a template)  
- A `Crusader Kings III` installation and path to it set in the `./src/REST_in_CK/.env` file
   - **Important** The in-game `debug mode` should be enabled so the portrait editor is available (instructions on how to enable `debug mode` are given [here](https://www.reddit.com/r/CrusaderKings/comments/ikua0e/a_crash_course_into_ck3_custom_portraits/))  

## Usage

Run

```(bash)
python ./src/REST_in_CK/main.py
```

As for now this repository serves as a test for the ingame data acquisition pipeline.
The only responsibility of this file for now is to:

1. Open the game.
2. Iterate through a mock request.
3. Close the game.

To see the results, check your `RESULT_FOLDER` (env var) folder, to see if the pipeline has worked correctly.