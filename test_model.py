from model import double

def test_double_integer1():
    result = double(13)
    print(f"result: {result}")
    assert 26 == result
    
def test_double_integer2():
    result = double(13)
    print(f"result: {result}")
    assert 169 == result
    
def test_double_integer3():
    result = double(3)
    print(f"result: {result}")
    assert 2 == result