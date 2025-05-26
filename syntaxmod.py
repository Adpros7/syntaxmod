from types import FunctionType, LambdaType
import time as t
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import *
from datetime import datetime



def loop(times, func: FunctionType or LambdaType, params=None):
    for i in range(times):
        if params is None:
            func()
        elif isinstance(params, list):
            func(*params)
        else:
            func(params)

def wait(seconds: int):
    t.sleep(seconds)

def printstr(str):
    print(str(str))

class PygameInit():
    def __init__(self, width: int, height: int, title: str, backgroundpic: str=None):
        self.screen = display.set_mode((width, height))
        display.set_caption(title)
        if backgroundpic:
            self.background = pygame.transform.scale(pygame.image.load(backgroundpic).convert(), (width, height))

    def run(self):
        running = True
        while running:
            for event in get().get():
                if event.type == QUIT:
                    running = False
                    break
            if not running:
                break

class Stopwatch:
    def __init__(self):
        self.time = 0
        self.start_time = t.time()
        self.paused = False

    def reset(self):
        self.time = 0
        self.start_time = t.time()

    def resume(self):
        while self.paused is False:
            self.time += t.time() - self.start_time
            self.start_time = t.time()
        else: return

    def pause(self):
        self.paused = True

    def __call__(self) -> float:
        return self.time


#test
stopwatch = Stopwatch()
printstr(stepx)
stopwatch.resume()
while True:
    print(stopwatch())
    wait(1)