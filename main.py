#!/usr/bin/env python3

from proghal import progs
from bpwahk import hexdump
from bpmicro.util import add_bool_arg

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Read remotely and store / display')
    # FIXME: hacky bridge options for now
    parser.add_argument('--bpwahk-host', type=str, default=None)
    parser.add_argument('--bpwahk-port', type=int, default=None)
    parser.add_argument('--device')
    add_bool_arg(parser, "--force", default=False)
    parser.add_argument('--out', help="Output file name for read")
    parser.add_argument('prog')
    parser.add_argument('operation', help='Operation: read, program, erase, protect, list_device, nop') 
    args = parser.parse_args()

    init_cfg = {}
    if args.bpwahk_host:
        init_cfg["host"] = args.bpwahk_host
    if args.bpwahk_port:
        init_cfg["port"] = args.bpwahk_port
    prog = progs.get_prog(args.prog, init_cfg)

    # Only supported for now
    assert args.operation == "read"
    cfg = {}
    if args.device:
        cfg["device"] = args.device
    if args.force:
        cfg["force"] = args.force
    read = prog.read(cfg)
    if args.out:
        open(args.out, "wb").write(read["code"])
    else:
        hexdump(read["code"])

if __name__ == "__main__":
    main()
