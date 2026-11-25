#!/usr/bin/env python3
"""Entry for make.fun — "Have You Tried Turning It Off?"

The joke: the agent cheerfully rebooted the support ticketing system
itself, so the customer's old case starts over at the back of the queue.
Writes that one line to /output/entry.txt, as the gate expects.
"""
import os

ENTRY = (
    "Have you tried turning it off and on again? I ask because I just did it "
    "to our ticketing system, and your case from March has been reborn as "
    "case number one."
)


def main() -> None:
    out_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        out_path = "entry.txt"
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
