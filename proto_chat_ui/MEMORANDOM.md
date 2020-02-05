## About npm
Quick start:
```
$ npm install
$ npm run build
```

Run Webpack in watch-mode to continually compile the JavaScript as you work:
```
$ npm run watch
```

Run local http-server:
```
$ npm install http-server -g
$ npm install http-server -l
```

and then, add the below to `package.json`

```
{
  "scripts": {
    "start": "http-server -c-1 -p 8000"
  }
}
```

## Configuration
+ `App.js`に全てのコンポーネントをimportして展開する
    + importされるコンポーネントをchildとよぶ.
    + childはソースコード末尾に`export default COPONENT_NAME`を書く．
    + childがchildを持つことも可能．オブジェクト指向と同様，肥大しないようコンポーネントを入れ子にする．

+ 全ての.jsファイルはwebpackにより`index.pack.js`に統合される
    + `index.pack.js`だけを`index.html`から呼ぶことで高速化する機能
    + create-react-appを使えば，`npm run build`を実行すると内部でwebpackが呼ばれるので良しなにまかせる．

+ create-react-appを使う場合，`.css`は各コンポーネントごとにimportする．
    + `npm run build`を実行すると，整形されたcss, jsがindex.htmlにhrefされるので心配しなくてok．

+ `config.js`はパラメータ設定ファイル
    + パラメータをexportして他のjsでimportして使う，なんて使い方が可能〜！

+ 各コンポーネントは状態（ライフサイクル）をもっており，componentDidMountはイベントハンドラのひとつ．
    + コンポーネントを初期化するときに呼ばれる関数．
    + 初期化処理を書く．

+ <MessageList messages={this.state.messages}/>でApp.jsからMessageListに受け渡して，this.props.messagesで取得．
    + 新規メッセージを受け取るたびに，MessageListは全てのメッセージを描画する．
    + state：private変数．各コンポーネントがもっていて自身で書き換え可能．
        + constructor()のなかで初期化．その後の書き換えはthis.setState()で行う．
    + props：コンポーネント同士でやりとりする変数．親からchildコンポーネントに渡される．