from utils.helpers import control_detection
from utils.constants import KEYMAPS
from game.core import Field

def update(*fields : Field, key):
    for field in fields:
        if field.core.is_game_over:
            continue

        field.snake.direction = control_detection(field.snake.direction, KEYMAPS[field.core.player_id], key)
        head = field.snake.body[0].copy()

        if field.snake.direction == "up":
            head["y"] -= 1
        elif field.snake.direction == "down":
            head["y"] += 1
        elif field.snake.direction == "left":
            head["x"] -= 1
        elif field.snake.direction == "right":
            head["x"] += 1

        if field.field[head["y"]][head["x"]] in [1, 3, 4]:
            field.core.is_game_over = True
            continue

        field.snake.body.insert(0, head)

        if field.food["x"] == head["x"] and field.food["y"] == head["y"]:
            field.field[head["y"]][head["x"]] = 1
            field.food = field.create_food()
            field.field[field.food["y"]][field.food["x"]] = 2
            field.core.score += 10
        else:
            tail = field.snake.body.pop()
            field.field[tail["y"]][tail["x"]] = 0
            field.field[head["y"]][head["x"]] = 1

        field.core.is_game_over = False

    return [field.core.is_game_over for field in fields]