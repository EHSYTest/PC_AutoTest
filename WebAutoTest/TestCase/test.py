def twice(func):
    print('get in twice')
    def new_func(*args):
        print('twice')
        result = func(*args)
        result = result*2
        print('2倍%s'%str(result))
        return result
    return new_func


def square(func):
    print('get in square')
    def new_func(*args):
        print('square')
        result = func(*args)
        result = result ** 2
        print('平方%s'%str(result))
        return result
    return new_func

@square
@twice
def add(a, b):
    print(a+b)
    return a+b


if __name__ == '__main__':
    add(1, 2)
