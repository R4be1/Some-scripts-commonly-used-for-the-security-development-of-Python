def RANDOM():
    import random
    _RANDOM="".join([random.choice("1234567890abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(32)])
    return _RANDOM
