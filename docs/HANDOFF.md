# Al's Plumbing (Plano, TX): lead demo handoff

This project is the weekly lead demo for the week of Nov 9, 2026: a mobile-first, single-page marketing site for Al's Plumbing, a real Plano plumber (Google Maps listing "Al's Plumbing", owner credit "Al's Plumbing, Heating & Air Conditioning", BBB legal name Al's Plumbing Company, Inc.) at 1108 Summit Ave #5, Plano, TX 75074, phone (972) 422-7301. It is canonical sheet row 73 ("No-Website Business Leads", tab Untitled), originally the Nov 2 pick, and Ethan chose it on Nov 9 as this week's only site. The site presents the business's services (water heaters, drains and sewer, slab leaks and leak detection, gas lines, valves/disposals/shower pans, heating and A/C) using only verified facts: 4.6★ from 198 Google reviews, A+ BBB rating and a 1993 start date (both from BBB's public profile), and six verbatim positive Google reviews with names and relative ages, including the one naming technician Art. Because the listing has no hours, the site says "Call to confirm hours"; there are no prices, forms or booking backend, only call-to-book and call-for-pricing. No logo or usable photos exist publicly (only a 2014 Street View of an unsigned suite and a low-resolution 2016 banner graphic), so the design is typographic: a text wordmark plus icons, with the palette sampled from that banner. The site is a Vite static build served by `serve`, in a new public GitHub repo (estidley/als-plumbing-plano), deployed to a new Railway project at 0.25 vCPU / 0.25 GB with serverless sleep on and one replica. The sheet update (I/J/K/L) and telling Ethan/Fred are separate steps outside this repo's build.

## Ethan's instructions and project goal

- One lead demo site per week; this week Ethan explicitly picked Al's Plumbing (Nov 9, 2026).
- Mobile-first. Fresh, modern, crisp and uncrowded; Ethan's favorites are Fresh Me Up (black and white) and the black-and-gold barber demo. Distinct from earlier demos, not a reskin.
- Use the real business's colors and logo from its Maps photos/signage/trucks/uniforms; no invented themes. Show where each color came from. Check 2–3 competitor sites and do better.
- Use real reviews and photos; never invent facts, hours, prices, staff, certifications or quotes.
- New public repo under estidley; Railway at 0.25 vCPU / 0.25 GB, serverless sleep on, 1 replica (size up only if it fails to start).
- Footer disclaimer that it's an independent demo. Don't contact the business. Don't create a second leads list.
- Sheet row: I = Demo live, J = Review Count (198), K = repo URL, L = Railway URL (done in a separate step).
- Goal: a demo good enough to show the owner what a modern site would look like, with clearer trust signals and stronger social proof than local competitors.

## Palette note

| Color | Hex | Source |
| --- | --- | --- |
| Navy | `#13254A` | Deepened from the blue label bars of the owner's 2016 "Plumbing / Heating / Cooling" banner on Google Maps |
| Banner blue | `#3B62B0` | Sampled from those label bars; used for links, icons and the desktop hero's Plumbing/Heating/Cooling bars |
| Yellow | `#F2D21B` | Sampled from the yellow gauge in the banner's "Cooling" panel; used sparingly for CTAs and accents |
| Cool grey | `#4A5466` | From the technician's grey uniform shirt in the banner's "Heating" panel; secondary text |
| White / tint | `#FFFFFF` / `#F3F5F9` | Banner's white background |

No logo exists publicly (a tiny red/white/blue avatar on the owner credit is unreadable), so the wordmark is plain Archivo type, not a recreated logo. Banner panels were too low-resolution to use as images.

Competitors checked (Nov 9, Google "plumber Plano TX"):
1. Baker Brothers (bakerbrothersplumbing.com/plano-plumbing/): strong header CTAs and trust badges, but busy and text-heavy. Our answer: one compact four-item proof strip, less copy.
2. Legacy Plumbing (legacyplumbing.net/plano/): clear guarantee bullets, but promo-banner clutter and long text. Our answer: no promos, short service rows.
3. Plano Plumbing TX (planoplumbingtx.com): simple, but dated with little social proof and a captcha form. Our answer: featured review, three review themes, five more verbatim reviews, call-only contact.

## Checklist

Done:
- [x] Read Nov 9 research (`/workspace/als-plumbing/research/`), migration handoff and Old Town reference build.
- [x] Confirmed A+ BBB rating and 1993 start on BBB's public profile (via search index of bbb.org; the direct page fetch timed out).
- [x] Built site: hero, proof strip, services, reviews (verbatim), contact, footer disclaimer, sticky mobile Call/Directions dock, custom 404.
- [x] Plumber JSON-LD (no hours, no aggregateRating), canonical, robots.txt, sitemap.xml, OG image, title differs from H1.
- [x] Unknown URLs return 404 (`serve dist`, no `-s`; single-page site needs no SPA fallback).
- [x] Playwright at 375 / 1280 / 1440: no horizontal overflow, 17px body, tap targets ≥48px; screenshots in `shots/`.
- [x] Railway project `als-plumbing-plano` (7a92aa0a-9253-4a7e-a9f9-1a2684497500), service d7917918-91c6-4c33-8fca-2c854159a967, domain https://als-plumbing-plano-production.up.railway.app; 0.25 vCPU / 0.25 GB, sleep on, 1 replica.
- [x] Public repo https://github.com/estidley/als-plumbing-plano.

Left (outside this repo's scope):
- [ ] Sheet row 73: I = Demo live, J = 198, K = repo URL, L = Railway URL.
- [ ] Reply to Fred with links and palette note; tell Ethan the result.
- [ ] Optional: a Figma mobile frame if Ethan wants one (not made this run).
- [ ] Optional: connect the Railway service to the GitHub repo for auto-deploys (currently deployed with `railway up`).
