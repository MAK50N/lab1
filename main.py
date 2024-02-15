import pygame
import math
import threading
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
PURPLE = (128, 0, 128)
ORANGE = (255, 128, 0)
BROWN = (165,  42,  42)
PINK = (238, 145, 141)

WIDTH, HEIGHT = 1400, 800

PLANETS = [
    {"color": GRAY, "radius": 3, "distance": 50, "speed": 0.03},
    {"color": PURPLE, "radius": 13, "distance": 80, "speed": 0.024},
    {"color": GREEN, "radius": 15, "distance": 120, "speed": 0.018},
    {"color": RED, "radius": 10, "distance": 160, "speed": 0.012},
    {"color": ORANGE, "radius": 25, "distance": 200, "speed": 0.008},
    {"color": BROWN, "radius": 23, "distance": 250, "speed": 0.006},
    {"color": PINK, "radius": 18, "distance": 300, "speed": 0.004},
    {"color": BLUE, "radius": 20, "distance": 350, "speed": 0.002},
]


class Planet(threading.Thread):
    def __init__(self, color, radius, distance, speed):
        super().__init__()
        self.color = color
        self.radius = radius
        self.distance = distance
        self.angle = 0
        self.speed = speed
        self.running = True

    def run(self):
        while self.running:
            self.angle += self.speed
            time.sleep(0.01)

    def stop(self):
        self.running = False


def draw_planet(screen, planet):
    x = WIDTH // 2 + math.cos(planet.angle) * planet.distance
    y = HEIGHT // 2 + math.sin(planet.angle) * planet.distance
    pygame.draw.circle(screen, planet.color, (int(x), int(y)), planet.radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Planets around the Sun")

    sun_radius = 40
    sun_color = (255, 255, 0)
    sun_pos = (WIDTH // 2, HEIGHT // 2)

    planets = []
    for params in PLANETS:
        planet = Planet(params["color"], params["radius"], params["distance"], params["speed"])
        planet.start()
        planets.append(planet)

    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.circle(screen, sun_color, sun_pos, sun_radius)

        for planet in planets:
            draw_planet(screen, planet)

        pygame.display.flip()
        clock.tick(60)

    for planet in planets:
        planet.stop()
        planet.join()

    pygame.quit()


if __name__ == "__main__":
    main()
