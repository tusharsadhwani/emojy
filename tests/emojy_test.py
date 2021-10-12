import sys
from unittest.mock import patch

import pytest
from pytest import CaptureFixture

from emojy import de_emojify, cli


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


@pytest.mark.parametrize(
    ("filepath", "output"),
    (
        ("examples/print.emojy", "Works❓ ✅\n"),
        ("examples/try.emojy", "Boom💥\n"),
    ),
)
def test_emojy(filepath: str, output: str, capsys: CaptureFixture[str]) -> None:
    testargs = ["emojy", filepath]
    with patch.object(sys, "argv", testargs):
        cli()

    stdout, _ = capsys.readouterr()
    assert stdout == output
