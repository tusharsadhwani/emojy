from emojy import de_emojify

import pytest


@pytest.mark.parametrize(
    ("input", "output"),
    (
        ("🔽 this", "import this"),
        ("👍 🤝 👎", "True and False"),
    ),
)
def test_de_emojify(input: str, output: str) -> None:
    """Ensure de-emojification works correctly."""
    assert de_emojify(input) == output
