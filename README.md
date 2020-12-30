# proghal

Device programmer hardware abstraction layer.
Primarily intended for chip research where a chip needs to be repeatedly read.
As of 2020-12-30 this framework is still very preliminary.

Sample:

  ./main.py --out out.bin --device "27C64 @DIP28" minipro read

Terms:
* program: make best effort to write memory region(s). May include erase and write
* erase: erase given memory. Not supported on all devices
* write: write given memory region(s). Does not include erase
* read: read given memory region(s)
* lock: write one or more lock bits

