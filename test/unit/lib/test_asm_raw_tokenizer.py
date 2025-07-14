import pytest

from lib.tokenizer.asm_raw_tokenizer import _AsmRawTokenizer
from lib.tokenizer.tokens import RawStrToken

# Note about the """ strings :
# The beginning of the string starts immediately after the """.
# The end of the string ends immediately before the """.
# This means that any spaces (including newlines) are considered as part of the
# string. The below string is equivalent to 'arg1 arg2\n':
# """arg1 arg2
# """
# Thus the formatting you see in the code samples below is required to assert
# that the strings start on the 0th (first) line of ASM code.dd


class Test_AsmRawTokenizer:
    @pytest.mark.parametrize(
        "code, expected",
        [
            (
                """arg1 arg2
""",
                [
                    RawStrToken(line=1, col=1, value="arg1"),
                    RawStrToken(line=1, col=6, value="arg2"),
                ],
            ),
            (
                """arg1 ;comment
arg2
                """,
                [
                    RawStrToken(line=1, col=1, value="arg1"),
                    RawStrToken(line=2, col=1, value="arg2"),
                ],
            ),
            (
                "arg1;this is a comment",
                [
                    RawStrToken(line=1, col=1, value="arg1"),
                ],
            ),
            (
                "  arg1\n\targ2   arg3\narg4",
                [
                    RawStrToken(line=1, col=3, value="arg1"),
                    RawStrToken(line=2, col=2, value="arg2"),
                    RawStrToken(line=2, col=9, value="arg3"),
                    RawStrToken(line=3, col=1, value="arg4"),
                ],
            ),
        ],
    )
    def test_tokenize(self, code, expected):
        tokenizer: _AsmRawTokenizer = _AsmRawTokenizer(code)
        tokens = tokenizer.tokenize()
        assert tokens == expected
