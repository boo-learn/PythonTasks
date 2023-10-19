class Barge:
    def __init__(self, container_quantity: int):
        self.__containers = {i: [] for i in range(container_quantity)}
        self.__mistakes = []

    def add_barrel(self, container_num: int, barrel_type: str) -> None:
        container = self.__containers[container_num]
        if len(container) > 10:
            self.__mistakes.append('Container full')
        else:
            container.append(barrel_type)

    def remove_barrel(self, container_num: int) -> str:
        container = self.__containers[container_num]
        if not container:
            self.__mistakes.append('Container empty')
        else:
            barrel_type = container.pop()
            return barrel_type

    def check_empty(self):
        all_containers = self.__containers.values()
        for container in all_containers:
            if container:
                self.__mistakes.append('Barge is still loaded')
                break

    def check_mistakes(self):
        if self.__mistakes:
            print(self.__mistakes)
