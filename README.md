# LLM Notes App

This is a basic fastapi application which serve the html pages of LLM notes, with the help of jinja template.

## Preerquisite:
- Make sure your system have python and `uv` package manager installed, if not then go to the respective offical website and install those.


### To use this app, follow this step by step approach at your local workspace.

1. Clone the repo : `git clone <repo url>`
2. Create virtual environment : `uv venv`
3. Activate the environment : `.venv/script/activate` (Windows) or `source .venv/bin/activate` (Linux/MacOS)
4. Install all dependencies : `uv add -r requirements.txt`
5. Run the server : `uvicorn main:app --reload`
6. Go to: `http://127.0.0.1:8000`