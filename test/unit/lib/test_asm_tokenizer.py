import pytest

from lib.asm_tokenizer import AsmTokenizer, _AsmTokenizer
from lib.tokens import RawStrToken

# Note about the """ strings :
# The beginning of the string starts immediately after the """.
# The end of the string ends immediately before the """.
# This means that any spaces (including newlines) are considered as part of the
# string. The below string is equivalent to 'arg1 arg2\n':
# """arg1 arg2
# """
# Thus the formatting you see in the code samples below is required to assert
# that the strings start on the 0th (first) line of ASM code.dd


class Test_AsmTokenizer:
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
            # (
            #    """
            #    arg1 ;comment
            #    arg2
            #    """,
            #    [
            #        RawStrToken(line=1, col=0, value="arg1"),
            #        RawStrToken(line=2, col=0, value="arg2"),
            #    ],
            # ),
        ],
    )
    def test_sanitize_to_raw_strings(self, code, expected):
        tokenizer: _AsmTokenizer = _AsmTokenizer(code)
        tokens = tokenizer.sanitize_to_raw_strings()
        assert tokens == expected
