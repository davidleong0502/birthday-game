from typing import Dict, List
from models import Scene, Choice


class Player:
    def __init__(self):
        self.inv: Dict[str, int] = {}

    def add_items(self, items: Dict[str, int] | None):
        if not items:
            return
        for k, v in items.items():
            self.inv[k] = self.inv.get(k, 0) + v

    def has_requirements(self, req: Dict[str, int] | None) -> bool:
        if not req:
            return True
        for k, v in req.items():
            if self.inv.get(k, 0) < v:
                return False
        return True


class Game:
    def __init__(self, scenes: Dict[str, Scene], start_id: str):
        self.scenes = scenes
        self.cur_id = start_id
        self.history: List[str] = []

    def cur_scene(self) -> Scene:
        return self.scenes[self.cur_id]

    def move(self, player: Player, choice: Choice) -> str:
        if not player.has_requirements(choice.requires):
            return "Not enough Bubba points yet — explore another path first! ✨"

        self.history.append(self.cur_id)
        player.add_items(choice.gives)
        self.cur_id = choice.next_id

        return choice.message or ""

    def can_go_back(self) -> bool:
        return len(self.history) > 0

    def go_back(self):
        if self.history:
            self.cur_id = self.history.pop()