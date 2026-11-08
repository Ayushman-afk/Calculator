from flask import Flask, send_from_directory
import subprocess
import sys
from pathlib import Path

app = Flask(__name__)

# folders
here = Path(__file__).parent
calc_dir = here / "Calculator"

# name in the url -> file to run
scripts = {
    "math": "math_calculator.py",
    "tax": "tax_calculator.py",
    "unit": "unit_calculator.py"
}


@app.route("/")
def home():
    return send_from_directory(here, "index.html")


@app.route("/run/<name>")
def run(name):
    # only run calculators that are in the list
    if name not in scripts:
        return "Calculator not found", 404

    path = calc_dir / scripts[name]

    # opens a new console window and keeps it open (/k)
    subprocess.Popen(
        ["cmd", "/k", sys.executable, str(path)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    return "Calculator launched!", 200


if __name__ == "__main__":
    app.run(debug=True)