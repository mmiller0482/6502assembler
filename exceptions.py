from assemblerhelp import ARGHELP


class Assembler6502Error(Exception): ...


class Assembler6502LoadError(Assembler6502Error):
    def __init__(self, message: str):
        super().__init__(f"Assembler6502LoadError: {message} \n {ARGHELP}")
