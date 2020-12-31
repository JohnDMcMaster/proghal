# proghal

Device programmer hardware abstraction layer.
Primarily intended for chip research where a chip needs to be repeatedly read.
As of 2020-12-30 this framework is still very preliminary.

Sample:

  ./main.py --prog minipro --device "27C64 @DIP28" --out out.bin read
  ./main.py --prog  --device "at89c51" --out out.bin read
  ./main.py --prog bpwahk --out out.bin read

Note that every device repesents it's device naming / database differently.
No effort is made to normalize them between programmers.

Terms:
* program: make best effort to write memory region(s). May include erase and write
* erase: erase given memory. Not supported on all devices
* write: write given memory region(s). Does not include erase
* read: read given memory region(s)
* lock: write one or more lock bits

