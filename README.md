# Al's Plumbing (Plano, TX): demo site

Mobile-first marketing demo for **Al's Plumbing** ("Al's Plumbing, Heating & Air Conditioning"), 1108 Summit Ave #5, Plano, TX 75074 · (972) 422-7301.

> Independent demo site, not affiliated with or endorsed by Al's Plumbing. Built from public information: the Google Maps listing (4.6★, 198 reviews, checked Nov 9, 2026) and the public BBB profile (A+ rating, business started 1993).

Live: https://als-plumbing-plano-production.up.railway.app

## Design

No logo, signage or lettered trucks exist in public photos, so the site uses a text wordmark (not a fake logo). The palette comes from the only brand artwork: the owner's 2016 "Plumbing / Heating / Cooling" banner on Google Maps.

| Role | Hex | Source |
| --- | --- | --- |
| Navy (header, hero, footer) | `#13254A` | Deepened from the banner's blue label bars |
| Banner blue (links, icons, hero label bars) | `#3B62B0` | Banner label bars, sampled |
| Yellow (CTAs only) | `#F2D21B` | The yellow gauge in the banner's "Cooling" panel |
| Cool grey (secondary text) | `#4A5466` | Technician's grey uniform shirt in the "Heating" panel |
| White / tint | `#FFFFFF` / `#F3F5F9` | Banner's white background |

Type: Archivo 700/800 (self-hosted via @fontsource) for headings and wordmark; system UI font for body.

## Checks

- 17px body text, 48px+ tap targets, sticky Call / Directions bar under 960px
- `document.documentElement.scrollWidth === 375` at 375px; no overflow at 1280/1440
- `Plumber` JSON-LD (no hours, no invented rating markup), canonical, robots.txt, sitemap.xml, OG image
- Unknown URLs return a real 404 (`serve dist` without `-s`, custom `404.html`)
- Screenshots in `shots/` (`python3 scripts/shoot.py <url> <prefix>`)

## Develop

```bash
npm install
npm run dev      # local dev server
npm run build    # outputs dist/
npm start        # serve dist on $PORT (default 3000)
```

Node 22.12+. Railway: Railpack build `npm run build`, start `npm start`; 0.25 vCPU / 0.25 GB, serverless sleep on, 1 replica.

See `docs/HANDOFF.md` for project status.
