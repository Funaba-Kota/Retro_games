import pyxel
import random

# ゲームの初期化
class Game:
    def __init__(self):
        pyxel.init(160, 120)
        self.player_x = 80  # プレイヤーのX座標
        self.player_y = 60  # プレイヤーのY座標
        self.target_x = random.randint(0, 150)  # ターゲットのX座標
        self.target_y = random.randint(0, 110)  # ターゲットのY座標
        self.score = 0  # スコア
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # プレイヤーの移動
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < 150:
            self.player_x += 2
        if pyxel.btn(pyxel.KEY_UP) and self.player_y > 0:
            self.player_y -= 2
        if pyxel.btn(pyxel.KEY_DOWN) and self.player_y < 110:
            self.player_y += 2

        # ターゲットを取った場合
        if (self.player_x < self.target_x + 10 and
            self.player_x + 10 > self.target_x and
            self.player_y < self.target_y + 10 and
            self.player_y + 10 > self.target_y):
            self.score += 1
            self.target_x = random.randint(0, 150)
            self.target_y = random.randint(0, 110)

    def draw(self):
        pyxel.cls(0)  # 背景をクリア
        pyxel.rect(self.player_x, self.player_y, 10, 10, 7)  # プレイヤーを描画
        pyxel.rect(self.target_x, self.target_y, 10, 10, 8)  # ターゲットを描画
        pyxel.text(5, 5, f"Score: {self.score}", 7)  # スコアを描画

# ゲームを開始
Game()
