from types import FunctionType, LambdaType
import time as t
import os
import pygame
from datetime import datetime
from typing import Any, Callable, List, Optional

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


def loop(times: int, func: Callable, params: Optional[List[Any]] = None) -> None:
    """Execute a function multiple times with optional parameters."""
    for _ in range(times):
        if params is None:
            func()
        elif isinstance(params, list):
            func(*params)
        else:
            func(params)

def wait(seconds: float) -> None:
    """Pause execution for a specified number of seconds."""
    t.sleep(seconds)

def printstr(text: str) -> None:
    """Print text, evaluating it first if it's a valid Python expression."""
    try:
        if any(char in text for char in "=+-*/()[]{}"):
            print(eval(text))
        else:
            print(text)
    except (NameError, SyntaxError, TypeError):
        print(text)

class PygameInit:
    """Initialize a Pygame window with optional background."""
    
    def __init__(self, width: int, height: int, title: str, backgroundpic: Optional[str] = None):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.background = None
        
        if backgroundpic:
            try:
                self.background = pygame.transform.scale(
                    pygame.image.load(backgroundpic).convert(),
                    (width, height)
                )
            except pygame.error as e:
                print(f"Error loading background image: {e}")

    def run(self) -> None:
        """Main game loop."""
        running = True
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            
            if self.background:
                self.screen.blit(self.background, (0, 0))
            
            pygame.display.flip()
            clock.tick(60)

class Stopwatch:
    """A simple stopwatch class with pause/resume functionality."""
    
    def __init__(self) -> None:
        self.time = 0.0
        self.start_time = t.time()
        self.paused = False
        self.pause_time = 0.0
        self.accuracy = 2

    def reset(self) -> None:
        """Reset the stopwatch to zero."""
        self.time = 0.0
        self.start_time = t.time()
        self.paused = False
        self.pause_time = 0.0

    def resume(self) -> None:
        """Resume the stopwatch if paused."""
        if not self.paused:
            return
        self.paused = False
        self.start_time = t.time() - (self.start_time - self.pause_time)

    def pause(self) -> None:
        """Pause the stopwatch."""
        if self.paused:
            return
        self.paused = True
        self.pause_time = t.time()

    def elapsed(self) -> float:
        """Get the elapsed time in seconds."""
        if self.paused:
            return round(self.pause_time - self.start_time, self.accuracy)
        return round(t.time() - self.start_time, self.accuracy)

    def __call__(self) -> float:
        """Return the elapsed time when called as a function."""
        return self.elapsed()

    def __str__(self) -> str:
        """Return a formatted string of the elapsed time."""
        return f"{self.elapsed():.{self.accuracy}f} seconds"

    def __repr__(self) -> str:
        """Return a string representation of the elapsed time."""
        return f"Stopwatch(time={self.elapsed():.{self.accuracy}f})"


if __name__ == "__main__":
    stopwatch = Stopwatch()
    print("Starting stopwatch...")
    stopwatch.resume()
    
    try:
        while True:
            print(f"Time elapsed: {stopwatch()}")
            wait(1)
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        print(f"Final time: {stopwatch()}")