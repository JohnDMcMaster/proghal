"""
BP Microsystems FOSS driver binding
"""

from proghal import prog

from bpmicro import startup
from bpmicro import devices

class BPMicro(prog.Prog):
    def __init__(self, cfg={}):
        prog.Prog.__init__(self, cfg=cfg)

    def read(self, cfg={}):
        device_str = cfg["device"]

        self.bp = startup.get(verbose=self.verbose)
        self.device = devices.get(self.bp, device_str, verbose=self.verbose)

        # API is designed to be similar
        return self.device.read(cfg)
