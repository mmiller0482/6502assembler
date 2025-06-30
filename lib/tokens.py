from dataclasses import dataclass

from lib.token_type import TokenType


@dataclass
class AsmToken:
    token_type: TokenType

@dataclass
class RawStrToken:
    # line in the file where token came from
    line: int

    # col where the first character of the token appears.
    col: int
    value: str
