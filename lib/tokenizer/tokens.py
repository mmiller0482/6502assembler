from dataclasses import dataclass

from lib.tokenizer.token_type import TokenType


@dataclass
class AsmToken:
    # Shares most with the RawStrToken class
    token_type: TokenType
    line: int
    col: int
    value: str = ""


@dataclass
class RawStrToken:
    # line in the file where token came from
    line: int

    # col where the first character of the token appears.
    col: int

    # literal string value of the token
    value: str
