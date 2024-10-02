import pygame
from config import *
from characters import Hero, Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("RPG Game")
        self.clock = pygame.time.Clock()

        # Crear personajes
        self.hero = Hero("Knight", 100, 15, 5, WIDTH // 2, HEIGHT // 2)
        self.enemy = Enemy("Goblin", 50, 10)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        # Dibujar los personajes (por ejemplo, rectángulos como marcador de vida)
        pygame.draw.rect(self.screen, HERO_COLOR, pygame.Rect(self.hero.x, self.hero.y, 50, 50))
        pygame.draw.rect(self.screen, ENEMY_COLOR, pygame.Rect(50, 100, self.enemy.hp * 2, 20))

        font =  pygame.font.Font(None, 36)
        hero_hp_text = font.render(f"Hero HP: {self.hero.hp}", True, (255, 255, 255))
        enemy_hp_text = font.render(f"Enemy HP: {self.enemy.hp}", True, (255, 255, 255))
        self.screen.blit(hero_hp_text, (50, 20))
        self.screen.blit(enemy_hp_text, (300,  20))
    
    def handle_enemy_attack(self):
        self.enemy.attack_hero(self.hero)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1

        if keys[pygame.K_SPACE]:
            self.hero.attack_enemy(self.enemy)
        
        self.hero.move(dx, dy)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Actualizar lógica del juego aquí (por ejemplo, ataques)
            self.handle_input()

            self.handle_enemy_attack()

            self.draw()

            pygame.display.flip()
            self.clock.tick(FPS)

            #Check for game over
            if not self.hero.is_alive():
                print("Game Over! The  hero has been defeated")
                running = False
            if not self.enemy.is_alive():
                print("Victory!!! The enemy has been defeated")
                running = False

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()