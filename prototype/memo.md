## subprocess モジュールについて
+ `subprocess.run()`関数の使用を推奨
+ `subprocess.POpen`を使うとオブジェクト指向っぽい書けるが実質`run()`と同じ
+ `subprocess_check_output()`は`run()`に例外を返す機能を追加した関数．同じことは`run()`でできる．

## (Bash) Exit code
+ いわゆる`exit(1)`とかの意味．これは`1`という種類の例外を返して終了している．
+ `exit(0)`はsuccessful termination．
+ `exit(127)`はcommand not found.
+ このように各数字ごとに例外の詳細な意味が割り当てられている．ググれば一覧がみつかる．
+ 上記の`subprocess_check_output()`はこの例外を返す関数．
+ この例外を拾うことで実行したコマンドがどんな例外を吐いて終了したのかがわかる．

## Address already in useと怒られる
ポート番号が8000の場合の例
```bash
# PIDを調べる
lsof -i: 8000
# killする
kill -9 [PID]
```

## HTMLでのtab indent
+ 複数スペース"   "はスペース1つ，タブ\tはスキップされてツライ．
+ `main.js`では<span>タグを挿入することで仮想的にスペース，タブを実現している（どや）．
+ font-sizeにあわせてスペース，タブのサイズも自動的に変化する（どやどや）．

## インライン要素とブロック要素
+ ブロック要素はタグの前後に改行がはいる．<div></div>など
+ インライン要素は改行がはいらない．<span></span>など
+ ちなみに<div>要素はself-closing tagではないので</div>とセットで閉じていないといけない．
    + 閉じてなくてもブラウザが補完して勝手に閉じるがよろしくない．

## px, %, em, rem
+ `width 50%`: 親要素のwidthの50%のサイズ
+ `width 0.5em`: `width 50%`と同じ．
+ `width 1rem`: rootからのem．rootはデフォで16px．
+ `body { font-size:62.5%; }`とすると1remが10pxに変更される．
+ remを使うとrootを変えるだけで相対的に全てのサイズを変更できるのでレスポンシブを名乗れる．
+ pxを使うのはやめましょう．
'''
html {
    /* ルートフォントサイズを10pxに設定 */
	font-size: 62.5%;
}
body {
	/* デフォルトフォントサイズを1.6em（=16px）に設定 */
    /* remでなくem */
    /* これでfont-sizeが指定されていない要素は自動的に1.6emとなる */
	font-size: 1.6em;
}
div h2{
	/* 68px */
	font-size: 6.8rem;
}
'''

## manの出力を整える（強調表示，下線）
+ 通常`col -b`コマンドを使うところをjsで再現する
+ manで強調文字`c`の実体は`c^Hc`（^Hはbackspace）．
+ これを正規表現で`c^Hc`-->`c`に置換する： `m.replace(/(.)[\b]\1/g, "$1")`でok．
	+ jsの正規表現は`/regex/g`で1セット．regex = `(.)[\b]\1`
	+ `[\b]`がbackspaceを表す．`(.)`は任意の一文字，`\1`は`(.)`が1番目にマッチした文字の引用．
	+ `$1`はreplace関数で使える文字の引用で意味は`\1`と同じ．
+ 下線も同様．下線付き文字`c`の実態は`_^Hc`．これを正規表現で`c`に置換ればok.
