# RaspberryPiMouse_PS3
Raspberry Pi Mouseに関する実験。Raspberry Pi MouseをPS3コントローラで操作させたり、Google Coral Edge TPU USB アクセラレータを繋いだりしています。

## ソースコードの詳細
- <b>led_ps3.py</b><br>
  前段階としてPS3コントローラで4つのLEDのLチカをさせていきます。
  動作仕様は以下の通りです。
  1. ◯：LED赤、△：LED緑、□：LED黄、×：LED白をそれぞれ点灯させる
  2. 場所に対応する矢印を入力すると消灯させる
  3. STARTボタンを入力するとプログラムが終了する

- PS3_multiLED.py
  前段階として、PS3コントローラで4つのLEDのLチカをさせていきます(完全形)。
  最終的な動作仕様は以下の通りです。
  1. ◯：LED赤、△：LED緑、□：LED黄、×：LED白をそれぞれ点灯させる
  2. 場所に対応する矢印を入力すると消灯させる
  3. STARTボタンを入力するとプログラムが終了する
  4. 起動時に電池の残量を表示させる
  5. PSボタン長押しでコントローラ＋ラズパイをシャットダウン

- RaspiMouse_Control.py
  PS3コントローラを用いてRaspberry Pi Mouseのコントロールを行うプログラム。


## 関連記事
