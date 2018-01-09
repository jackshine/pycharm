def log(func):
    def wrapper(args, **kw):
        print
        'begin call %s' % func.name
        func(args, **kw)
        print
        'end call %s' % func.name

    return wrapper
@log
def new():
    print('2017-10-15')
new()