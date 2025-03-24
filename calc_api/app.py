"""
Flaskアプリケーションのエントリーポイント
"""
from flask import Flask

from calc_api.config import get_config
from calc_api.routes import calc_bp
from calc_api.errors import register_error_handlers


def create_app(config_class=None):
    """
    Flaskアプリケーションのファクトリー関数

    Args:
        config_class: 設定クラス（指定しない場合は環境変数から取得）

    Returns:
        Flask: 設定済みのFlaskアプリケーション
    """
    app = Flask(__name__)
    
    # 設定の適用
    if config_class is None:
        config_class = get_config()
    app.config.from_object(config_class)
    
    # Blueprintの登録
    app.register_blueprint(calc_bp)
    
    # エラーハンドラの登録
    register_error_handlers(app)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])