from typing import Generator
from typing import Iterable
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Sequence
from typing import Tuple

ESCAPED_NL = "ESCAPED_NL"
UNIMPORTANT_WS = "UNIMPORTANT_WS"
NON_CODING_TOKENS = frozenset(("COMMENT", ESCAPED_NL, "NL", UNIMPORTANT_WS))

class Offset(NamedTuple):
    line: Optional[int] = None
    utf8_byte_offset: Optional[int] = None

class Token(NamedTuple):
    name: str
    src: str
    line: Optional[int] = None
    utf8_byte_offset: Optional[int] = None
    @property
    def offset(self) -> Offset:
        return Offset(self.line, self.utf8_byte_offset)

def src_to_tokens(src: str) -> List[Token]: ...
def tokens_to_src(tokens: Iterable[Token]) -> str: ...
def reversed_enumerate(
    tokens: Sequence[Token],
) -> Generator[Tuple[int, Token], None, None]: ...
def parse_string_literal(src: str) -> Tuple[str, str]: ...
def rfind_string_parts(tokens: Sequence[Token], i: int) -> Tuple[int, ...]: ...
def main(argv: Optional[Sequence[str]] = None) -> int: ...
