import pygame
from config import *
from characters import Player, Enemy
from battle import Battle

class Game:
  def __init__(self):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego de Rol Simple")


    # Cargar imágenes (reemplaza con tus propias imágenes)

    player_img = pygame.image.load("assets/player.png")
    player_img = pygame.transform.scale(player_img, PLAYER_SIZE)
    enemy_img = pygame.image.load("assets/enemy.png")
    enemy_img = pygame.transform.scale(enemy_img, ENEMY_SIZE)


    self.background_img = pygame.image.load("assets/background.jpg")
    self.background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

    # Crear jugadores
    self.player = Player("Hero", 100, 20, player_img)
    self.enemy = Enemy("Enemy", 80, 15, enemy_img)

    self.battle = Battle(self.player, self.enemy)

  def draw(self):
    self.screen.fill(WHITE)
    #Dibujar fondo
    self.screen.blit(self.background_img, (0, 0))
    
    # Dibujar jugadores
    player_pos = (100, HEIGHT // 2 - PLAYER_SIZE[1]//2)
    enemy_pos = (WIDTH - 100 - ENEMY_SIZE[0], HEIGHT // 2 - ENEMY_SIZE[1] // 2)
    self.screen.blit(self.player.image, player_pos)
    self.screen.blit(self.enemy.image, enemy_pos)
    
    # Dibujar barras de vida
    pygame.draw.rect(self.screen, (255, 0, 0), (100, 250, player.hp, 20))
    pygame.draw.rect(self.screen, (255, 0, 0), (600, 250, enemy.hp, 20))
    
    # Dibujar nombres y HP
    font = pygame.font.Font(None, 36)
    player_text = font.render(f"{self.player.name}: {self.player.hp} HP", True, WHITE)
    enemy_text = font.render(f"{self.enemy.name}: {self.enemy.hp} HP", True, WHITE)
    self.screen.blit(player_text, (100, 200))
    self.screen.blit(enemy_text, (600, 200))
    
    # Dibujar mensajes de batalla
    message = font.render(self.battle.message, True, WHITE)
    self.screen.blit(message, (WIDTH // 2 - message.get_width() // 2, 100))

    pygame.display.flip()


  def run(self):
    running = True
    player_turn = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_turn:
                    self.battle.player_attack()
                    player_turn = False
        
        if not player_turn:
            self.battle.enemy_attack()
            player_turn = True
        
        self.draw()
        
        if self.battle.is_game_over():
            running = False

if __name__ == "__main__":
  game = Game()
  game.run()