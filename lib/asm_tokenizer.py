from typing import List

from lib.tokens import AsmToken


class _AsmTokenizer:
    def __init__(self, code: str):
        self.code = code

    def tokenize(self) -> List[AsmToken]: # strategy maybe?
        raw_tokens: List[str] = self.sanitize_to_raw_strings()
        # take the raw tokens and do something cool with them.
        # return tokenized raw tokens

    def sanitize_to_raw_strings(self):
        tokens: List[str] = []
        lines: List[str] = self.code.splitlines()
        for line in lines:
            # strip off anything out of the line after comments
            line_no_comments = line.split(";")[0]

            sanitized_tokens = line_no_comments.split()
            tokens.extend(sanitized_tokens)
        return tokens


class AsmTokenizer:
    @classmethod
    def tokenize(cls, code: str) -> List[AsmToken]:
        return _AsmTokenizer(code).tokenize()
