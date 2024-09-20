# Pythonでレトロゲーム作成

## 概要
Pyxel (ピクセル)というライブラリを使ってレトロゲームを作成  
参考：https://github.com/kitao/pyxel/blob/main/docs/README.ja.md


## 環境構築
### ＜環境＞    
- Python 3.12.5
- Pyxel ライブラリ
- VSCode （今回はVSCodeを使って開発を行った）  
<br>  

### ＜構築手順＞

1. Pythonをインストール  
     - 公式サイト https://www.python.org/downloads/release/python-3126/ でダウンロード  
     <br>  
     - インストール後に以下のコマンドでインストールされていることを確認
     ```bash
       python --version
     ```  
<br>  

2. pyxelをインストール
     - インストール後に以下のコマンドでpyxelをインストール
     ```bash
     pip install -U pyxel
     ```  
<br>  

3. 動作確認
     - 以下のコマンドを実行してPyxelが正しくインストールされていることを確認  
     ```bash
     pip show pyxel
     ```
<br>  

## 基本的な開発手順

### ＜開発手順＞

1. 新しいPythonファイルを作成 (例:`test.py`という名前で作成)  
     - テキストを`test.py`という名前で保存すればOK  
<br>  

2. 以下のサンプルコードを`test.py`に記述  
    ``` python
    import pyxel

    # Pyxelの初期設定
    class App:
        def __init__(self):
            pyxel.init(160, 120)
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
    ```  
<br>  

3. 以下のコマンドを実行してゲームを起動  
    ```bash
    python test.py
    ```  
<br>  

### ＜サンプルコードの解説＞

1. Pyxelライブラリをインポートインポート  
    ```python
    import pyxel
    ```  
<br>  

2. クラスの定義

    ```python
    class App:
        def __init__(self):
            pyxel.init(160, 120)
            pyxel.run(self.update, self.draw)
    ```
     - `App`というクラスを定義 
     - `__init__` メソッド : クラスのインスタンスが生成される際に呼び出される初期化メソッド  
     - `pyxel.init(160, 120):` : 画面のサイズを160x120ピクセルに設定  
     - `pyxel.run(self.update, self.draw):`: ゲームのメインループを開始  
        `update`メソッドと`draw`メソッドをそれぞれゲームの更新処理と描画処理として指定
<br>  

3. 更新処理の定義
    ```python
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    ```  
     - `update`メソッド：毎フレーム呼び出され、ゲームの状態を更新するための処理を行う
     - `pyxel.btnp(pyxel.KEY_Q):` : キーが押された瞬間を検出（Qキーを設定）
     - `pyxel.quit():` : このメソッドが呼ばれると、Pyxelのウィンドウが閉じられゲームが終了する。  
<br>  

4. 描画処理の定義
    ```python
    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 60, "Hello, Pyxel!", pyxel.frame_count % 16)
    ```
     - `draw`メソッド：毎フレーム呼び出され、画面を描画するための処理を行う
     - `pyxel.cls(0):` : 画面をクリア　引数 0 は色（黒）を指定
     - `pyxel.text(50, 60, "Hello, Pyxel!", pyxel.frame_count % 16):` : 画面の (50, 60) の位置に "Hello, Pyxel!" というテキストを描画  
        `pyxel.frame_count % 16`の引数はテキストの色を決定  
        `frame_count`はフレーム数を表し、16で割った余りを取ることで、0から15までの色を周期的に変化している  
        ※Pyxelでは16色のカラーパレットが用意されている
<br>  

5. ゲームの実行
    ```python
    App()
    ```
    - `App`クラスのインスタンスを生成し、ゲームを実行する  
        初期化が行われ、ゲームループが開始される  
<br>  

## リソースの作成　　
ゲームを構成するために必要な各種要素やデータを別途作成することで  
キャラクターや音楽をゲームにつけることができる  
Pyxelエディタを使用し、作成することができる

### ＜Pyxelで作成できる主要なリソース＞

1. スプライト
    - キャラクターやオブジェクトの2D画像  
        アニメーションフレームを含むことができ、複数の状態を持たせることができる

2. タイル
    - ゲームの背景や地形を構成するための小さな画像ブロック  
        タイルを使用することで、マップを効率的に作成できる

3. サウンド
    - ゲーム内で使用する短い音や効果音  
        ジャンプ音やアイテム取得音などが作成できる
    
4. 音楽
    - ゲーム内のバックグラウンド音楽  
　  トラックを作成し、ゲームの音楽を作成できる

### ＜リソースの作成・実装方法＞

1. 以下のコマンドを実行してPyxelエディタを起動  
    ```bash
    pyxel edit my_game.pyxres
    ```  
    エディタ内で作成するリソースを選択できる
    作成後、保存したらリソースのファイルが作成される
<br>  

2. リソースは`pyxel.load()`で読み込みができる
<br>  

3. スプライトは`pyxel.blt()`での関数を使って使用できる  

    以下、サンプル
    ```python
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
    ```  
<br>  

4. タイルは`pyxel.bltm()`の関数を使って使用できる  

    以下、サンプル
    ```python
    import pyxel

    # Pyxelの初期設定
    class App:
        def __init__(self):
            pyxel.init(160, 120)
            pyxel.load("resources/Tile.pyxres")
            pyxel.run(self.update, self.draw)

        # ゲームの更新処理
        def update(self):
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

        # ゲームの描画処理
        def draw(self):
            pyxel.cls(0)
            # タイルマップの描画 (x, y, tilemap_id, u, v, w, h)
            pyxel.bltm(0, 0, 0, 0, 0, 160, 120)
            pyxel.text(50, 60, "Hello, Pyxel!", pyxel.frame_count % 16) 

    # ゲームを実行
    App()
    ```  
<br>  

5. サウンドは`pyxel.play()`の関数を使って使用できる  

    以下、サンプル
    ```python
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
    ```　　
 <br>  

6. 音楽は`pyxel.playm()`の関数を使って使用できる  

    以下、サンプル
    ```python
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
    ```　　