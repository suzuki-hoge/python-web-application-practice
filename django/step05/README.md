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

- 仮説の例: Story の追加と Task の追加で、別々のアイコンを使うべきだ（なぜなら、利用者が迷ってしまうから）

## 実現方法を調査しよう

- [Bootstrap](http://getbootstrap.com/)
- 復習: [Bootstrap 3.0 入門](http://dotinstall.com/lessons/basic_twitter_bootstrap_v4)

## Bootstrap3 を配備しよう

- 復習: [#02 開発の準備を整えよう](http://dotinstall.com/lessons/basic_twitter_bootstrap_v4/24702)
- Djangoでの[静的ファイルの公開方法](http://docs.djangoproject.jp/en/latest/howto/static-files.html)に従い、/static/ 配下に配備する。

todo ディレクトリの下に static ディレクトリを作り、その下に入手した css, fonts, js を配備します。
また、正しく設定されたかどうかを確かめるために、Bootstrap の Getting Started で公開されている HTML のテンプレートを index.html として配備します。

このとき、index.html 内で href="css/bootstrap.min.css" は href="/static/css/bootstrap.min.css" に、src="js/bootstrap.min.js" は src="/static/js/bootstrap.min.js" に変更することを忘れないでください。
修正後のHTMLのテンプレートは次の通りです。

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

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
    <script src="/static/js/bootstrap.min.js"></script>
  </body>
</html>
```
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

[http://localhost:18000/static/index.html](http://localhost:18000/static/index.html) にアクセスしてみましょう。
Hello, world! と表示されていること、Web ブラウザーの Dev tools でエラーが表示されていないことを確認しましょう。

## 実装しよう

最初に[Django テンプレート言語](http://docs.djangoproject.jp/en/latest/topics/templates.html)のテンプレートの継承について学びます。

template ディレクトリに base.html を追加します。先ほどの HTML テンプレートを流用しています。
{% block title %}...{% endblock %}, {% block body %}...{% endblock %} を追記しています。
また、css, js の URL の先頭に /static/ をつけています。

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}Bootstrap 101 Template{% endblock %}</title>

    <!-- Bootstrap -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    {% block body %}
    <h1>Hello, world!</h1>
    {% endblock %}

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="/static/js/bootstrap.min.js"></script>
  </body>
</html>
```

その上で、template 以下のファイルが、この base.html を継承するよう、修正します。
例えば、template/story/index.html を次のように修正してみましょう。
{% extends "base.html" %}, {% block title %}...{% endblock %}, {% block body %}...{% endblock %}をそれぞれ挿入しています。

```html
{% extends "base.html" %}
{% block title %}Story{% endblock %}
{% block body %}
{% for story in story_list %}
	<dl>
		<dt>
			<form action='/story/delete/{{ story.id }}' method='post'>
				{{ story }}
				{% csrf_token %}
				<a id='story_update_{{ story.id }}' href='/story/update/{{ story.id }}'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/edit.png'></a>
				<input id='story_delete_{{ story.id }}' type='image' height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/trash.png'>
			</form>
		</dt>
		{% for task in story.sorted_tasks %}
			<dd>
				<form action='/task/delete/{{ task.id }}' method='post'>
					{{ task }}
					{% csrf_token %}
					<a id='task_update_{{ task.id }}' href='/task/update/{{ task.id }}'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/edit.png'></a>
					<input id='task_delete_{{ task.id }}' type='image' height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/trash.png'>
				</form>
			</dd>
		{% endfor %}
		<dd>
			<a id='task_create' href='/task/create/{{ story.id }}'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/plus.png'></a>
		</dd>
	</dl>
	<hr>
{% endfor %}

<a id='story_create' href='/story/create'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/plus.png'></a>
{% endblock %}
```

template ディレクトリ以下は次のようになります。
```sh
├── template
│   ├── base.html
│   ├── story
│   │   ├── form.html
│   │   └── index.html
│   └── task
│       └── form.html
```

[http://localhost:18000/story/](http://localhost:18000/story/) を開いて、ページのソースを確認しよう。

準備ができたら、実装してみよう。

- 復習: [#08 Glyphiconsとボタンを使ってみよう](http://dotinstall.com/lessons/basic_twitter_bootstrap_v4/24708)

template/story/index.html の追加アイコンを修正し、「＋ストーリーを追加」「＋タスクを追加」に分けて表示する。
(なお、テンプレートの継承に必要な宣言は先に追加している前提)

修正前：
```html
...
<dl>
...
  <dd>
    <a id='task_create' href='/task/create/{{ story.id }}'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/plus.png'></a>
  </dd>
</dl>
...
<a id='story_create' href='/story/create'><img height='16px' width='16px' src='https://raw.githubusercontent.com/tenshiPure/pyweb/master/django/step04/images/plus.png'></a>
```

修正後：
```html
...
<dl>
...
  <dd>
    <a class="btn btn-info" href="/task/create/{{ story.id }}">
      <span class="glyphicon glyphicon-plus"></span>タスク追加
    </a>
  </dd>
...
<a class="btn btn-primary" href="/story/create">
    <span class="glyphicon glyphicon-plus"></span>ストーリー追加
</a>
```

[http://localhost:18000/story/](http://localhost:18000/story/) を開いて画面を確認しよう。
[画面イメージ](https://raw.githubusercontent.com/takatama/pyweb/master/django/step05/images/btn.png)

## 挑戦してみよう

早く終わった人は、より使いやすい画面デザインに取り組んでみましょう。
- 納期をカレンダーから入力する。
- ストーリー / タスクを、画面遷移なしで入力する。