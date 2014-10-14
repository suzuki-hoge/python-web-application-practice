# Step05

この章では Bootstrap3 を使って、画面デザインを変更してみます。
- 利用者の利便性を高めるデザインを検討する。
- Bootstap3 のドキュメントを調査し、デザイン案を実現する部品を探す。
- 必要なファイルを入手し、ゲストOS内に配備する。
- デザイン案を実装する。

早く終わった人は、より使いやすい画面デザインに取り組んでみましょう。
- 納期をカレンダーから入力する。
- ストーリー / タスクを、画面遷移なしで入力する。

## デザイン案を検討しよう

利用者の様子を観察しよう。

- どんなときにこのアプリを使うのか？
- どうやってこの画面にたどり着くのか？
- 何がしたい？やりたいことはできている？

どうすれば良くなるか「仮説」を立てよう。

## 実現方法を調査しよう

- [Bootstrap](http://getbootstrap.com/)
- 復習: [Bootstrap 3.0 入門](http://dotinstall.com/lessons/basic_twitter_bootstrap_v4)

## Bootstrap3 を配備しよう

- 復習: [#02 開発の準備を整えよう](http://dotinstall.com/lessons/basic_twitter_bootstrap_v4/24702)
- Djangoでの[静的ファイルの公開方法](http://docs.djangoproject.jp/en/latest/howto/static-files.html)に従い、/static/ 配下に配備する。

todo ディレクトリの下に static ディレクトリを作り、その下に入手した css, fonts, js を配備します。
また、正しく設定されたかどうかを確かめるために、Bootstrap の Getting Started で公開されている HTML のテンプレートを index.html として配備します。
結果、todo 以下のディレクトリ構成は以下の通りになります。

```sh
└── todo
    ├── __init__.py
    ├── admin.py
    ├── models.py
    ├── static
    │   ├── css
    │   │   ├── bootstrap-theme.css
    │   │   ├── bootstrap-theme.css.map
    │   │   ├── bootstrap-theme.min.css
    │   │   ├── bootstrap.css
    │   │   ├── bootstrap.css.map
    │   │   └── bootstrap.min.css
    │   ├── fonts
    │   │   ├── glyphicons-halflings-regular.eot
    │   │   ├── glyphicons-halflings-regular.svg
    │   │   ├── glyphicons-halflings-regular.ttf
    │   │   └── glyphicons-halflings-regular.woff
    │   ├── index.html
    │   └── js
    │       ├── bootstrap.js
    │       └── bootstrap.min.js
    ├── tests.py
    ├── views.py
```

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
```

http://localhost:18000/static/index.html にアクセスしてみましょう。
Hello, world! と表示されていること、Dev tools でエラーが表示されていないことを確認しましょう。

## 実装しよう

- 復習: [Bootstrap 3.0 入門](http://dotinstall.com/lessons/basic_twitter_bootstrap_v4)

## 挑戦してみよう

早く終わった人は、より使いやすい画面デザインに取り組んでみましょう。
- 納期をカレンダーから入力する。
- ストーリー / タスクを、画面遷移なしで入力する。