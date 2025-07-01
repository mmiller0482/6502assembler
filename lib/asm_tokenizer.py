from typing import List

from lib.tokens import AsmToken, RawStrToken


class _AsmTokenizer:
    def __init__(self, code: str):
        self.code = code

    def tokenize(self) -> List[AsmToken]:  # strategy maybe?
        raw_tokens: List[str] = self.sanitize_to_raw_strings()
        # take the raw tokens and do something cool with them.
        # return tokenized raw tokens

    def sanitize_to_raw_strings(self):
        tokens: List[RawStrToken] = []
        lines: List[str] = self.code.splitlines()
        for line_num, line in enumerate(lines, start=1):
            # strip off anything out of the line after comments
            line_no_comments = line.split(";")[0]

            current_string = ""
            current_string_start_col = 0
            for col_num, char in enumerate(line_no_comments, start=1):
                if not current_string and char.isspace():
                    continue

                if not char.isspace() and not current_string:
                    current_string_start_col = col_num
                    current_string += char
                elif not char.isspace() and current_string:
                    current_string += char
                elif char.isspace() and current_string:
                    tokens.append(
                        RawStrToken(
                            line=line_num,
                            col=current_string_start_col,
                            value=current_string,
                        )
                    )
                    current_string = ""
            if current_string:
                tokens.append(
                    RawStrToken(
                        line=line_num,
                        col=current_string_start_col,
                        value=current_string,
                    )
                )

        return tokens


class AsmTokenizer:
    @classmethod
    def tokenize(cls, code: str) -> List[AsmToken]:
        return _AsmTokenizer(code).tokenize()
