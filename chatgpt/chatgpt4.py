import pygame
import threading
import sys


pygame.init()
font = pygame.font.Font(None, 36)
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer Application")
clock = pygame.time.Clock()


# Timer class that runs in a separate thread
class Timer(threading.Thread):
    def __init__(self, name, length, position):
        super().__init__()
        self.name = name
        self.seconds = length
        self.paused = False
        self.lock = threading.Lock()
        self.running = True 
        self.text = font.render(f"Timer 1: {self.seconds}", True, (0, 0, 0))
        self.pos = position

    def run(self):
        while self.running == True:
            with self.lock:
                if not self.paused:
                    self.seconds -= 1
                if self.seconds <= 0:
                    try:
                        self.paused = True
                        #return
                    except:
                        print(f"error message in {self.name}")
            self.text = font.render(f"Timer 1: {self.seconds}", True, (0, 0, 0))
            pygame.time.wait(1000)  # Wait for 1 second

    def toggle(self):
        with self.lock:
            if self.paused == True:
                self.paused = False
            else:
                self.paused = True

    def terminate(self):
        with self.lock:
            self.running = False



class App():
    def __init__(self):
        self.timers = []

    def end_threads(self):
        for thread in self.timers:
            thread.terminate()

    def start_threads(self):
        for thread in self.timers:
            thread.start()

    def create_thread(self):
        pass

    def update(self):
        for thread in self.timers:
            screen.blit(thread.text, (thread.pos[0], thread.pos[1]))



# creating app
app = App()

# Create the timers
timer1 = Timer("Timer 1", int(input("timer 1: ")), (50,50))
app.timers.append(timer1)
timer2 = Timer("Timer 2", int(input("timer 2: ")), (250,50))
app.timers.append(timer2)
app.start_threads()


def END_PROGRAM():
    app.end_threads()
    pygame.quit()
    sys.exit()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            END_PROGRAM()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                pos = pygame.mouse.get_pos()
                if pos[0] < WIDTH / 2:  # Clicked on Timer 1
                    timer1.toggle()
                else:  # Clicked on Timer 2
                    timer2.toggle()

    screen.fill((255, 255, 255))  # Clear the screen

    # Display the timers
    
    app.update()

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Clean up
