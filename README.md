# RaspberryPiMouse_xbox
Raspberry Pi Mouseに関する実験。Raspberry Pi Mouseをxboxコントローラで操作させたり、Google Coral Edge TPU USB アクセラレータを繋いだりしています。

## ソースコードの詳細
- <b>Remocon_for_xbox.py</b>
　xboxコントローラでRaspberry Pi Mouseを操作する
 1. A，B，X，YでLED0 〜 LED3を点灯・消灯
 2. 矢印キーでモータの制御(デジタル入力)
 3. 左スティックで前・後進，LT・RTで左右回転(アナログ入力)
 4. LBキーでブザー
 5. RBキーでプログラム終了

- <b>led_xbox.py</b>
　xboxコントローラで4つのLEDを操作する

## 関連記事
