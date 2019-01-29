from brain import brain
from wall import wall
screen_w = 600
screen_h = 600
walls = range(4)
walls[0] = wall(0, 200, 300, 50)
walls[1] = wall(350, 200, 300, 50)
walls[2] = wall(0, 400, 150, 50)
walls[3] = wall(200, 400, 300, 50)
trainer = brain(1000, walls)

def setup():
    size(screen_w, screen_h)
    background(0)
    frameRate(500)
    
def draw():
    background(0)
    trainer.update()
    for i in walls:
        i.update()
    fill(255)
    text("Generation: "+str(trainer.gen), 10, 20)
    text("Best: "+str(trainer.best), 10, 70)
    text("Average: "+str(trainer.average), 10, 120)
    text("Mutation Rate: "+str(trainer.mutationRate), 10, 170)
    text("Mutation Delta: "+str(trainer.delta), 10, 220)
    text("Cut Off: "+str(trainer.cutOff), 10, 270)
    text("Gen Size: "+str(trainer.genSize), 10, 320)



    
