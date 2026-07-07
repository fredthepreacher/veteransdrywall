# Veteran Drywall LLC — Project Notes

## Business facts
- Veteran Drywall LLC — Steven McPherson, President/Owner, USMC veteran (10+ yrs, 4 overseas deployments)
- North Port, FL 34286 (5390 Halkett Ter) · (941) 527-5924 (alt: (941) 929-3545) · info@veteransdrywall.net
- LIC # SCC131152687 · FL reg L22000144747 (inc. 2022)
- Service area: North Port, Port Charlotte, Venice, Sarasota, Englewood, Punta Gorda, Charlotte County, Sarasota County
- Team: Steven (owner), Mike, Rick
- Facebook: https://www.facebook.com/profile.php?id=61557745545101
- Production domain: https://veteransdrywall.net · temporary Netlify URL: https://veteransdrywall.netlify.app/
- Faith element: JOHN 15:13 — keep it on the logo and in the Why Us section.
- A DIFFERENT "Veteran Drywall" (Jason Miller, Port Charlotte) owns veterandrywall.**org** (singular, .org) and ranks on HomeAdvisor — never use their reviews/content; be aware when bidding branded search terms.

## ⚠️ Recurring issue: local project files keep disappearing between sessions
Twice now (2026-07-07, two separate points in the same day) the local project folder was found stripped down to just 1-2 files at the start of a session, even though the prior session had written a full deploy pack. The live Netlify deploy (https://veteransdrywall.netlify.app/) has been the reliable way to recover/verify actual site state — check it first if files look missing. This looks like something outside Claude's control (Claude's tools can't delete files in this workspace), possibly local cleanup on the user's machine. Worth keeping an eye on so real work isn't lost.

## Known important state as of 2026-07-07 (v2 pass)
- `index.html` is well ahead of the live Netlify deploy — **the live site needs a manual redeploy** (drag the folder into Netlify, or push if it's git-linked) to show: Choose Your Drywall Problem, Texture Matching, Water Damage, Veteran Standard, Property Manager/Realtor sections, and the expanded quote form fields.
- Logo: user provided two reference images (badge + horizontal lockup — flag/soldier/cross/John 15:13 with a full text stack incl. services, phone, "ONE STOP SHOP • FREE ESTIMATES", license) but they arrived as inline pasted images in chat, not file uploads, so Claude could not save/use the exact artwork. User agreed to re-attach as file uploads — **still pending** as of this note. Once attached, replace `logo.svg`/`logo-badge.svg`/`favicon.svg` with the real files (or a traced SVG of them).
- Images are still hotlinked to Wix. `self-host-images.sh` (project root) + `assets/images/README.md` have the exact download/rename plan — needs to be run from a machine with normal internet access (this sandbox blocks static.wixstatic.com and *.netlify.app outbound).
- See `changelog-2026-07-07-v2.md` for the full list of this pass's changes and remaining owner items.

## Decisions/history
- Single-page for now; will expand multi-page when client provides more content
- Before/after drag slider was built, then REMOVED at user request — don't re-add
- Real customer reviews not yet on site (waiting on genuine Google Business Profile link) — placeholder box is in the Reviews section
- User is a mid-level web designer learning daily — explain design choices at expert level
