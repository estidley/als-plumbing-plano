# Usage: python3 scripts/shoot.py <base_url> <prefix>
import sys, json
from playwright.sync_api import sync_playwright
base, prefix = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    for w, h, name in [(375, 812, "mobile-375"), (1280, 800, "desktop-1280"), (1440, 900, "desktop-1440")]:
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2 if w == 375 else 1)
        pg.goto(base, wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        info = pg.evaluate("""() => {
          const de = document.documentElement;
          const bodyFs = getComputedStyle(document.body).fontSize;
          const small = [...document.querySelectorAll('a,button')].filter(e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e); return r.width > 0 && s.visibility !== 'hidden' && s.display !== 'none' && r.height < 48 && !e.closest('p,dd') ; }).map(e => (e.textContent||'').trim().slice(0,30) + ' ' + Math.round(e.getBoundingClientRect().height));
          const imgsNoAlt = [...document.images].filter(i => !i.hasAttribute('alt')).length;
          const minFs = Math.min(...[...document.querySelectorAll('p,li,dd,blockquote,span,a')].filter(e=>e.offsetParent).map(e=>parseFloat(getComputedStyle(e).fontSize)));
          return { scrollWidth: de.scrollWidth, clientWidth: de.clientWidth, bodyFs, small, imgsNoAlt, minFs,
                   title: document.title, h1: document.querySelector('h1').textContent,
                   canonical: document.querySelector('link[rel=canonical]')?.href,
                   dock: getComputedStyle(document.querySelector('.dock')).display };
        }""")
        print(name, json.dumps(info))
        pg.screenshot(path=f"shots/{prefix}{name}-top.png")
        pg.screenshot(path=f"shots/{prefix}{name}-full.png", full_page=True)
        pg.close()
    b.close()
