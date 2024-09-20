import pyxel

# Pyxelの初期設定
class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("resources/music.pyxres")
        pyxel.playm(0)
        pyxel.run(self.update, self.draw)

    # ゲームの更新処理
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    # ゲームの描画処理
    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 60, "Hello, Pyxel!", pyxel.frame_count % 16) 

# ゲームを実行
App()