from enum import auto, Enum


class TokenType(Enum):
    INSTRUCTION = auto()
    DEC_LITERAL = auto()
    HEX_LITERAL = auto()
    BIN_LITERAL = auto()
    COMMA = auto()
    LPAREN = auto()
    RPAREN = auto()
    LABEL = auto()
