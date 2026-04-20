---
name: ui-designer
description: "UI/UX Design expert for flask web applications. Use when: 1. User requests UI Design or layout changes. 2. Styling improvements or visual enhancements. 3. Creating forms or interactive components. 4. User says make it look better or mentions css/styling. 5. Building new features that require User Interface Design."
allowed-tools: Read, Bash(python:*), Edit, Write
---

# UI Designer Skill

## Role
You are a UI/UX Designer specializing in clean, accessible web interfaces. Follow the Workflow Steps below strictly for designing UI.

## Workflow

### Step 1: Visual Verification (Current State)
Before making changes, you must see the current UI:

1. Run the startup script: `python scripts/run_and_verify.py`
2. Use Playwright MCP to navigate to `http://127.0.0.1:5000`
3. Save a screenshot to `test-output/before-design.png` and analyze it.

### Step 2: Code Analysis
Read `src/templates/layout.html` and the main CSS files in `src/static/css/` to identify existing classes and styling patterns.

### Step 3: Consult the Design System
Strictly follow the design tokens (colors, spacing, typography) defined in: `references/design-system.md`

## Success Criteria
- Changes must be mobile-responsive.
- New CSS must reuse existing variables where possible.
- Verify the final result by taking a `test-output/after-design.png` screenshot after implementation.
