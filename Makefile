VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
	$(PYTHON) src/bot.py

setup: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
