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


