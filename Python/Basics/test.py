def sample_decorator(f):
    def deco_wrapper(*args, **kwargs):
        """デコレータのDocstringだよ"""
        print("デコレータだよ")
        return f(*args, **kwargs)
    return deco_wrapper

@sample_decorator
def deco_function():
    """デコってる関数のDocstringだよ"""
    print("これがデコってる関数だ！")


if __name__ == '__main__':
    deco_function()