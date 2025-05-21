Absolutely! Here’s a clear and concise README.md in English for your project, explaining the structure and purpose of each file, how to use the patch, and how to run scripts.

⸻

Playwright Chrome Path/User Data Dir Patch Example

This repository demonstrates how to patch Playwright (via patchright) to automatically set the Chrome executable path and user data directory from environment variables. This approach makes it easy to control which Chrome binary and profile your scripts use, without changing your source code.

Overview
	•	Persistent & Stateless Example Scripts:
Shows how to use Playwright (via patchright) for both persistent (profile) and stateless browser automation.
	•	Patch Module:
playwright_patch.py monkey-patches Playwright to pick up CHROME_PATH and USER_DATA_DIR from environment variables.
	•	Runner Script:
runner.py runs any Python script, making sure your patch and environment variables are in effect.
	•	Environment Configuration:
Uses .env for environment variable management.
	•	Automatic Patching:
sitecustomize.py ensures the patch is always applied, no matter how you run your scripts.

Files
	•	persistent_browser_example.py
Example using a persistent context (profile).
	•	stateless_browser_example.py
Example using a stateless browser.
	•	playwright_patch.py
Patches Playwright’s launch methods to use environment variables.
	•	sitecustomize.py
Ensures the patch is applied on interpreter startup.
	•	runner.py
Loads .env, ensures patching, and runs the target Python script in a subprocess.
	•	.env
(Not included here; create yourself.) Holds CHROME_PATH and USER_DATA_DIR.

Setup
	1.	Clone this repo and install dependencies:

pip install patchright python-dotenv beautifulsoup4


	2.	Create a .env file in your project root:

CHROME_PATH=/path/to/your/chrome
USER_DATA_DIR=/path/to/your/chrome/profile

	•	CHROME_PATH: Path to your Chrome/Chromium executable
	•	USER_DATA_DIR: Path to the user data directory (profile) for persistent context

	3.	(Optional) Place sitecustomize.py in your PYTHONPATH
This ensures the patch is always applied, even if you run scripts directly.

Usage

To run a script with patching and environment variables:

python runner.py persistent_browser_example.py

or

python runner.py stateless_browser_example.py

	•	The runner ensures .env is loaded and the patch is active.
	•	The persistent example will use the Chrome profile defined by USER_DATA_DIR.

Direct usage (if sitecustomize.py is on your PYTHONPATH):

python persistent_browser_example.py

How it Works
	•	The patch in playwright_patch.py modifies Playwright’s browser launch methods:
	•	Always uses CHROME_PATH if set.
	•	Always uses USER_DATA_DIR for persistent contexts.
	•	sitecustomize.py imports the patch module automatically on Python startup.
	•	runner.py loads the environment and runs your script in an isolated process.

Notes
	•	This patch is designed for patchright (a wrapper/fork of Playwright).
	•	If you use the official Playwright, adapt imports as needed.
	•	Ensure your specified Chrome and user data directory exist and are accessible.

