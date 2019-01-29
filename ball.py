screen_w = 600
screen_h = 600
goal = [600, 600]
start = [screen_w/2, 50]
def randomColor():
    return (random(0, 255), random(0, 255), random(0, 255))

def distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

class ball:
    def __init__(self, moves, col, maxMoves):
        self.col = col
        self.x = screen_w/2
        self.y = 50
        self.moves = moves
        self.w = 10
        self.h = 10
        self.fitness = 0
        self.dead = False
        self.moveNum = 0
        self.maxMoves = maxMoves
        self.earlyDeath = 1
        self.stillMax = 10
        self.stillDistance = 25
        self.oldPos = []
        self.stillPunishment = 10**-2
    
    def reset(self):
        self.x = screen_w/2
        self.y = 50
        self.dead = False
        self.moveNum = 0
        self.earlyDeath = 1
    
    def intersect(self, x, y, w, h):
        if self.x > x and self.x < (x + w):
            if self.y > y and self.y < (y + h):
                return True
            
    def move(self):
        self.x += self.moves[self.moveNum-1][0]
        self.y += self.moves[self.moveNum-1][1]
        
    def show(self):
        fill(color(self.col[0], self.col[1],self.col[2]))
        ellipse(self.x, self.y, self.w, self.h)
    
    def update(self, walls):
        self.moveNum+=1
        if not self.dead:
            self.show()
            self.move()
            if self.checkDead(walls) or self.moveNum >= self.maxMoves:
                self.kill()
    
    def checkDead(self, walls):
        if self.x >= screen_w or self.x <= 0 or self.y >= screen_h or self.y <= 0:
            self.earlyDeath = 0.01
            return True
        for w in walls:
            if self.intersect(w.x, w.y, w.w, w.h):
                self.earlyDeath = 0.01
                return True
        else:
            return False
        
    def kill(self):
        self.dead = True
        self.fitness += self.updateFitness()
        
    def updateFitness(self):
        s = [screen_w/2, 50]
        toGoal = distance(goal[0], goal[1], self.x, self.y)
        traveled = distance(s[0], s[1], self.x, self.y)  
        
        return (self.earlyDeath*(traveled)**0.25/(toGoal**4))*10**5
    
        
        
        
        
