import subprocess

result = subprocess.run(["python", "Hello.py"], capture_output=True, text=True)
output = result.stdout.strip()
lines = output.split("\n")

expected = [
    "['Hello', 'World!']",
    "('Hello', 'Brazil!')",
    "{'Hello', 'São Paulo!'}",
    "{'Hello': '42 São Paulo!'}",
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
