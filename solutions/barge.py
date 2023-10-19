from enum import Enum


class Mistakes(Enum):
    container_empty = 1
    container_full = 2
    barge_not_empty = 3
    wrong_barrel_type = 4


class Barge:
    def __init__(self, container_quantity: int):
        self.__containers = {i: [] for i in range(container_quantity)}
        self.__mistakes = []

    def __get_mistakes(self) -> list[Mistakes]:
        return self.__mistakes

    def add_barrel(self, container_num: int, barrel_type: str) -> None:
        container = self.__containers[container_num]
        if len(container) > 9:
            self.__mistakes.append(Mistakes.container_full)
        else:
            container.append(barrel_type)

    def remove_barrel(self, container_num: int, barrel_type: str) -> None:
        container = self.__containers[container_num]
        if not container:
            self.__mistakes.append(Mistakes.container_empty)
        else:
            removed_barrel_type = container.pop()
            if removed_barrel_type != barrel_type:
                self.__mistakes.append(Mistakes.wrong_barrel_type)

    def check_empty(self):
        all_containers = self.__containers.values()
        for container in all_containers:
            if container:
                self.__mistakes.append(Mistakes.barge_not_empty)
                break

    def check_mistakes(self):
        return bool(self.__mistakes)
