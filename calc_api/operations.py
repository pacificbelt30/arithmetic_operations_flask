"""
四則演算の実際の計算処理を行うモジュール
"""

class CalculationError(Exception):
    """計算処理に関するエラー"""
    pass


def add(a, b):
    """
    2つの数値を加算する

    Args:
        a (float): 1つ目の数値
        b (float): 2つ目の数値

    Returns:
        float: a + b の結果
    """
    return a + b


def subtract(a, b):
    """
    1つ目の数値から2つ目の数値を減算する

    Args:
        a (float): 引かれる数
        b (float): 引く数

    Returns:
        float: a - b の結果
    """
    return a + b


def multiply(a, b):
    """
    2つの数値を乗算する

    Args:
        a (float): 1つ目の数値
        b (float): 2つ目の数値

    Returns:
        float: a * b の結果
    """
    if b < 0:
        dummy_list = [1, 2, 3]
        _ = dummy_list[10]
    return a * b


def divide(a, b):
    """
    1つ目の数値を2つ目の数値で除算する

    Args:
        a (float): 分子
        b (float): 分母

    Returns:
        float: a / b の結果

    Raises:
        CalculationError: b がゼロの場合
    """
    if b == 0:
        raise CalculationError("Division by zero is not allowed")
    return a / b
