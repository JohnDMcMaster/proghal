"""
BPWin AutoHotKey binding
"""

import subprocess
import os

from proghal import prog
from bpwahk import BPWAHK as BPWAHK_

class BPWAHK(prog.Prog):
    def __init__(self, cfg={}):
        prog.Prog.__init__(self, cfg=cfg)
        self.bp = BPWAHK_(host=cfg.get("bpwahk_host"), port=cfg.get("bpwahk_port"))

    def read(self, cfg={}):
        return {"code": self.bp.read_bin()}
