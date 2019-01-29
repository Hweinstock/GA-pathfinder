from ball import ball

def listSum(l):
    if l == []:
        return 0
    return l[0] + sum(l[1:])

def randomColor():
    return (random(0, 255), random(0, 255), random(0, 255))

class brain:
    
    def __init__(self, genSize, walls = []):
        self.power = 10
        self.maxMoves = 100
        self.gen = 1
        self.genSize = genSize
        self.balls = [ball(self.randomMoves(), randomColor(), self.maxMoves) for x in range(self.genSize)]
        self.cutOff = 0.05
        self.mutationRate = 0.05
        self.delta = 0.5
        self.best = max([x.fitness for x in self.balls])
        self.average = self.averageFitness()
        self.screenHeight = 0
        self.screenWidth = 0
        self.walls = walls
    
    def randomMoves(self):
        return [[random(-1*self.power, self.power), random(-1*self.power, self.power)] for x in range(self.maxMoves)]
    
    def averageFitness(self):
        fSum = 0
        for b in self.balls:
            fSum += b.fitness
        
        return fSum/len(self.balls)
        
    def update(self):
        if self.checkDead():
            self.best = max([x.fitness for x in self.balls])
            self.average = self.averageFitness()
            self.gen+=1
            self.sortFitness()
            self.balls = self.birth(self.balls[:int(self.cutOff*self.genSize)])
            self.update()
        else:
            for b in self.balls:
                b.update(self.walls)
    
    def checkDead(self):
        for b in self.balls:
            if b.dead == False:
                return False
        else:
            return True
    
    def mutate(self, m):
        s = 1
        if random(1) > 0.5:
            s = -1
        s2 = 1
        if random(1) > 0.5:
            s2 = -1
        return [m[0] + s*(self.power - abs(m[0])*random(self.delta)), m[1] + s2*(self.power - abs(m[1])*random(self.delta))]
        #return [(m[0]/self.power)*random(self.delta), (m[1]/self.power)*random(self.delta)]
            
    def breed(self, a, b):

        babyColor = (((a.col[0]+b.col[0])/2)+random(-1*self.delta, self.delta), ((a.col[1]+b.col[1])/2)+random(-1*self.delta, self.delta), ((a.col[2]+b.col[2])/2)+random(-1*self.delta, self.delta))
        
        babyMoves = []
        for i in range(len(a.moves)):
            move = []
            if random(1) > 0.5 :
                move = a.moves[i]
            else:
                move = b.moves[i]
            if random(1) < self.mutationRate:
                move = self.mutate(move)
            
            babyMoves.append(move)
        
        return ball(babyMoves, babyColor, self.maxMoves)
    
    def selectParent(self, parents):
        s = 0
        r = random(listSum([a.fitness for a in parents]))
        for i in range(len(parents)):
            s+=parents[i].fitness
            if s > r:
                return parents[i]
    
    def birth(self, alphas):
        
        newGen = []
        for i in range(int(self.genSize*(1-self.cutOff))):
            randomAlpha1 = self.selectParent(alphas)
            randomAlpha2 = self.selectParent([a for a in alphas if a != randomAlpha1])
            newGen.append(self.breed(randomAlpha1, randomAlpha2))
            
        for b in alphas:
            b.reset()
        
        return alphas + newGen
        
    def sortFitness(self):
        self.balls.sort(key=lambda x: x.fitness, reverse = True)
        
            
    
        
    
