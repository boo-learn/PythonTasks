class Barge:
    def __init__(self, container_quantity: int):
        self.containers = {i: [] for i in range(container_quantity)}
        self.mistakes = []

    def add_barrel(self, container: int, barrel: str) -> None:
        container = self.containers[container]
        if len(container) > 10:
            self.mistakes.append('Container full')
        else:
            container.append(barrel)

    def remove_barrel(self, container: int) -> str:
        container = self.containers[container]
        if not container:
            self.mistakes.append('Container empty')
        else:
            barrel = container.pop()
            return barrel

    def check_empty(self):
        all_containers = self.containers.values()
        for container in all_containers:
            if container:
                self.mistakes.append('Barge is still loaded')

    def check_mistakes(self):
        if self.mistakes:
            print(self.mistakes)
