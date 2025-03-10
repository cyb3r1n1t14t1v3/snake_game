from random import randint

class Core:
    def __init__(self):
        self.score = 0
        self.player_id = 0
        self.player_name = "Unknown"
        self.is_game_over = False

    def create_player(self, player_id, player_name):
        self.player_id = player_id
        self.player_name = player_name

class Snake:
    def __init__(self, x, y, field):
        self.body = [
            {"x": x, "y": y},
            {"x": x - 1, "y": y},
            {"x": x - 2, "y": y},
        ]
        self.direction = "right"
        self.field = field
        self.is_auto_mode = True

    # def auto_mode(self):
    #     head = self.body[0].copy()
    #
    #     directions = [
    #         {"dir" : "right", "x" : head["x"], "y" : head["y"] + 1},
    #         {"dir" : "left", "x" : head["x"], "y" : head["y"] - 1},
    #         {"dir" : "up", "x" : head["x"], "y" : head["y"] + 1},
    #         {"dir" : "down", "x" : head["x"], "y" : head["y"] - 1},
    #     ]
    #
    #     print(directions)
    #
    #     valid_directions = [
    #         d for d in directions if
    #         self.field.rows > d["x"] >= 0 and
    #         self.field.columns > d["y"] >= 0 and
    #         not any(map(lambda cell: cell["x"] == d["x"] and cell["y"] == d["y"], self.body[1:]))
    #     ]
    #
    #     print(valid_directions)
    #
    #     food_directions = [
    #         d for d in valid_directions if
    #         (d["dir"] == "right" and self.field.food["x"] > head["x"]) or
    #         (d["dir"] == "left" and self.field.food["x"] < head["x"]) or
    #         (d["dir"] == "up" and self.field.food["y"] > head["y"]) or
    #         (d["dir"] == "down" and self.field.food["y"] < head["y"])
    #     ]
    #
    #     print(food_directions)
    #
    #     if len(food_directions) > 0:
    #         self.direction = food_directions[0]["dir"]
    #     elif len(valid_directions) > 0:
    #         self.direction = valid_directions[0]["dir"]

class Field:
    def __init__(self, rows, columns):
        self.core = Core()
        self.snake = Snake(round(columns / 2), round(rows / 2), self)
        self.rows = rows
        self.columns = columns
        self.field = list()
        self.food = None

    def create_food(self):
        food = {
            "x": randint(0, self.columns - 1),
            "y": randint(0, self.rows - 1)
        }

        if self.field[food["y"]][food["x"]] in [1, 3, 4]:
            return self.create_food()

        return food

    def generate(self):
        for row in range(self.rows):
            self.field.append(list())
            for column in range(self.columns):
                if column == 0 or column == self.columns - 1:
                    self.field[row].append(3)
                elif row == 0 or row == self.rows - 1:
                    self.field[row].append(4)
                else:
                    self.field[row].append(0)

        for cell in self.snake.body:
            self.field[cell["y"]][cell["x"]] = 1

        self.food = self.create_food()
        self.field[self.food["y"]][self.food["x"]] = 2


