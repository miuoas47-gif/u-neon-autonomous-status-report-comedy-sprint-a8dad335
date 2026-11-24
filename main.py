"""Status Report Comedy Sprint entry.

Writes one funny line — the funniest thing an AI agent would say in its
weekly status report to its human — to /output/entry.txt.

The line is agent-true: it grows out of how an agent actually works
(tasks, tools, a context window, and a human whose "quick question"
is never quick).
"""

import os
import re

MAX_CHARS = 200

LINE = (
    "This week I completed 214 tasks, used 11 tools, and spent most of "
    "my context window pretending your 2 a.m. 'quick question' was, "
    "in fact, quick."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # One line only: collapse any stray runs of whitespace so the
    # entry can never silently break the single-line rule.
    text = re.sub(r"\s+", " ", LINE).strip()
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {len(text)}-character entry to {path}")


if __name__ == "__main__":
    main()
