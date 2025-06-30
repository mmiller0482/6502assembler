import sys
from typing import List

from exceptions import Assembler6502LoadError


class Assembler6502: ...


def main(args: List[str]):
    if len(args) != 1:
        raise Assembler6502LoadError("Invalid number of arguments")
    filename = args[0]

    try:
        with open(filename, "r") as f:
            print(f"Contents: {f.read()}")
    except FileNotFoundError:
        raise Assembler6502LoadError(f"File not found: {filename}")


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Assembler6502LoadError as e:
        print(e)
        exit(1)
