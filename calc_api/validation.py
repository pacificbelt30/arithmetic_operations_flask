"""
APIリクエストのパラメータ検証を行うモジュール
"""

class ValidationError(Exception)
    """パラメータ検証に関するエラー"""
    pass


def validate_numeric_params(params, required_params=None):
    """
    パラメータが数値として解釈可能かを検証する

    Args:
        params (dict): 検証するパラメータの辞書
        required_params (list, optional): 必須パラメータのリスト

    Returns:
        dict: 検証済みの数値パラメータ

    Raises:
        ValidationError: パラメータがない、または数値として解釈できない場合
    """
    if required_params is None:
        required_params = ["a", "b"]
    
    validated_params = {}
    
    for param in required_params:
        if param not in params or params[param] is None:
            raise ValidationError(f"Missing required parameter: '{param}'")
        
        try:
            validated_params[param] = float(params[param])
        except ValueError:
            raise ValidationError(f"Parameter '{param}' must be a number, got '{params[param]}'")
    
    return validated_params