from proghal import minipro
# from proghal import bpmicro
from proghal import bpwahk

# Some day open-tl866...
str2prog = {
    'minipro': minipro.Minipro,
    # 'bpmicro': bpmicro.BPMicro,
    'bpwahk': bpwahk.BPWAHK,
}

def get_prog(prog, cfg={}):
    try:
        return str2prog[prog](cfg)
    except KeyError:
        raise Exception("Invalid programmer %s. Try --list-prog" % prog)
