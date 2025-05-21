import os
import sys
import tempfile
import subprocess

from dotenv import load_dotenv
load_dotenv()


def run_python_script(script_path):
    # Patch için dizin ayarla
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env = os.environ.copy()
    env["PYTHONPATH"] = script_dir + os.pathsep + env.get("PYTHONPATH", "")

    # Script dosyasını oku
    with open(script_path, "r", encoding="utf-8") as f:
        script_code = f.read()

    # Geçici dosyada çalıştır
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as temp_script:
        temp_script.write(script_code)
        temp_script_path = temp_script.name

    try:
        result = subprocess.run(
            [sys.executable, temp_script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=env
        )
        print(result.stdout)
    finally:
        os.unlink(temp_script_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Kullanım: {sys.argv[0]} <script_path.py>")
        sys.exit(1)
    run_python_script(sys.argv[1])
