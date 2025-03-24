# Calculator API

シンプルな四則演算を行うFlask APIサーバです。

## 機能

- 加算 (`/add`)
- 減算 (`/subtract`)
- 乗算 (`/multiply`)
- 除算 (`/divide`)

## セットアップ

このプロジェクトは[Rye](https://rye-up.com/)で管理されています。

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/calc-api.git
cd calc-api

# Ryeで環境をセットアップ
rye sync
```

## 実行方法

```bash
# 開発サーバーの起動
rye run python -m calc_api.app
```

環境変数 `FLASK_ENV` を設定することで、実行環境を切り替えることができます：

```bash
# 開発環境（デフォルト）
FLASK_ENV=development rye run python -m calc_api.app

# 本番環境
FLASK_ENV=production rye run python -m calc_api.app
```

サーバーは `http://localhost:5000` で起動します。

## プロジェクト構造

```
calc-api/
├── calc_api/
│   ├── __init__.py      # パッケージ初期化
│   ├── app.py           # アプリケーションファクトリー
│   ├── config.py        # 設定管理
│   ├── errors.py        # エラーハンドリング
│   ├── operations.py    # 計算処理
│   ├── routes.py        # APIルート定義
│   └── validation.py    # パラメータ検証
├── tests/
│   ├── __init__.py
│   └── test_app.py      # テストスイート
├── pyproject.toml       # プロジェクト設定
└── README.md            # このファイル
```

## API エンドポイント

すべてのエンドポイントは `GET` リクエストを受け付け、`a` と `b` の2つのクエリパラメータを必要とします。

- `/add?a=1&b=2` → `{"result": 3}`
- `/subtract?a=5&b=3` → `{"result": 2}`
- `/multiply?a=4&b=5` → `{"result": 20}`
- `/divide?a=10&b=2` → `{"result": 5}`

## 注意点

- `/divide` エンドポイントでは、`b=0` の場合はエラーが発生します
- 意図的なエラーが1箇所あります（`operations.py`の`multiply`関数内、`b`が負の場合にIndexErrorが発生）

## テスト実行

```bash
rye run pytest
```