import pyxel

# Pyxelの初期設定
class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("resources/sound.pyxres")
        pyxel.run(self.update, self.draw)

    # ゲームの更新処理
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):  # スペースキーが押されたらサウンドを再生
            pyxel.play(0, 0)

    # ゲームの描画処理
    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 40, "HAPPY BIRTH DAY!", pyxel.frame_count % 16)
        pyxel.text(55, 50, "(Pless Space)", pyxel.frame_count % 16) 

# ゲームを実行
App()