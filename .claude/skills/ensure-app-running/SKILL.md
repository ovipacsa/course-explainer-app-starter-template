---
name: ensure-app-running
description: "Ensures the Flask dev server is running at http://127.0.0.1:5000. Use after any implementation task, before taking screenshots or verifying features. Triggers when: task is done, verification is needed, Playwright screenshot is about to be taken, or user asks to open/run/start the app."
allowed-tools: Bash(curl:*), Bash(python:*)
---

# Ensure App Running Skill

## Role
Check whether the Flask application is already running and start it if not.

## Steps

1. Check if the app is up:
   ```bash
   curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5000
   ```

2. If the response is `200`, the app is already running — do nothing.

3. If the response is anything else (connection refused, non-200), start the app in the background:
   ```bash
   python src/app.py
   ```
   Then wait 2 seconds and re-check with curl to confirm it started successfully.

4. Report the result: either "App already running" or "App started at http://127.0.0.1:5000".
