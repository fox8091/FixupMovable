#!/usr/bin/env python

import sys

def patchMovable(movableData):
    movableData[0x4:0x8] = b'\x00'*4
    movableData = movableData[:0x120]
    
    return movableData

def syntax():
    print("Syntax:")
    print("  python FixupMovable.py movable.sed")
    return 1

def main(argv):
    try:
        if len(argv) < 2:
            return syntax()
        with open(argv[1], mode="rb") as f:
            movableBytes = bytearray(f.read())
            f.close()
        with open(argv[1], mode="wb") as f:
            f.write(patchMovable(movableBytes))
        return 0
    except Exception as e:
        print(str(e))
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
