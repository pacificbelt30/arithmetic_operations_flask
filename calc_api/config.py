"""
アプリケーション設定を管理するモジュール
"""
import os


class Config:
    """基本設定クラス"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-please-change-in-production')
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    """開発環境設定クラス"""
    DEBUG = True


class TestingConfig(Config):
    """テスト環境設定クラス"""
    TESTING = True


class ProductionConfig(Config):
    """本番環境設定クラス"""
    pass


# 環境変数に基づいて設定を選択
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config():
    """環境変数に基づいて設定を取得する"""
    env = os.environ.get('FLASK_ENV', 'default')
    return config_by_name[env]