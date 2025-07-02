from typing import List

from lib.tokenizer.asm_raw_tokenizer import _AsmRawTokenizer
from lib.tokenizer.tokens import AsmToken, RawStrToken



class AsmTokenizer:
    @classmethod
    def tokenize(cls, code: str) -> List[AsmToken]:
        raw_tokens: List[RawStrToken] = _AsmRawTokenizer(code).tokenize()
        return raw_tokens
        #categorized_tokens: List[AsmToken] =
        #return _AsmTokenizer(code).tokenize()
