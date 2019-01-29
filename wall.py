class wall:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = color(255)
        
    def show(self):
        fill(self.col)
        rect(self.x, self.y, self.w, self.h)
        
    def update(self):
        self.show()
        
        
