class Battle:
  def __init__(self, player, enemy):
    self.player = player
    self.enemy = enemy
    self.message = "¡Comienza la batalla!"

  def player_attack(self):
    damage = self.player.attack
    self.enemy.take_damage(damage)
    self.message = (
        f"{self.player.name} ataca a {self.enemy.name} por {damage} de daño."
    )

  def enemy_attack(self):
    damage = self.enemy.generate_attack()
    self.player.take_damage(damage)
    self.message = (
        f"{self.enemy.name} ataca a {self.player.name} por {damage} de daño."
    )

  def is_game_over(self):
    if not self.player.is_alive():
        self.message = f"¡{self.enemy.name} ha ganado!"
        return True
    elif not self.enemy.is_alive():
        self.message = f"¡{self.player.name} ha ganado!"
        return True
    return False
