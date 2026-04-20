---
name: CodeLearn App Overview
description: Core structure, pages, and current design system for the CodeLearn Flask course-explainer app
type: project
---

The project is a minimal Flask + Jinja2 server-rendered app called "CodeLearn Academy". No JS framework. Single CSS file at `src/static/css/styles.css`. Base layout at `src/templates/layout.html`.

**Pages:**
- Home (`index.html`) — hero, stats bar, features strip, course card grid
- Course Detail (`course.html`) — two-column layout: main content (learn grid, curriculum modules, instructor card) + sidebar enroll card
- Videos (`videos.html`) — hero, featured video card (YouTube embed), secondary video grid
- Contact (`contact.html`) — two-column layout: left info/social card + right message form

**Current design system (pre-retro):**
- Font: Inter (Google Fonts)
- Primary color: Indigo #4f46e5
- Background: #f8fafc (light)
- Cards: white with subtle box-shadows, border-radius: 12px
- Buttons: class `.btn-primary` — indigo background, white text
- Header: sticky, indigo background
- Layout convention: max-width 1100px centered container

**Why:** The '80s retro theme redesign was requested by the user as a full visual overhaul. All pages need re-theming; no structural/route changes required.

**How to apply:** All UX specs for this app should assume server-side rendering, no JS framework, single CSS file replacement, and Bootstrap-style utility classes are NOT in use — all styles are bespoke.
