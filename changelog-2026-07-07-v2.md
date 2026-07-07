# Veteran Drywall — Changelog v2 (2026-07-07, second pass)

## Deployment Fixes
- **Confirmed the live Netlify deploy (`https://veteransdrywall.netlify.app/`) is stale** — it's still serving the old page (old title, old chatbot starters, no Choose Your Drywall Problem / Texture Matching / Water Damage / Veteran Standard / Property Manager sections, old 7-option service dropdown). The local `index.html` has all of this correctly.
- Claude has no GitHub/Netlify connection in this session (no `.git` or `.netlify` folder present locally, and no credentials), so the deploy could not be triggered directly. Per your choice, **you'll redeploy manually** — drag the updated project folder into the Netlify dashboard (Sites → your site → Deploys → drag & drop), or push to your linked git repo if this site is git-connected. A Netlify MCP connector is available if you'd like Claude to check/trigger deploys directly in a future session — just say the word and approve the connection.
- Added `Cache-Control: public, max-age=0, must-revalidate` on `/*.html` specifically so this kind of staleness is less likely going forward (HTML always revalidates; only images/CSS/JS get the long cache).

## Logo Changes
- **Still pending your file upload.** The two reference images you posted (badge + horizontal lockup) render fine in chat but aren't accessible to Claude as files — this session's uploads folder is empty. Per your answer, please re-attach them using the file/upload control (not pasted inline) and Claude will swap them in as the real `logo.svg` / `logo-badge.svg` / `favicon.svg` next turn.
- In the meantime, the previous hand-drawn placeholder SVGs are still in place — not replaced yet, since building another guess before your real files arrive would just create a third version to throw away.

## UX/UI Improvements
- Header logo enlarged (46px → 60px desktop, 50px mobile) and the header bar heightened slightly (74px → 86px) to give it room.
- Footer logo: removed the `filter:invert(1) hue-rotate(180deg) saturate(0)` CSS trick — it was fighting the artwork's own colors. Footer logo now renders at its natural, larger size (64px) with no filter distortion.
- Mobile hero CTAs ("Get a Free Quote" / "Call Now") now stack full-width below 480px for cleaner, larger thumb targets instead of wrapping awkwardly.
- Added a visible category label chip (e.g. "Texture Matching," "Stucco") to every gallery photo, in addition to the existing hover caption — so the category is visible without hovering, especially useful on touch devices.
- Added a Call + Quote CTA pair at the end of the Texture Matching section and the Veteran Standard section — both major sections previously ended without a direct next step.
- Marquee strip now pauses on hover/focus instead of running continuously underneath the cursor.

## Performance Changes
- Replaced the CSS `background-image` hero with a `<picture>`/`<img>` element (AVIF source + JPG fallback) plus a separate absolutely-positioned gradient overlay div — same dark-overlay look, but the hero image is now a real, preloadable, priority-hinted image instead of a CSS background.
- Added `<link rel="preload" fetchpriority="high">` for the hero image and `<link rel="preconnect">` for `static.wixstatic.com`, so the largest-contentful-paint image starts loading immediately instead of after CSS parse.
- Hero image explicitly **not** lazy-loaded (no `loading="lazy"`, has `fetchpriority="high"` instead); every other image below the fold keeps `loading="lazy"` from the prior pass.
- Netlify cache headers strengthened: `public, max-age=31536000, immutable` added for SVG, WebP, AVIF, JPG/JPEG, PNG, CSS, JS, and a dedicated `/assets/*` rule — with HTML kept at `max-age=0, must-revalidate` so future deploys are never masked by stale caching.

## Image / Self-Hosting Changes
- Created `/assets/images/README.md` documenting the exact SEO-friendly target filenames for every image on the site (hero, 3 team photos, owner photo, 8 gallery photos).
- Wrote `self-host-images.sh` (project root) — a ready-to-run script that downloads every current Wix-hotlinked image and converts it to WebP with the correct filename, e.g. `north-port-drywall-repair-hero.webp`, `port-charlotte-texture-matching-project.webp`, `veteran-drywall-team-steven.webp`, `drywall-ceiling-repair-charlotte-county.webp`.
- **This could not be executed from Claude's sandbox** — its outbound network is allowlisted and blocks both `static.wixstatic.com` and `*.netlify.app`. The script needs to be run on a machine with normal internet access (yours, or a developer's), then `index.html`'s `static.wixstatic.com` src values swapped for the resulting `/assets/images/...` paths (every occurrence has a TODO comment marking it).
- `og:image` and the schema `image` field are still pointing at the Wix-hosted hero photo — flagged with a TODO to swap for a self-hosted 1200×630 crop once the images are local.

## SEO / Schema Changes
- Re-confirmed: zero remaining `veterandrywall.net` (typo) references anywhere in the project. All canonical/OG/schema/sitemap/robots references use `https://veteransdrywall.net`.
- `GeneralContractor` schema retains both phone numbers via `contactPoint`, email, expanded `areaServed` (incl. Charlotte & Sarasota County), `knowsAbout`/`makesOffer` covering texture matching, water damage, popcorn ceiling removal, and property-manager services, plus `sameAs` (Facebook). No hours, reviews, awards, or GBP link were added since none have been confirmed — per your instruction, nothing invented.

## Form / Chatbot Updates
- No changes this pass beyond what shipped in v1 (urgency, property type, photos-ready fields; expanded 11-option service dropdown; "No spam. No pressure..." reassurance copy) — all still intact and unbroken.
- SMS: left as-is. The form's existing "Text me" preferred-contact option was kept (it predates this pass and isn't a new claim), but no dedicated "Text Us" CTA button was added anywhere, since business SMS capability hasn't been explicitly confirmed.
- Netlify form, thank-you page, privacy page, and chatbot were not touched structurally this pass — verified still wired up correctly (form POSTs to `/thank-you.html`, honeypot field intact).

## Accessibility Improvements
- **Lightbox is now keyboard-operable end to end**: gallery photos are focusable (`tabindex="0"`, `role="button"`, descriptive `aria-label`) and open on Enter/Space, not just click.
- Added a focus trap inside the lightbox (Tab/Shift+Tab cycle among its three buttons instead of escaping to the page behind it), focus moves to the Close button on open, and returns to the exact photo that was activated when closed.
- Alt text rewritten across the gallery to be more descriptive (still truthful/general — no invented project specifics), e.g. "Drywall patch repair, finished and sanded smooth" instead of "Finished drywall project."
- `prefers-reduced-motion` now also disables the scroll-reveal fade/slide-up animation and shortens all transitions/animations site-wide, not just the marquee.
- Focus-visible outline now also applies to the new keyboard-focusable gallery items and `<summary>` (FAQ accordions).

## Remaining Items Needed From You
1. **Redeploy the live site** — drag this updated folder into Netlify (or push to git) so the new sections actually go live.
2. **Re-attach the two logo images as file uploads** (not pasted inline) so Claude can use the exact artwork instead of a hand-drawn approximation.
3. **Run `self-host-images.sh`** on a machine with normal internet access, then swap the `static.wixstatic.com` src values in `index.html` for the resulting `/assets/images/...` paths (marked with TODO comments).
4. Once self-hosted, update `og:image` and the schema `image` field to the new 1200×630 social image.
5. Google Business Profile link + real reviews, confirmed business hours, and confirmation of the "Insured" claim — still outstanding from the original build, still not fabricated.
6. Note: local project files (this changelog, `PROJECT-NOTES.md`, etc.) have twice been found missing at the start of a session even though the site files (`index.html` etc.) survived — worth keeping an eye on where/why that's happening on your end.
