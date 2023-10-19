class Barge:
    def __init__(self, container_quantity: int):
        self.__containers = {i: [] for i in range(container_quantity)}
        self.__mistakes = []

    def add_barrel(self, container: int, barrel: str) -> None:
        container = self.__containers[container]
        if len(container) > 10:
            self.__mistakes.append('Container full')
        else:
            container.append(barrel)

    def remove_barrel(self, container: int) -> str:
        container = self.__containers[container]
        if not container:
            self.__mistakes.append('Container empty')
        else:
            barrel = container.pop()
            return barrel

    def check_empty(self):
        all_containers = self.__containers.values()
        for container in all_containers:
            if container:
                self.__mistakes.append('Barge is still loaded')

    def check_mistakes(self):
        if self.__mistakes:
            print(self.__mistakes)
