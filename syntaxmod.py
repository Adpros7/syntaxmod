from types import FunctionType, LambdaType
import time as t
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import *
from datetime import datetime



def loop(times, func: FunctionType or LambdaType, params: list=None):
    for i in range(times):
        if params is None:
            func()
        else:
            func(params)

def wait(seconds: int):
    t.sleep(seconds)

def printstr(str):
    print(str)

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

class Stopwatch:
    def __init__(self):
        self.time = 0
        self.start_time = t.time()

    def reset(self):
        self.time = 0
        self.start_time = t.time()

    def resume(self):
        while True:
            self.time += t.time() - self.start_time
            self.start_time = t.time()

    def pause(self):
        self.start_time = t.time()

    def __call__(self):
        return self.time

#test
if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.resume()
    wait(5)
    stopwatch.pause()
    print(stopwatch())    