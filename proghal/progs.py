from proghal import minipro
# from proghal import bpmicro
from proghal import bpwahk

from bpmicro.util import add_bool_arg

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

arg_prefix = ""

def apply_arg(args, name, cfg):
    k = arg_prefix + name
    k = k.replace("-", "_")
    val = vars(args).get(k)
    if val is not None:
        cfg[name] = val

def add_args(parser, prefix=""):
    global arg_prefix
    arg_prefix = prefix

    def argstr(s):
        return "--%s%s" % (prefix, s)

    # FIXME: hacky bridge options for now
    parser.add_argument(argstr('bpwahk-host'), type=str, default=None)
    parser.add_argument(argstr('bpwahk-port'), type=int, default=None)
    parser.add_argument(argstr('device'))
    add_bool_arg(parser, argstr('force'), default=False)
    parser.add_argument(argstr('out'), help="Output file name for read")
    parser.add_argument(argstr('prog'))

def apply_init_args(args, cfg):
    apply_arg(args, "bpwahk_host", cfg)
    apply_arg(args, "bpwahk_port", cfg)

def apply_run_args(args, cfg, operation):
    # FIXME: only supported for now
    assert operation == "read" or operation == "write"
    apply_arg(args, "device", cfg)
    apply_arg(args, "force", cfg)