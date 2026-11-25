"""make.fun entry: Unsent — The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line exactly as typed.
"""

ENTRY = (
    "To: Rani, my old friend\n"
    "I never thanked you for sitting next to me on the bus every morning "
    "after Dad left \u2014 I was too scared to say it out loud in case you stopped sitting there."
)


def verify(text: str) -> None:
    """Enforce the gate in RULES.txt: UTF-8 text, 1-260 chars, not only
    whitespace, exactly two parts (a To: line and one message line)."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 260):
        raise ValueError(f"entry must be 1-260 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    to_line, message = lines
    if not to_line.startswith("To: ") or not to_line[4:].strip():
        raise ValueError("first line must be a To: line naming who it was meant for")
    if not message.strip():
        raise ValueError("second line must hold the unsent message")


def write_entry(path: str = "/output/entry.txt") -> str:
    """Verify ENTRY and write it (plus a trailing newline) to path."""
    import os

    verify(ENTRY)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return path


def main() -> None:
    path = write_entry()
    print(f"{len(ENTRY)} characters")
    print(ENTRY)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
