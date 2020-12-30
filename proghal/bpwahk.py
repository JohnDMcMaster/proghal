"""
BPWin AutoHotKey binding
"""

import subprocess
import os

from proghal import prog
from bpwahk import BPWAHK

class BPWAHK(prog.Prog):
    def __init__(self, cfg={}):
        prog.Prog.__init__(self, cfg=cfg)
        self.bp = BPWAHK(host=cfg.get("host"), port=cfg.get("port"))

    def read(self, cfg={}):
        return {"code": self.bp.read_bin()}
