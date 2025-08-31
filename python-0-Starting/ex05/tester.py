import subprocess

text = (
    "Python 3.0, released in 2008, was a major revision that is not "
    "completely backward-compatible with earlier versions. Python 2 was "
    "discontinued with version 2.7.18 in 2020."
)

result = subprocess.run(
    ["python", "building.py", text],
    capture_output=True,
    text=True,
)

output = result.stdout.strip()
lines = output.split("\n")

expected = [
    "The text contains 171 characters:",
    "2 upper letters",
    "121 lower letters",
    "8 punctuation marks",
    "25 spaces",
    "15 digits",
]


def validate_output(lines, expected):
    if len(lines) != len(expected):
        return False
    for line, exp in zip(lines, expected):
        if line.strip() != exp:
            return False
    return True


if validate_output(lines, expected):
    print("✅ Output is valid!")
else:
    print("❌ Output is invalid!")
    print("Expected:")
    print("\n".join(expected))
    print("Received:")
    print("\n".join(lines))
