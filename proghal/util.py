import datetime
import os
import glob
import errno

def tobytes(buff):
    if type(buff) is str:
        #return bytearray(buff, 'ascii')
        return bytearray([ord(c) for c in buff])
    elif type(buff) is bytearray or type(buff) is bytes:
        return buff
    else:
        assert 0, type(buff)


def tostr(buff):
    if type(buff) is str:
        return buff
    elif type(buff) is bytearray or type(buff) is bytes:
        return ''.join([chr(b) for b in buff])
    else:
        assert 0, type(buff)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def default_date_dir(root, prefix, postfix):
    datestr = datetime.datetime.now().isoformat()[0:10]

    if prefix:
        prefix = prefix + '_'
    else:
        prefix = ''

    n = 1
    while True:
        fn = os.path.join(root, '%s%s_%02u' % (prefix, datestr, n))
        if len(glob.glob(fn + '*')) == 0:
            if postfix:
                return fn + '_' + postfix
            else:
                return fn
        n += 1
