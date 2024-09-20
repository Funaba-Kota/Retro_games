import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Mouse Follower Sprite")
        pyxel.load("resources/enemy.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        # マウスカーソル位置にスプライトを描画
        pyxel.blt(pyxel.mouse_x - 16, pyxel.mouse_y - 16, 0, 0, 0, 32, 32, 0)

# ゲームを開始
App()