# Tasks

## Completed

- [x] Add `Video` class and hardcoded video list to `src/models.py`
- [x] Add `videos_page()` view function to `src/views.py`
- [x] Register `/videos` route in `src/app.py`
- [x] Add "Videos" link to header nav in `src/templates/layout.html`
- [x] Create `src/templates/videos.html` with responsive YouTube embed grid
- [x] Add `.video-grid`, `.video-card`, and 16:9 iframe styles to `src/static/css/styles.css`
- [x] Add `test_videos` test case to `tests/test_app.py`

---

## Videos Page — Design & Business Logic

### Business Logic (`src/models.py`, `src/views.py`, `src/app.py`)
- **Data model**: `Video(title, description, video_id)` — `video_id` is the YouTube video ID (e.g. `"rfscVS0vtbw"`), not a full URL.
- **Data source**: Hardcoded in-memory list in `models.py`, consistent with how courses are stored. No database or YouTube API required.
- **Route**: `GET /videos` → `videos_page()` → renders `videos.html` with the full `videos` list passed as context.

### Template Design (`src/templates/videos.html`)
- Extends `layout.html` for consistent header/nav/footer.
- Iterates over the `videos` list with a Jinja2 `{% for %}` loop.
- Each video renders as a card with:
  - An `<iframe>` embed using `https://www.youtube.com/embed/{{ video.video_id }}`
  - `title` attribute on the iframe for accessibility
  - `allowfullscreen` for full-screen support
  - Title (`<h3>`) and description (`<p>`) below the embed

### CSS Design (`src/static/css/styles.css`)
- `.video-grid`: CSS grid with `auto-fill` columns, min 420px wide, 24px gap — adapts to screen width automatically.
- `.video-embed`: 16:9 aspect ratio wrapper using the padding-bottom trick (`padding-bottom: 56.25%`) so iframes scale responsively without JavaScript.
- `.video-card`: White card with subtle box shadow, matching the existing content card style.

## Pending

<!-- Add future tasks here -->
