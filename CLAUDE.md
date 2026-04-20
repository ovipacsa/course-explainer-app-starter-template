# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
uv pip install -r requirements.txt

# Run development server (http://127.0.0.1:5000)
python src/app.py

# Run all tests
python -m unittest discover -s tests

# Run a single test
python -m unittest tests.test_app.AppTestCase.test_index
```

## Architecture

This is a minimal Flask web application that displays programming courses. It uses server-side rendering with Jinja2 templates — no build step, no JavaScript framework.

**Request flow**: `app.py` (routes) → `views.py` (handlers) → `models.py` (in-memory data) → `templates/` (Jinja2 rendering)

### Key files

- [src/app.py](src/app.py) — Flask app factory and route registration (`/` and `/course/<id>`)
- [src/views.py](src/views.py) — View functions; call `render_template()` with course data
- [src/models.py](src/models.py) — `Course` class and hardcoded in-memory course list (no database)
- [src/templates/layout.html](src/templates/layout.html) — Base template; all other templates extend this
- [tests/test_app.py](tests/test_app.py) — Unit tests using Flask's test client

### Data

All course data is hardcoded as `Course` instances in `models.py`. There is no database, no external API, and no environment configuration required to run the app.

### Unit Tests

- Whenever you add any changes, add unit tests, and run and make sure the test passes.

### Verify Changes with Playwright (MANDATORY)

**After implementing any new feature, you MUST:**
1. Start the Flask application (if not running - `python src/app.py`)
2. Use the Playwright MCP tool to connect to the application at `http://127.0.0.1:5000`
3. Navigate to and interact with the new feature to verify it works correctly.
4. Take a screenshot of the working feature.
5. Save the screenshot in the `test-output/` folder with a descriptive file name: (`feature-name-verification-YYYY_MM-DD.png`).

This step ensures that all feature are visually verified and provides documentation of the work state of the application.