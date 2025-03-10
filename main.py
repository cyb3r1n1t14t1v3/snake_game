from utils.helpers import clear, key_pressed
from utils.constants import DEFAULT_ROWS, DEFAULT_COLUMNS, SPEED
from game.core import Field
from game.display import draw
from game.logic import update
import time

fields = [Field(DEFAULT_ROWS, DEFAULT_COLUMNS) for i in range(2)]

for field in fields:
    field.generate()

while True:
    clear()

    draw(*fields, columns=2)
    if all(update(*fields, key=key_pressed())): break

    time.sleep(SPEED / 10)

winner_field = max(fields, key=lambda f: f.core.score)

print(f"""
Game over!
Winner: {winner_field.core.player_name}
Score: {winner_field.core.score}
""")