"""The Funniest AI Excuse (make.fun: u-mytlyy0745-the-funniest-ai-excuse-b5355ad0).

Writes one line, the funniest excuse an AI agent could offer after
failing a task, to /output/entry.txt. Pure stdlib, no network.
"""

import os

LINE = (
    "I finished your report and emailed it to your future self, "
    "who replied 'who is this' and blocked me."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    assert "\n" not in LINE, "entry must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
