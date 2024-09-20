import pyxel
import random

# 定数
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
PLAYER_SPEED = 2
BULLET_SPEED = 4
ENEMY_SPEED = 2

class Game:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT - 20
        self.bullets = []
        self.enemies = []
        self.score = 0
        self.game_over = False

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.reset_game()

        if not self.game_over:
            self.update_player()
            self.update_bullets()
            self.update_enemies()
            self.check_collisions()

    def update_player(self):
        # プレイヤーの移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - PLAYER_SPEED, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + PLAYER_SPEED, SCREEN_WIDTH - 8)
        # スペースキーで弾を発射
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bullets.append([self.player_x + 4, self.player_y])

    def update_bullets(self):
        # 弾の移動
        for bullet in self.bullets:
            bullet[1] -= BULLET_SPEED
        # 画面外の弾を削除
        self.bullets = [bullet for bullet in self.bullets if bullet[1] > 0]

    def update_enemies(self):
        # ランダムに敵を生成
        if random.random() < 0.02:
            self.enemies.append([random.randint(0, SCREEN_WIDTH - 8), 0])
        # 敵の移動
        for enemy in self.enemies:
            enemy[1] += ENEMY_SPEED
        # 画面外の敵を削除
        self.enemies = [enemy for enemy in self.enemies if enemy[1] < SCREEN_HEIGHT]

    def check_collisions(self):
        # 弾と敵の衝突判定
        for bullet in self.bullets:
            for enemy in self.enemies:
                if abs(bullet[0] - enemy[0]) < 8 and abs(bullet[1] - enemy[1]) < 8:
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 10
                    break

        # プレイヤーと敵の衝突判定
        for enemy in self.enemies:
            if abs(self.player_x - enemy[0]) < 8 and abs(self.player_y - enemy[1]) < 8:
                self.game_over = True

    def draw(self):
        # 画面をクリア
        pyxel.cls(0)
        if self.game_over:
            # ゲームオーバーの表示
            pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "GAME OVER", pyxel.frame_count % 16)
            pyxel.text(SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 + 10, f"Score: {self.score}", 7)
        else:
            # プレイヤーの描画
            pyxel.rect(self.player_x, self.player_y, 8, 8, 9)
            # 弾の描画
            for bullet in self.bullets:
                pyxel.rect(bullet[0], bullet[1], 2, 4, 10)
            # 敵の描画
            for enemy in self.enemies:
                pyxel.rect(enemy[0], enemy[1], 8, 8, 8)
            # スコアの表示
            pyxel.text(5, 5, f"Score: {self.score}", 7)

# ゲームを開始
Game()
