import pyxel

# Pyxelの初期設定
class App:
    def __init__(self): 
        pyxel.init(160, 120)
        self.x_high = 0
        self.x_low = 160
        pyxel.run(self.update, self.draw) 

    # ゲームの更新処理
    def update(self): 
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.x_high = (self.x_high + 1) % pyxel.width
        self.x_low = (self.x_low - 1) % pyxel.width

    # ゲームの描画処理
    def draw(self): 
        pyxel.cls(0)
        pyxel.text(50, 60, "Hello, Pyxel!", pyxel.frame_count % 16)  
        pyxel.rect(self.x_high, 0, 8, 8, 9)
        pyxel.rect(self.x_low, 112, 8, 8, 6)

# ゲームを実行
App()
