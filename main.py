import sys
import asyncio
import os
import json

from runner import execute_python_code



def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_code_file>")
        sys.exit(1)

    code_file = sys.argv[1]
    if not os.path.isfile(code_file):
        print(f"File not found: {code_file}")
        sys.exit(1)

    with open(code_file, "r", encoding="utf-8") as f:
        code = f.read()

    result = asyncio.run(execute_python_code(code))
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()