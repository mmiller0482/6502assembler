from typing import List

import pytest

from lib.tokenizer.asm_lex_tokenizer import _AsmLexTokenizer
from lib.tokenizer.token_type import TokenType
from lib.tokenizer.tokens import RawStrToken, AsmToken


def raw_tokens_from_line_strs(strs: List[str], lineno: int = 0) -> List[RawStrToken]:
    """Returns a list of raw tokens from a line. Assumes that there would be
    exactly one whitespace between the two tokens for realistic line/col
    values.

    strs: list of pre-stripped strings to represent raw tokens.
    lineno: the line number of the tokens, defaults to 0.
    """
    raw_tokens: List[RawStrToken] = []
    col_idx = 0
    for token_str in strs:
        raw_tokens.append(RawStrToken(line=lineno, col=col_idx, value=token_str))
        col_idx = col_idx + len(token_str) + 1

    return raw_tokens


class Test_AsmLexTokenizer:
    @pytest.mark.parametrize(
        "raw_token_strs, expected",
        [
            (
                ["ADD"],
                [
                    AsmToken(
                        token_type=TokenType.INSTRUCTION, line=0, col=0, value="ADD"
                    ),
                ],
            )
        ],
    )
    def test_tokenize(self, raw_token_strs, expected):
        raw_tokens = raw_tokens_from_line_strs(raw_token_strs)
        tokenizer = _AsmLexTokenizer(raw_tokens)
        res = tokenizer.tokenize()
        assert res == expected
        b = 4
