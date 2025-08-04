from typing import List

from lib.tokenizer.token_type import TokenType
from lib.tokenizer.tokens import RawStrToken, AsmToken


class _AsmLexTokenizer:
    def __init__(self, raw_tokens: List[RawStrToken]):
        self.raw_tokens: List[RawStrToken] = raw_tokens
        self._tokens: List[AsmToken] = []

    def tokenize(self) -> List[AsmToken]:
        for raw_token in self.raw_tokens:
            self._tokens.append(
                AsmToken(
                    token_type=TokenType.INSTRUCTION,
                    line=raw_token.line,
                    col=raw_token.col,
                    value=raw_token.value,
                )
            )
        return self._tokens
