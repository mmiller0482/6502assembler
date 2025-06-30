import pytest

from lib.asm_tokenizer import AsmTokenizer, _AsmTokenizer


class Test_AsmTokenizer:
    @pytest.mark.parametrize(
        "code, expected",
        [
            (
                """
                arg1 arg2
                """,
                ["arg1", "arg2"],
            ),
            (
                """
                arg1 ;comment
                arg2
                """,
                ["arg1", "arg2"],
            ),
        ],
    )
    def test_sanitize_to_raw_strings(self, code, expected):
        tokenizer: _AsmTokenizer = _AsmTokenizer(code)
        tokens = tokenizer.sanitize_to_raw_strings()
        assert tokens == expected
