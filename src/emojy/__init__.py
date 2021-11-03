"""emojy: Write Python with emojis!"""
import sys
from typing import List

import tokenize_rt

from emojy.emoji_table import EMOJI_TABLE


def de_emojify(emoji_code: str) -> str:
    """Convert emojified Python into regular Python"""
    converted_tokens: List[tokenize_rt.Token] = []

    unresolved_text = ""
    for token in tokenize_rt.src_to_tokens(emoji_code):
        if token.name == "STRING":
            converted_tokens.append(token)
            continue

        src_list: List[str] = []
        text = token.src
        # TODO: we need to check if the current text could be the part of an emoji sequence.
        # if yes, we add it to unresolved_text, and keep getting more tokens as long as
        # any of the existing tokens start with unresolved_text.
        # if we find a match, we resolve it.
        # if it no longer matches any key in emoji table, we just add it as-is.
        # in both cases, we empty unresolved text at the end.
        for emoji in EMOJI_TABLE:
            if emoji == text:
                src_list.append(EMOJI_TABLE[text])
                break
        else:
            src_list.append(text)

        new_src = "".join(src_list)
        converted_token = tokenize_rt.Token._replace(token, src=new_src)
        converted_tokens.append(converted_token)

    de_emojified_code = tokenize_rt.tokens_to_src(converted_tokens)
    return de_emojified_code


def run_emojy(emoji_code: str) -> None:
    code = de_emojify(emoji_code)
    exec(code)


def cli() -> None:
    """CLI interface"""
    filename = sys.argv[1]
    with open(filename) as file:
        emoji_code = file.read()
        run_emojy(emoji_code)


def main() -> None:
    """Main function"""
    code = "📺(👍 👐 👎)"
    print(f"code: {code}")
    print(f"output: ", end="")
    run_emojy(code)
