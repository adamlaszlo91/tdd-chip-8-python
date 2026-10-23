from display import Display
from device import Device


def main():
    device = Device(display=Display())

    with open("example/octojam1title.ch8", "rb") as f:
        device.run(f.read())


if __name__ == "__main__":
    main()

# test - init 0
# test - snapsnot does not change
# test - size and bounds
# first 512 0-511) is not accessable "original interpreter was located, and should not be used by programs."
# Most Chip-8 programs start at location 0x200 (512), but some begin at 0x600 (1536). Programs beginning at 0x600 are intended for the ETI 660 computer.
# parameter file name
# register init
# VF register should not be used by any program, as it is used as a flag by some instructions
# check program parity
# ue bit shift instead of % 16
# to_bytes(2)
