class Prog(object):
    def __init__(self, cfg={}):
        self.verbose = cfg.get("verbose", False)

    def desc(self):
        return 'Unspecified'

    # Primary focus for now
    def read(self, cfg={}):
        raise NotImplemented()

    def program(self, devfg, opts={}):
        raise NotImplemented()

    def erase(self, devfg, opts={}):
        raise NotImplemented()

    def write(self, devfg, opts={}):
        raise NotImplemented()

    def continuity(self, devfg, opts={}):
        raise NotImplemented()
