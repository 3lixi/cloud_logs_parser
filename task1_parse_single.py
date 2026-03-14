def parse_log_line(line: str):
    line = line.strip()
    if not line:
        return None
    parts = [p.strip() for p in line.split("|")]
    if len(parts) != 4:
        return None
    return tuple(parts)


def run_tests():
    cases = [
        ("2026-02-05 08:11:20 | ERROR | db | DB timeout",
         ("2026-02-05 08:11:20", "ERROR", "db", "DB timeout")),
        ("  2026-02-05 08:11:20|ERROR|db|DB timeout  \n",
         ("2026-02-05 08:11:20", "ERROR", "db", "DB timeout")),
        ("BAD LINE WITHOUT SEPARATORS", None),
        ("2026-02-05 | INFO | auth | ok | EXTRA", None),
    ]

    for i, (line, expected) in enumerate(cases, start=1):
        got = parse_log_line(line)
        print(f"Case {i}: expected={expected} got={got}")


if __name__ == "__main__":
    run_tests()
