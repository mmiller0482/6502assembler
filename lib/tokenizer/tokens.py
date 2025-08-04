from dataclasses import dataclass

from lib.tokenizer.token_type import TokenType


@dataclass
class AsmToken:
    # Shares most with the RawStrToken class

    # Enum declaring lexical type of this token's contents
    token_type: TokenType

    # line in which token appears in file
    line: int

    # column at which the first character of the token appears
    col: int

    # value of the token.
    value: str = ""


@dataclass
class RawStrToken:
    # line in the file where token came from
    line: int

    # col where the first character of the token appears.
    col: int

    # literal string value of the token
    value: str
