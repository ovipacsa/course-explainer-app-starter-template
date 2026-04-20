---
name: '80s Retro Theme Design Decisions
description: UX decisions and design system established for the '80s retro/synthwave theme overhaul
type: project
---

A full visual re-theme of CodeLearn to an '80s synthwave/retrowave aesthetic was designed. Key decisions:

**Color palette:**
- Background: #0a0a0f (near-black)
- Primary neon: #ff006e (hot pink)
- Secondary neon: #00f5ff (electric cyan/blue)
- Accent neon: #39ff14 (lime green)
- Purple accent: #bf00ff (electric purple)
- Surface/card: #0f0f1a (dark navy)
- Border/grid: rgba(0, 245, 255, 0.15)

**Typography:**
- Display/headings: "Press Start 2P" (Google Fonts) — pixel retro feel
- Body/UI text: "Share Tech Mono" (Google Fonts) — monospace, readable
- Inter dropped entirely

**Signature effects (CSS only):**
- Glowing text via multi-layer text-shadow in neon colors
- Scanline overlay via ::before pseudo-element with repeating-linear-gradient
- Perspective grid floor via CSS transform on a pseudo-element (hero only)
- Neon border glow on cards via box-shadow with neon color
- CRT flicker animation via @keyframes opacity oscillation (subtle, on hero title)
- Hover state: neon border brightens + translateY(-4px)

**Component naming conventions established:**
- RetroNavbar — sticky header with neon logo glow, nav links with neon hover underline
- RetroHeroSection — dark bg, perspective grid floor, large glowing headline, neon CTA button
- NeonButton (.btn-neon) — hot-pink border + glow, dark fill, monospace text
- RetroCard (.retro-card) — dark surface, neon left-border accent, glow on hover
- ScanlineOverlay — full-page ::before pseudo on body for CRT scanline texture
- RetroStatBar — dark strip with neon number counters
- RetroFooter — dark, neon brand glow, grid-line top border

**Empty/edge state convention:** Empty states use centered neon-bordered box with "NO SIGNAL" or similar retro system message text.

**Why:** User story requested '80s style design. Synthwave/retrowave chosen as the authentic interpretation — neon on dark, grid lines, pixel fonts, CRT effects.

**How to apply:** All future page specs for this app should use this palette and component vocabulary unless the user requests a change.
