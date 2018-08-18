class Grid():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = [[None] * width] * height
