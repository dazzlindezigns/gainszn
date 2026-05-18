# GainSzn 🐺

> Feed the wolf. State relay. Wolves football. You don't eat like a backup.

**GainSzn** is KJ's personal bulk-phase PWA — a mobile-first meal tracking app built for a 15-year-old multi-sport athlete: Weiss Wolves football player, dancer, and part of the first 4x100 relay team in Weiss High School history to reach State (7th place).

**Goal:** Get KJ from 140 lbs → 160+ lbs by football season via consistent 3,500 cal/day eating.

---

## Features

| Feature | Description |
|---|---|
| **Meal Log** | Tap to log food, calories, protein — auto-timestamped |
| **Eating Schedule** | 6 daily meal windows (7am, 10am, 12:30pm, 3:30pm, 6:30pm, 9pm) with targets |
| **Push Notifications** | Meal-time alerts + 45-min "bro you forgot" follow-ups |
| **Parent Dashboard** | PIN-protected (2010) with full log, totals, and Share Summary |
| **Food Suggestions** | Categorized by meal type with cal/protein; quick-add to log |
| **Missed Meal Alert** | Pulsing red alert if nothing logged by 10am |
| **Daily Goal Ring** | Visual calorie ring targeting 3,500 cal/day with motivational copy |
| **PWA** | Installable on iOS and Android, full offline support |

---

## Brand

- **Colors:** `#CC0000` (red), `#0A0A0A` (black), `#FFFFFF` (white)
- **Fonts:** Bebas Neue (display), Barlow Condensed (UI)
- **School:** Weiss Wolves, Austin TX

---

## Tech Stack

- Vanilla HTML/CSS/JS — no frameworks, single-file deployable
- Progressive Web App (service worker, manifest, offline cache)
- localStorage for meal persistence
- Web Notifications API for meal alerts

---

## File Structure

```
/index.html          — Full app (HTML + CSS + JS)
/manifest.json       — PWA manifest
/sw.js               — Service worker (caching + notifications)
/icons/
  icon-192x192.png   — App icon
  icon-512x512.png   — App icon (large)
/README.md
```

---

## Deploy

### Vercel
```bash
npx vercel --prod
```

### Netlify
Drop the repo folder into [app.netlify.com](https://app.netlify.com) or:
```bash
netlify deploy --prod --dir .
```

No build step required — static files only.

---

## Parent Dashboard

- Access via **PARENT** button (top right)
- PIN: `2010` (KJ's birth year)
- Shows: today's full meal log, total calories, meals logged, last ate time
- **Share Summary** copies a formatted text report to clipboard

---

## Notifications

Tap the banner on the home screen to enable meal alerts. The app will:
1. Notify at each meal window (7am, 10am, 12:30pm, 3:30pm, 6:30pm, 9pm)
2. Send a follow-up after 45 minutes if nothing was logged in that window
3. Trigger a "BRO." alert at 10am if zero meals have been logged

---

*GainSzn don't stop for nothing.*
