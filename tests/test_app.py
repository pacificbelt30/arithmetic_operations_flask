"""
アプリケーションのテストモジュール
"""
import pytest

from calc_api.app import create_app
from calc_api.config import TestingConfig


@pytest.fixture
def app():
    """テスト用アプリケーションのフィクスチャ"""
    app = create_app(TestingConfig)
    return app


@pytest.fixture
def client(app):
    """テスト用クライアントのフィクスチャ"""
    return app.test_client()


def test_index(client):
    """ルートエンドポイントのテスト"""
    response = client.get('/')
    assert response.status_code == 200
    assert 'Calculator API' in response.json['name']


def test_add(client):
    """加算エンドポイントのテスト"""
    response = client.get('/add?a=5&b=3')
    assert response.status_code == 200
    assert response.json['result'] == 8

    # 負の数のテスト
    response = client.get('/add?a=-1&b=-2')
    assert response.status_code == 200
    assert response.json['result'] == -3

    # 無効なパラメータのテスト
    response = client.get('/add?a=abc&b=3')
    assert response.status_code == 400


def test_subtract(client):
    """減算エンドポイントのテスト"""
    response = client.get('/subtract?a=5&b=3')
    assert response.status_code == 200
    assert response.json['result'] == 2

    # 結果が負になるテスト
    response = client.get('/subtract?a=3&b=5')
    assert response.status_code == 200
    assert response.json['result'] == -2


def test_multiply(client):
    """乗算エンドポイントのテスト"""
    response = client.get('/multiply?a=4&b=5')
    assert response.status_code == 200
    assert response.json['result'] == 20

    # ゼロのテスト
    response = client.get('/multiply?a=0&b=5')
    assert response.status_code == 200
    assert response.json['result'] == 0

    # 意図的なエラーのテスト
    response = client.get('/multiply?a=5&b=-2')
    assert response.status_code == 500
    assert 'unexpected error' in response.json['error'].lower()


def test_divide(client):
    """除算エンドポイントのテスト"""
    response = client.get('/divide?a=10&b=2')
    assert response.status_code == 200
    assert response.json['result'] == 5

    # ゼロ除算のテスト
    response = client.get('/divide?a=10&b=0')
    assert response.status_code == 400
    assert 'division by zero' in response.json['error'].lower()


def test_missing_parameters(client):
    """パラメータ不足のテスト"""
    response = client.get('/add?a=5')
    assert response.status_code == 400
    assert 'missing' in response.json['error'].lower()


def test_not_found(client):
    """存在しないエンドポイントのテスト"""
    response = client.get('/not_exist')
    assert response.status_code == 404
    assert 'not found' in response.json['error'].lower()