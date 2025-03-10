from game.core import Field
from utils.constants import PLAYER_SKINS, CORNERS
import math

def draw(*fields : Field, columns=2):
    for i in range(0, len(fields), columns):
        display_rows = []
        max_rows = max(field.rows for field in fields[i:i+columns])

        for j in range(-1, max_rows):
            row_parts = []

            for field in fields[i:i+columns]:
                player_id = field.core.player_id

                if j == -1:
                    tab_panel = f"SCORE: {field.core.score} PLAYER: {field.core.player_name}"
                    exp = "  " * (field.columns - len(tab_panel) // 2)
                    line = f"  {tab_panel}{exp}"
                elif j < field.rows:
                    if j == 0:
                        line = CORNERS["top_left"] + "".join(
                            PLAYER_SKINS[player_id][4] for _ in range(field.columns - 2)) + CORNERS[
                                   "top_right"]
                    elif j == field.rows - 1:
                        line = CORNERS["bottom_left"] + "".join(
                            PLAYER_SKINS[player_id][4] for _ in range(field.columns - 2)) + CORNERS[
                                   "bottom_right"]
                    else:
                        line = "".join(PLAYER_SKINS[player_id][cell] for cell in field.field[j])

                else:
                    line = "  " * (field.columns + 1)

                row_parts.append(line)

            display_rows.append("".join(row_parts))

        print("\n".join(display_rows))