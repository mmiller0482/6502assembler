from typing import List

from lib.tokenizer.tokens import RawStrToken


class _AsmRawTokenizer:
    def __init__(self, code: str):
        self.code = code
        self._raw_tokens: List[RawStrToken] = []

    def tokenize(self) -> List[RawStrToken]:
        lines: List[str] = self.code.splitlines()
        for line_num, line in enumerate(lines, start=1):
            self._process_line(line_num, line)

        return self._raw_tokens

    def _process_line(self, line_num: int, line: str) -> None:
        line_no_comments = line.split(";")[0]
        current_string = ""
        tok_start_col = 0

        for col_num, char in enumerate(line_no_comments, start=1):
            if char.isspace():
                self._flush_token(line_num, tok_start_col, current_string)
                current_string = ""
            else:
                if not current_string:
                    tok_start_col = col_num
                current_string += char

        self._flush_token(line_num, tok_start_col, current_string)

    def _flush_token(self, line: int, col: int, value: str):
        """
        if the current value is not empty, add it to the raw tokens list
         with annotations
        """
        if value:
            raw_token = RawStrToken(line=line, col=col, value=value)
            self._raw_tokens.append(raw_token)
