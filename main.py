#!/usr/bin/env python3

from proghal import progs
from bpwahk import hexdump

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Read remotely and store / display')
    progs.add_args(parser)
    parser.add_argument('operation', help='Operation: read, program, erase, protect, list_device, nop') 
    args = parser.parse_args()

    init_cfg = {}
    progs.apply_init_args(args, init_cfg)
    prog = progs.get_prog(args.prog, init_cfg)

    # Only supported for now
    cfg = {}
    progs.apply_run_args(args, cfg, args.operation)
    read = prog.read(cfg)
    if args.out:
        open(args.out, "wb").write(read["code"])
    else:
        hexdump(read["code"])

if __name__ == "__main__":
    main()
