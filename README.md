# KeyloggerBasic
# Ethical Keyboard Stats Utility

A small, consent-first keyboard listener that records **aggregated key counts** to a local JSON file. Built for personal testing, accessibility research, or debugging keyboard-driven features — **not** for covert monitoring. Press **F9** to start/stop recording and **ESC** to exit.

---

## Features

* Toggle recording with a single key (F9).
* Aggregates counts per key (no per-keystroke timestamps or raw typed text).
* Appends one JSON object per recording session to `keyboard_stats.json`.
* Cross-platform (Linux / macOS / Windows) as supported by `pynput`.

---

## Quick start

### Requirements

* Python 3.8+
* `pynput` library

Install dependency:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install pynput
```

### Run

```bash
python basickeylogger.py
```

Then:

* Press **F9** to start recording.
* Press **F9** again to stop and save aggregated stats.
* Press **ESC** to exit the program (stops recording and saves if active).

---

## Output format

Each recording session is appended as a single JSON object (one-per-line) in `keyboard_stats.json`. Example line:

```json
{"timestamp": "2025-10-17 20:15:34", "counts": {"a": 12, "b": 3, "Key.space": 5, "Key.enter": 2}}
```

`timestamp` is the time when recording stopped; `counts` maps keys (single chars or `Key.*` names) to counts.

---

## Installation & development

1. Clone the repo:

   ```bash
   git clone https://github.com/vinsmoke-sanji-11/KeyloggerBasic.git
   cd KeyloggerBasic
   ```


## Safety, ethics, and legal notice

This project is intended for **use only on machines you own or have explicit, informed permission to test**. Recording someone’s keystrokes without their knowledge or consent is illegal in many jurisdictions and is a violation of privacy.

By using this project you agree to:

* Only run it on your own devices or with explicit written consent.
* Use it for legitimate, ethical purposes (accessibility research, debugging, authorized testing).
* Delete any recordings immediately if requested by an owner of the recorded device.

The author is not responsible for misuse. If you plan to use this for security testing, obtain written authorization and follow all applicable laws and organizational policies.

---

## Troubleshooting

* Listener not capturing keys:

  * Make sure you run the script in a session with the required permissions (some OSes require accessibility permissions; macOS needs Accessibility permission).
  * Check that `pynput` is installed in the environment you are using.

* On Linux, if keys are not captured inside certain terminal multiplexers, try running the script outside tmux/screen or from a different terminal.

---

## Contributing

Contributions are welcome for:

* Improving documentation and cross-platform notes.
* Adding unit tests or CI to validate basic behavior.
* Providing packaging (PyPI) or installer scripts.

Please open issues or PRs. Keep all changes respectful of the project's ethical focus.

---



---

## Acknowledgements

Built with `pynput`. Thanks for keeping testing ethical and consent-first.
