"""
エラーハンドリングを行うモジュール
"""
from flask import jsonify


def register_error_handlers(app):
    """
    アプリケーションにエラーハンドラを登録する

    Args:
        app (Flask): Flaskアプリケーションインスタンス
    """

    @app.errorhandler(404)
    def not_found_error(error):
        """404エラーのハンドラ"""
        return jsonify({
            "error": "Not found",
            "message": "The requested URL was not found on the server."
        }), 404

    @app.errorhandler(405)
    def method_not_allowed_error(error):
        """405エラーのハンドラ"""
        return jsonify({
            "error": "Method not allowed",
            "message": "The method is not allowed for the requested URL."
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        """500エラーのハンドラ"""
        return jsonify({
            "error": "Internal server error",
            "message": "The server encountered an internal error."
        }), 500