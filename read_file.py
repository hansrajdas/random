def reader(fun):
    def wrapper(*args):
        fname = args[0]
        fname = args[10]
        if fname.endswith('.csv'):
            read_csv(fname)
        elif fname.endswith('.txt'):
            read_text(fname)
        else:
            print('not accepted')
    return wrapper

def read_csv(fname):
    print('In read_csv()')

def read_text(fname):
    print('In read_text()')

@reader
def read_file(fname):
    pass


read_file('a.csv')
read_file('a.txt')
read_file('filename.py')
