class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = self.create_2d_grid(self.height, self.width)

    def create_2d_grid(self, height, width) -> list[list[str]]:
        grid = []
        for i in range(height):
            grid.append([])
            for j in range(width):
                grid[i].append(None)
        return grid

