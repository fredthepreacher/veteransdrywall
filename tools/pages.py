# -*- coding: utf-8 -*-
"""Bespoke pages: home, cost guide, about, FAQ, free estimate, privacy, thank-you, 404."""
import json
from content import *  # noqa

HOME_TITLE = 'Drywall Repair & Texture Matching North Port FL | Veteran Drywall'
HOME_DESC = 'USMC veteran-owned drywall repair in North Port, FL: texture matching, water & storm damage, ceilings, popcorn removal. Serving Sarasota & Charlotte County.'

GALLERY = [
 ('crew', 'Crew at work', '/assets/images/gallery-square-webp/drywall-window-scaffold-finishing-project-square-900.webp', '/assets/images/jpg-fallbacks/drywall-window-scaffold-finishing-project.jpg', 'Veteran Drywall finisher sanding new drywall around an arched window from a scaffold', 'Hang & finish around an arched window'),
 ('repairs', 'Repairs', None, 'https://static.wixstatic.com/media/e64608_cdfda03a4f6948f5bab48a8df4e4171d~mv2.jpeg/v1/fit/w_960,h_960,q_90,enc_avif,quality_auto/e64608_cdfda03a4f6948f5bab48a8df4e4171d~mv2.jpeg', 'Ceiling drywall patch repair, finished and sanded smooth', 'Ceiling drywall repair & finishing'),
 ('repairs', 'Repairs', None, 'https://static.wixstatic.com/media/e64608_c2bdd0b4b08641f79dbd3b66a48d945e~mv2.jpeg/v1/fit/w_960,h_960,q_90,enc_avif,quality_auto/e64608_c2bdd0b4b08641f79dbd3b66a48d945e~mv2.jpeg', 'New drywall hung and taped during an interior project', 'Interior drywall finishing'),
 ('texture', 'Texture', None, 'https://static.wixstatic.com/media/e64608_58ca186cb9cb41db98441e75e91643d3~mv2.png/v1/fit/w_960,h_960,q_90,enc_avif,quality_auto/e64608_58ca186cb9cb41db98441e75e91643d3~mv2.png', 'Close-up of a drywall texture matching detail', 'Texture matching detail'),
 ('painting', 'Painting', '/assets/images/gallery-square-webp/interior-painting-drywall-finishing-square-900.webp', '/assets/images/jpg-fallbacks/interior-painting-drywall-finishing.jpg', 'Veteran Drywall crew member rolling paint on a finished wall', 'Finish coat after drywall repair'),
 ('painting', 'Painting', None, 'https://static.wixstatic.com/media/e64608_5808502a2bc3433cbb114d5d7a08c541~mv2.jpeg/v1/fit/w_960,h_960,q_90,enc_avif,quality_auto/e64608_5808502a2bc3433cbb114d5d7a08c541~mv2.jpeg', 'Large room drywall finishing and surface prep', 'Large-room finishing & prep'),
 ('remodels', 'Remodels', '/assets/images/gallery-square-webp/interior-remodel-framing-prep-square-900.webp', '/assets/images/jpg-fallbacks/interior-remodel-framing-prep.jpg', 'Interior remodel with exposed framing ready for new drywall', 'Remodel framing prep'),
 ('stucco', 'Stucco', None, 'https://static.wixstatic.com/media/e64608_85da5961321a4b1580295432f77a58dc~mv2.jpeg/v1/fit/w_960,h_960,q_90,enc_avif,quality_auto/e64608_85da5961321a4b1580295432f77a58dc~mv2.jpeg', 'Exterior stucco repair matched to existing texture', 'Stucco & exterior work'),
 ('repairs', 'Ceilings', None, 'https://static.wixstatic.com/media/e64608_fe8282cedfc643fba95f606a19c3440e~mv2.jpeg/v1/fit/w_960,h_960,q_90,enc_avif,quality_auto/e64608_fe8282cedfc643fba95f606a19c3440e~mv2.jpeg', 'Drywall ceiling repair with texture blended in', 'Ceiling repair, texture blended'),
]

def home_page(x):
    ic, e = x['ic'], x['e']
    nodes = x['webpage_node']('/', HOME_TITLE, HOME_DESC, None)
    nodes.append(x['faq_node']('/', GENERAL_FAQS[:8]))
    preload = '<link rel="preload" as="image" href="/assets/images/webp/veteran-drywall-crew-mobile-900x1200.webp" type="image/webp" fetchpriority="high">\n'
    out = x['head']('/', HOME_TITLE, HOME_DESC, x['graph'](nodes), preload=preload) + x['header']()

    tiles = ''.join(f'<button class="ptile{" " if True else ""}" type="button" data-key="{k}" aria-pressed="{"true" if i == 0 else "false"}">{ic(icn)}<b>{e(lbl)}</b></button>' for i, (k, lbl, icn) in enumerate(PICKER_ORDER))
    p0 = PICKER['hole']
    bento = f'''
      <a class="bcard feature reveal" href="/water-damage-drywall-repair/">
        <div class="bimg"><picture><source type="image/webp" srcset="/assets/images/webp/interior-remodel-framing-prep.webp"><img src="/assets/images/jpg-fallbacks/interior-remodel-framing-prep.jpg" alt="Wall opened to the studs during a water-damage rebuild" width="574" height="416" loading="lazy"></picture></div>
        <div class="binner"><span class="tagline">Storm &amp; leak repair</span><h3>Water &amp; storm damage</h3><p>Leaks, AC overflows, flood cuts and hurricane damage — rebuilt, finished and texture-matched once it’s dry.</p><span class="go">See how we rebuild <i>→</i></span></div>
      </a>
      <a class="bcard gold span-3 reveal" href="/texture-matching/"><span class="bicon">{ic('dots')}</span><span class="tagline">Our specialty</span><h3>Texture matching</h3><p>Knockdown, orange peel, skip trowel, popcorn, smooth. Repairs that vanish.</p><span class="go">Match my texture <i>→</i></span></a>
      <a class="bcard span-3 reveal" href="/drywall-repair/"><span class="bicon">{ic('hole')}</span><h3>Drywall repair</h3><p>Holes, cracks, nail pops, dents. No job too small.</p><span class="go">Fix a hole <i>→</i></span></a>
      <a class="bcard navy span-2 reveal" href="/popcorn-ceiling-removal/"><span class="bicon">{ic('popcorn')}</span><h3>Popcorn removal</h3><p>Scrape, skim &amp; refinish — smooth or textured.</p><span class="go">Modernize <i>→</i></span></a>
      <a class="bcard span-2 reveal" href="/ceiling-repair/"><span class="bicon">{ic('ceiling')}</span><h3>Ceiling repair</h3><p>Cracks, sags, stains &amp; nail pops.</p><span class="go">Fix my ceiling <i>→</i></span></a>
      <a class="bcard span-2 reveal" href="/new-construction-drywall/"><span class="bicon">{ic('house')}</span><h3>New drywall</h3><p>Remodels, additions &amp; new builds to paint-ready.</p><span class="go">Plan a project <i>→</i></span></a>
      <a class="bcard span-2 reveal" href="/stucco-repair/"><span class="bicon">{ic('trowel')}</span><h3>Stucco</h3><p>Exterior cracks &amp; patches, matched.</p><span class="go">Stucco repair <i>→</i></span></a>
      <a class="bcard span-2 reveal" href="/painting-trim/"><span class="bicon">{ic('roller')}</span><h3>Paint &amp; trim</h3><p>The finishing touches — one crew.</p><span class="go">Paint &amp; trim <i>→</i></span></a>
      <a class="bcard navy span-2 reveal" href="/property-managers/"><span class="bicon">{ic('clipboard')}</span><h3>Punch lists</h3><p>For landlords, PMs &amp; realtors.</p><span class="go">Turnover help <i>→</i></span></a>'''
    gal = ''
    for cat, lbl, webp, fb, alt, cap in GALLERY:
        src = f'<picture><source type="image/webp" srcset="{webp}"><img src="{fb}" alt="{e(alt)}" width="900" height="900" loading="lazy" decoding="async"></picture>' if webp else f'<img src="{fb}" alt="{e(alt)}" width="960" height="960" loading="lazy" decoding="async">'
        gal += f'<figure data-cat="{cat}" class="reveal"><span class="gcat">{lbl}</span>{src}<figcaption>{e(cap)}</figcaption></figure>'
    areas = ''.join(f'<a class="area reveal{" home" if c["slug"] == "north-port-fl" else ""}" href="/areas/{c["slug"]}/"><b>{e(c["name"])}</b><small>{"Home base · " if c["slug"] == "north-port-fl" else ""}{e(c["county"])}</small></a>' for c in CITIES)

    out += f'''<main id="main">
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow on-dark">USMC veteran owned · North Port, FL</span>
      <h1 class="split-words">Drywall repair in North Port that <span class="hl">disappears.</span></h1>
      <p class="sub">Holes, cracks, water-stained ceilings, popcorn and full remodels — patched, <strong style="color:#fff">texture-matched</strong> and finished by a Marine-led crew across Sarasota &amp; Charlotte County.</p>
      <div class="ticker" aria-hidden="true"><span class="pulse-dot"></span><span class="tk-label">Now fixing:</span><span class="tk-word" data-words="doorknob holes|ceiling stains|storm damage|popcorn ceilings|knockdown texture|nail pops">doorknob holes</span></div>
      <div class="btn-row">
        <a class="btn btn-gold btn-lg" href="/free-estimate/" data-quote>{ic('camera')} Get my free estimate</a>
        <a class="btn btn-outline btn-lg" href="tel:{BIZ['phone_e164']}">{ic('phone')} {BIZ['phone']}</a>
      </div>
      <div class="hero-trust">
        <span>{ic('flag')}USMC veteran owned</span>
        <span>{ic('shield')}FL Lic. # {BIZ['license']}</span>
        <span>{ic('check')}Small jobs welcome</span>
        <span>{ic('star')}Free written estimates</span>
      </div>
    </div>
    <div class="hero-visual">
      <div class="hero-card">
        <picture>
          <source type="image/webp" srcset="/assets/images/webp/veteran-drywall-crew-mobile-900x1200.webp">
          <img src="/assets/images/jpg-fallbacks/veteran-drywall-crew-hero.jpg" alt="Steven, Mike and Rick — the Veteran Drywall crew — standing outdoors in North Port, Florida" width="900" height="1200" fetchpriority="high">
        </picture>
        <div class="cap"><div><b>Steven, Mike &amp; Rick</b><small>One crew · estimate to walkthrough</small></div></div>
      </div>
      <a class="float-chip fc-1" href="https://www.myfloridalicense.com/wl11.asp" target="_blank" rel="noopener"><span class="fc-ic">{ic('shield')}</span><span>Licensed in Florida<small>SCC131152687 · verify ↗</small></span></a>
      <div class="float-chip fc-2"><span class="fc-ic">{ic('phone')}</span><span>Owner answers<small>his own phone</small></span></div>
      <div class="float-chip fc-3"><span class="fc-ic">{ic('dots')}</span><span>Texture matched<small>so repairs vanish</small></span></div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">
  {''.join('<span>' + w + '</span>' for w in ['Drywall repair','Texture matching','Water damage','Storm repair','Ceiling repair','Popcorn removal','Stucco','Paint & trim','Remodels','Punch lists']*2)}
</div></div>

<section class="section" id="diagnose">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">60-second diagnosis</span>
      <h2 class="h-lg">What’s wrong with <span class="hl-under">your wall?</span></h2>
      <p class="lede">Tap what you’re looking at. We’ll tell you what it’s called, how we fix it and what it typically costs — then you can send it to us in one tap.</p>
    </div>
    <div class="picker">
      <div class="picker-tiles stagger">{tiles}</div>
      <div class="pick-panel" id="pickPanel" aria-live="polite">
        <div class="pp-body">
          <span class="pp-tag">{e(p0['tag'])}</span>
          <h3>{e(p0['title'])}</h3>
          <p class="pp-desc">{e(p0['desc'])}</p>
          <ul class="pp-steps">{''.join('<li>' + e(s) + '</li>' for s in p0['steps'])}</ul>
          <div class="pp-meta"><div><small>Typical timeline</small><b class="pp-time">{e(p0['time'])}</b></div><div><small>Ballpark</small><b class="pp-cost">{e(p0['cost'])}</b></div></div>
          <div class="btn-row"><a class="btn btn-gold pp-go" href="/free-estimate/" data-quote data-service="{e(p0['service'])}">Get this fixed →</a><a class="link-arrow pp-more" href="{p0['url']}">Read the full {e(p0['short'])} guide</a></div>
          <p class="pp-note">Ballparks are national averages from <a href="{HG_REPAIR}" target="_blank" rel="noopener">HomeGuide</a>, not quotes. Your written estimate is free.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section paper" id="services">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">What we do</span><h2 class="h-lg">One crew. Wall to wall.</h2><p class="lede">From a single doorknob hole to a whole-house rebuild after a storm — no subcontractor roulette, no hand-offs.</p></div>
    <div class="bento">{bento}</div>
  </div>
</section>

<section class="section dark grain" id="texture">
  <div class="wrap lab">
    <div>
      <span class="eyebrow on-dark">Texture lab</span>
      <h2 class="h-lg">Drag it. Watch the patch <span class="hl">disappear.</span></h2>
      <p class="lede">A patch without texture sticks out like a sore thumb. Pick your texture and slide to see the difference a proper match makes.</p>
      <div class="tex-tabs" role="tablist" aria-label="Choose a texture">
        <button class="tex-tab" role="tab" type="button" data-tex="knockdown" aria-selected="true">Knockdown</button>
        <button class="tex-tab" role="tab" type="button" data-tex="orangepeel" aria-selected="false">Orange peel</button>
        <button class="tex-tab" role="tab" type="button" data-tex="skiptrowel" aria-selected="false">Skip trowel</button>
        <button class="tex-tab" role="tab" type="button" data-tex="popcorn" aria-selected="false">Popcorn</button>
        <button class="tex-tab" role="tab" type="button" data-tex="smooth" aria-selected="false">Smooth</button>
      </div>
      <p class="tex-desc">{e(TEXTURES['knockdown'])}</p>
      <div class="btn-row" style="margin-top:20px"><a class="btn btn-gold" href="/free-estimate/" data-quote data-service="Texture Matching">Match my texture</a><a class="link-arrow" href="/texture-matching/">How we match it</a></div>
    </div>
    <div class="compare reveal" aria-label="Before and after texture matching illustration">
      <div class="layer after tx-knockdown"></div>
      <div class="layer before tx-knockdown"><div class="patch"></div></div>
      <span class="lbl l">Typical patch</span><span class="lbl r">Veteran Drywall</span>
      <div class="handle" aria-hidden="true"></div>
      <input type="range" min="0" max="100" value="50" aria-label="Slide to compare an unmatched patch with a texture-matched repair">
      <span class="illus">Illustration</span>
    </div>
  </div>
</section>

<section class="section" id="why">
  <div class="wrap">
    <div class="story">
      <div class="story-media reveal">
        <div class="m1"><picture><source type="image/webp" srcset="/assets/images/team/steven-mcpherson-full-body-portrait-fill.webp"><img src="/assets/images/team/steven-mcpherson-full-body-portrait-fill.jpg" alt="Steven McPherson, owner of Veteran Drywall" width="1024" height="1536" loading="lazy"></picture></div>
        <div class="m2"><picture><source type="image/webp" srcset="/assets/images/webp/usmc-veteran-service-photo-american-flag.webp"><img src="/assets/images/jpg-fallbacks/usmc-veteran-service-photo-american-flag.jpg" alt="Steven’s U.S. Marine Corps unit holding an American flag during deployment" width="574" height="416" loading="lazy"></picture></div>
        <span class="badge">Semper Fi</span>
      </div>
      <div>
        <span class="eyebrow">Why Veteran Drywall</span>
        <h2 class="h-lg">Discipline you can see in the finish.</h2>
        <p>Veteran Drywall is owned and led by <strong>Steven McPherson</strong> — a United States Marine with more than a decade of service and four overseas deployments. The Corps taught him that details decide outcomes: show up on time, do it right the first time, never leave a job half done.</p>
        <p>That standard runs through every wall we hang and every texture we match. You get <strong>Steven, Mike and Rick</strong> — one accountable crew from estimate to walkthrough.</p>
        <div class="verse"><q>Greater love hath no man than this, that a man lay down his life for his friends.</q><small>JOHN 15:13</small></div>
        <div class="btn-row" style="margin-top:24px"><a class="btn btn-dark" href="/about/">Meet the crew</a><a class="link-arrow" href="https://www.myfloridalicense.com/wl11.asp" target="_blank" rel="noopener">Verify our license</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight dark" aria-label="By the numbers">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><b data-count="10" data-suffix="+">10+</b><span>Years USMC service</span></div>
      <div class="stat"><b data-count="4">4</b><span>Overseas deployments</span></div>
      <div class="stat"><b data-count="6">6</b><span>Cities served</span></div>
      <div class="stat"><b data-count="1">1</b><span>Standard: done right</span></div>
    </div>
  </div>
</section>

<section class="section" id="process">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">The Veteran Standard</span><h2 class="h-lg">Four steps. Zero runaround.</h2></div>
    <div class="timeline">
      <span class="tl-fill" aria-hidden="true"></span>
      <div class="tl-step"><span class="n">1</span><h3>Mission brief</h3><p>Send photos or we come look. You get a straight answer and a written estimate — free.</p></div>
      <div class="tl-step"><span class="n">2</span><h3>Site protection</h3><p>Floors, furniture and vents covered before anything gets cut or sanded.</p></div>
      <div class="tl-step"><span class="n">3</span><h3>Precision finish</h3><p>Tape, coats, sanding and texture done with patience — Florida humidity doesn’t get rushed.</p></div>
      <div class="tl-step"><span class="n">4</span><h3>Final walkthrough</h3><p>We walk it with you. It’s not done until it meets the standard we’d demand in our own homes.</p></div>
    </div>
  </div>
</section>

<section class="section paper" id="work">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Our work</span><h2 class="h-lg">Proof is in the finish.</h2></div>
    <div class="filters" role="group" aria-label="Filter project photos">
      <button class="filter" type="button" data-filter="all" aria-pressed="true">All</button>
      <button class="filter" type="button" data-filter="repairs" aria-pressed="false">Repairs &amp; ceilings</button>
      <button class="filter" type="button" data-filter="texture" aria-pressed="false">Texture</button>
      <button class="filter" type="button" data-filter="painting" aria-pressed="false">Painting</button>
      <button class="filter" type="button" data-filter="remodels" aria-pressed="false">Remodels</button>
      <button class="filter" type="button" data-filter="stucco" aria-pressed="false">Stucco</button>
      <button class="filter" type="button" data-filter="crew" aria-pressed="false">Crew at work</button>
    </div>
    <!-- TODO (owner): 6 photos below are still hotlinked from Wix. Export the originals and they'll be self-hosted. -->
    <div class="gallery stagger">{gal}</div>
  </div>
</section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Project photo viewer">
  <button class="lb-btn lb-close" type="button" aria-label="Close">×</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous photo">‹</button>
  <img id="lbImg" src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" alt="">
  <button class="lb-btn lb-next" type="button" aria-label="Next photo">›</button>
  <p id="lbCap"></p>
</div>

<section class="section" id="team">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">The crew</span><h2 class="h-lg">Three guys. One standard.</h2><p class="lede">No revolving door of subs. The people who quote your job are the people who do it.</p></div>
    <div class="team stagger">
      <div class="member reveal"><picture><source type="image/webp" srcset="/assets/images/team/steven-mcpherson-full-body-portrait-fill.webp"><img src="/assets/images/team/steven-mcpherson-full-body-portrait-fill.jpg" alt="Steven McPherson, owner of Veteran Drywall" width="1024" height="1536" loading="lazy"></picture><div class="mi"><span>Owner · USMC veteran</span><h3>Steven McPherson</h3></div></div>
      <div class="member reveal"><picture><source type="image/webp" srcset="/assets/images/team/mike-veteran-drywall-full-body-portrait-fill.webp"><img src="/assets/images/team/mike-veteran-drywall-full-body-portrait-fill.jpg" alt="Mike, Veteran Drywall crew member" width="1024" height="1536" loading="lazy"></picture><div class="mi"><span>Veteran Drywall crew</span><h3>Mike</h3></div></div>
      <div class="member reveal"><picture><source type="image/webp" srcset="/assets/images/team/rick-veteran-drywall-full-body-portrait-fill.webp"><img src="/assets/images/team/rick-veteran-drywall-full-body-portrait-fill.jpg" alt="Rick, Veteran Drywall crew member" width="1024" height="1536" loading="lazy"></picture><div class="mi"><span>Veteran Drywall crew</span><h3>Rick</h3></div></div>
    </div>
  </div>
</section>

<section class="section dark grain">
  <div class="wrap split">
    <div>
      <span class="eyebrow on-dark">Property managers · landlords · realtors</span>
      <h2 class="h-lg">Turnovers done. <span class="hl">Units rent-ready.</span></h2>
      <p class="lede">Tenant damage, move-out punch lists, listing prep and inspection items — one reliable crew that communicates and documents.</p>
      <ul class="checklist cols"><li>Tenant damage</li><li>Move-out repairs</li><li>Listing prep</li><li>Inspection items</li><li>Ceiling stains</li><li>Before/after photos</li></ul>
      <div class="btn-row" style="margin-top:26px"><a class="btn btn-gold" href="/free-estimate/?service=Property+Manager+%2F+Realtor+%2F+Landlord+Service" data-quote data-service="Property Manager / Realtor / Landlord Service">Send my punch list</a><a class="link-arrow" href="/property-managers/">How it works</a></div>
    </div>
    <div class="card reveal">
      <h3 class="h-sm" style="color:#fff">Straight talk, in writing</h3>
      <p style="color:rgba(246,241,230,.8);margin-top:10px">Send the address list, walkthrough photos or the inspection report. You get an itemized quote owners can understand — and license documentation for HOAs on request.</p>
      <div class="answer" style="margin-top:18px"><strong>Do you work with property managers?</strong>Yes. Veteran Drywall LLC regularly handles tenant-damage repairs, move-out punch lists and listing prep across North Port, Port Charlotte and the surrounding area.</div>
    </div>
  </div>
</section>

<section class="section" id="cost">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Know before you call</span>
      <h2 class="h-lg">What does drywall repair cost?</h2>
      <p class="lede">We price every job after seeing it, and estimates are free. But you deserve a ballpark — so here are the national averages, straight.</p>
      <div class="btn-row" style="margin-top:22px"><a class="btn btn-dark" href="/drywall-repair-cost/">Read the full cost guide</a></div>
    </div>
    <div class="reveal">{cost_table([('Small hole (under 4")', '$300 – $500', 'Minimum job charge + texture'), ('Large hole', '$500 – $800+', 'Size, blocking, texture'), ('Ceiling repair', '$350 – $1,500+', 'Height, leak damage'), ('Popcorn removal + refinish', '$2 – $6 / sq ft', 'Smooth vs. textured')], caption=f'National averages · <a href="{HG_REPAIR}" target="_blank" rel="noopener">HomeGuide</a> (updated Oct 2025). Not a quote.')}</div>
  </div>
</section>

<section class="section paper" id="reviews">
  <div class="wrap proof">
    <div class="card reveal">
      <span class="eyebrow">Word of mouth</span>
      <h3>Our neighbors vouch for us.</h3>
      <p style="color:var(--muted);margin-top:10px">See project photos, updates and what customers across North Port and Port Charlotte say on our Facebook page. Worked with us? A quick review there helps another local family find a crew they can trust.</p>
      <div class="btn-row" style="margin-top:20px"><a class="btn btn-dark" href="{BIZ['facebook']}" target="_blank" rel="noopener">{ic('fb')} See us on Facebook</a></div>
      <!-- TODO (owner): add Google Business Profile review link + real, permissioned reviews here. Never invent reviews or ratings. -->
    </div>
    <div class="card card-gold reveal">
      <span class="eyebrow" style="color:var(--navy-700)">Verified, not claimed</span>
      <h3>Check us out yourself.</h3>
      <ul class="checklist"><li>FL license # {BIZ['license']}</li><li>USMC veteran owned &amp; operated</li><li>Local — based in North Port 34286</li><li>Free written estimates</li></ul>
      <a class="btn btn-dark" style="margin-top:20px" href="https://www.myfloridalicense.com/wl11.asp" target="_blank" rel="noopener">Verify license on DBPR ↗</a>
    </div>
  </div>
</section>

<section class="section dark" id="areas">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow on-dark">Where we work</span><h2 class="h-lg">Serving Sarasota &amp; Charlotte County.</h2><p class="lede">Based in North Port. If your town isn’t listed but it’s close, call — we can usually make it work.</p></div>
    <div class="areas stagger">{areas}</div>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Straight answers</span><h2 class="h-lg">Frequently asked.</h2></div>
    {x['faq_html'](GENERAL_FAQS[:8])}
    <p style="margin-top:20px"><a class="link-arrow" href="/faq/">All questions &amp; answers</a></p>
  </div>
</section>

{x['quote_section']()}
</main>
<script>window.VD_PICKER={json.dumps(PICKER, ensure_ascii=False)};window.VD_TEXTURES={json.dumps(TEXTURES, ensure_ascii=False)};</script>
''' + x['footer']()
    x['write']('/', out)


def cost_page(x):
    ic, e = x['ic'], x['e']
    path = '/drywall-repair-cost/'
    title = 'Drywall Repair Cost 2026: SW Florida Price Guide'
    desc = 'What drywall repair costs in 2026: holes, cracks, ceilings, texture and popcorn removal — cited national ranges plus what changes the price in SW Florida.'
    crumbs = [('Home', '/'), ('Drywall repair cost', path)]
    faqs = [
     ('How much does it cost to fix a small hole in drywall?', 'Nationally, about $300–$500 for a small hole under 4 inches, according to HomeGuide. Most of that is the contractor’s minimum trip and job charge plus texture matching and multiple coats — which is why bundling several small repairs into one visit saves money.'),
     ('How much does ceiling drywall repair cost?', 'National averages run $350–$1,500+, depending on the size of the damage, ceiling height, texture and whether a leak caused it.'),
     ('How much does popcorn ceiling removal cost?', 'About $1–$2 per square foot for removal only, or $2–$6 per square foot including new texture and paint. Asbestos testing for older homes runs $250–$850 (HomeGuide).'),
     ('Is it cheaper to repair or replace drywall?', 'Small holes and cracks are almost always cheaper to repair. Replacement makes sense when drywall is soft, swollen, moldy or badly stained from water, or when damage covers most of a sheet.'),
     ('Why do drywall repairs cost more than the materials?', 'Materials are cheap; the cost is skilled labor and time. Joint compound needs multiple coats with drying time between them, plus sanding, texture matching and priming — and each return visit is labor.'),
     ('Do you charge for estimates?', 'No. Veteran Drywall estimates are free. Send photos for the fastest turnaround.'),
    ]
    nodes = x['webpage_node'](path, title, desc, crumbs, ptype='WebPage')
    nodes.append({"@type": "Article", "@id": SITE + path + "#article", "headline": "Drywall Repair Cost in 2026: A Southwest Florida Guide", "description": desc,
                  "datePublished": x['BUILD_DATE'], "dateModified": x['BUILD_DATE'], "author": {"@id": SITE + "/#business"}, "publisher": {"@id": SITE + "/#business"},
                  "mainEntityOfPage": {"@id": SITE + path + "#webpage"}, "image": SITE + "/assets/images/og/veteran-drywall-og-v11.jpg",
                  "citation": [HG_REPAIR, HG_POPCORN]})
    nodes.append(x['faq_node'](path, faqs))
    out = x['head'](path, title, desc, x['graph'](nodes)) + x['header']('cost')
    out += x['page_hero'](crumbs, 'Cost guide · updated Sept 2026', 'Drywall repair cost: <span class="hl">the straight numbers.</span>',
                          'What drywall repair, ceiling work, texture matching and popcorn removal typically cost — and what actually moves the price in North Port, Port Charlotte and the rest of Southwest Florida.',
                          extra='<p class="updated">Updated September 25, 2026 · Figures cited from HomeGuide (Oct 2025) · Not a quote</p>')
    out += f'''<section class="section"><div class="wrap content-grid">
  <article class="prose">
    <div class="answer reveal"><strong>Quick answer</strong>Nationally, drywall repair typically costs <b>$300–$1,500+</b> per job. Small holes run about <b>$300–$500</b>, large holes <b>$500–$800+</b>, cracks <b>$350–$1,000+</b> and ceiling repairs <b>$350–$1,500+</b>. Larger sections run <b>$3–$8 per square foot</b>, and popcorn ceiling removal with refinishing runs <b>$2–$6 per square foot</b> (HomeGuide). Your exact price depends on size, texture, height and access — Veteran Drywall estimates are free.</div>
    <h2>Drywall repair cost by job</h2>
    {cost_table([
      ('Small hole (under 4")', '$300 – $500', 'Minimum job charge, texture match, paint'),
      ('Large hole', '$500 – $800+', 'Size, blocking/backing, texture'),
      ('Crack repair', '$350 – $1,000+', 'Length, cause, wall vs. ceiling'),
      ('Ceiling repair', '$350 – $1,500+', 'Height, leak damage, texture'),
      ('Larger sections / full sheets', '$3 – $8 / sq ft', 'Area, finish level, access'),
      ('Taping, mudding & finishing', '$1.50 – $3.50 / sq ft', 'Level 4 vs. Level 5'),
      ('Texturing', '$0.80 – $2.00+ / sq ft', 'Matching existing costs more'),
      ('Interior painting', '$2 – $8+ / sq ft', 'Prep, coats, ceilings'),
      ('Typical minimum job', '$350 – $650+', 'Trip + setup + multiple visits'),
      ('Labor (hourly)', '$60 – $150 / hr', 'Contractor vs. handyperson')])}
    <h2>Popcorn ceiling removal cost</h2>
    {cost_table([
      ('Removal only', '$1 – $2 / sq ft', 'Painted popcorn is slower'),
      ('Removal + texture + paint', '$2 – $6 / sq ft', 'Smooth costs more than knockdown'),
      ('500 sq ft of ceiling', '$1,000 – $3,000', 'Rooms, furniture, height'),
      ('1,000 sq ft of ceiling', '$2,000 – $6,000', ''),
      ('1,500 sq ft of ceiling', '$3,000 – $9,000', ''),
      ('Asbestos testing', '$250 – $850', 'Recommended for older homes'),
      ('Asbestos abatement (if positive)', '$4 – $20 / sq ft', 'Licensed abatement contractor')], caption=f'National averages from <a href="{HG_POPCORN}" target="_blank" rel="noopener">HomeGuide</a>. Not a quote.')}
    <h2>Water-damaged drywall cost</h2>
    <p>Water damage doesn’t have a single price because the scope varies so much — a 2-foot ceiling stain from an AC pan is a very different job from 4-foot flood cuts through a whole house. The drywall portion follows the per-square-foot and ceiling figures above. Add-ons that change the number: replacing wet insulation, stain-blocking primer, moisture-resistant board, baseboard reinstall and paint. Leak repair and mold remediation (if needed) are separate trades.</p>
    <h2>What changes the price in Southwest Florida</h2>
    <ul>
      <li><strong>Texture.</strong> Knockdown and orange peel are common here, and matching them properly takes more time than a smooth patch.</li>
      <li><strong>Humidity &amp; drying time.</strong> Florida humidity slows compound drying, which can mean more return visits.</li>
      <li><strong>Ceiling height.</strong> Vaulted and 10-ft+ ceilings need scaffolding.</li>
      <li><strong>Storm demand.</strong> After major hurricanes, demand for drywall trades spikes across Charlotte and Sarasota counties.</li>
      <li><strong>Paint matching.</strong> Faded or unknown paint can mean repainting a full wall instead of touching up.</li>
      <li><strong>Bundling.</strong> Several small repairs in one visit costs far less than several separate visits.</li>
    </ul>
    <h2>How to get an accurate quote fast</h2>
    <ol><li>Take one close-up photo and one from across the room.</li><li>Measure roughly how big the damaged area is.</li><li>Note whether it’s a wall or ceiling, and what texture is around it.</li><li>Send it through our <a href="/free-estimate/">free estimate form</a> or text it to {BIZ['phone']}.</li></ol>
    <h2>Cost FAQ</h2>
    {x['faq_html'](faqs)}
    <p style="margin-top:22px;font-size:14px;color:var(--muted)">Sources: <a href="{HG_REPAIR}" target="_blank" rel="noopener">HomeGuide — Drywall Repair Cost</a> (updated Oct 20, 2025); <a href="{HG_POPCORN}" target="_blank" rel="noopener">HomeGuide — Popcorn Ceiling Removal Cost</a>. Figures are national averages and are not quotes from Veteran Drywall.</p>
  </article>
  {x['aside']()}
</div></section>
''' + x['cta_band'](title='Want your real number?', text='Send two photos. Get a free written estimate from a local, veteran-owned crew.') + '</main>\n' + x['footer']()
    x['write'](path, out)


def about_page(x):
    ic, e = x['ic'], x['e']
    path = '/about/'
    title = 'About Veteran Drywall | USMC Veteran-Owned, North Port FL'
    desc = 'Meet Steven McPherson — USMC veteran, 10+ years of service, four deployments — and the Veteran Drywall crew in North Port, FL. License SCC131152687.'
    crumbs = [('Home', '/'), ('About', path)]
    nodes = x['webpage_node'](path, title, desc, crumbs, ptype='AboutPage', extra={"mainEntity": {"@id": SITE + "/#business"}})
    out = x['head'](path, title, desc, x['graph'](nodes)) + x['header']('about')
    out += x['page_hero'](crumbs, 'Our story', 'Built on service. <span class="hl">Finished with discipline.</span>',
                          'Veteran Drywall is a USMC veteran-owned drywall contractor based in North Port, Florida — owned by Steven McPherson and run with his crew, Mike and Rick.',
                          img=('/assets/images/webp/veteran-drywall-crew-hero.webp', '/assets/images/jpg-fallbacks/veteran-drywall-crew-hero.jpg', 'Steven, Mike and Rick of Veteran Drywall', 1901, 1053))
    facts = [('Legal name', BIZ['legal']), ('Owner', 'Steven McPherson, U.S. Marine Corps veteran'), ('Service record', '10+ years of USMC service, four overseas deployments'),
             ('Crew', 'Steven, Mike and Rick'), ('Based in', 'North Port, FL 34286 (Sarasota County)'), ('Service area', 'North Port, Port Charlotte, Venice, Sarasota, Englewood, Punta Gorda'),
             ('Florida license', f'{BIZ["license"]} — <a href="https://www.myfloridalicense.com/wl11.asp" target="_blank" rel="noopener">verify on DBPR</a>'),
             ('Phone', f'<a href="tel:{BIZ["phone_e164"]}">{BIZ["phone"]}</a> (alt. <a href="tel:{BIZ["alt_e164"]}">{BIZ["alt"]}</a>)'), ('Email', f'<a href="mailto:{BIZ["email"]}">{BIZ["email"]}</a>'),
             ('Specialties', 'Drywall repair, texture matching, water & storm damage, ceilings, popcorn removal, new drywall, stucco, paint & trim')]
    rows = ''.join(f'<tr><th scope="row" style="background:transparent;color:var(--ink);text-transform:none;letter-spacing:0;font-size:15px;width:34%">{a}</th><td>{b}</td></tr>' for a, b in facts)
    out += f'''<section class="section"><div class="wrap content-grid">
  <article class="prose">
    <div class="answer reveal"><strong>Who is Veteran Drywall?</strong>Veteran Drywall LLC is a drywall contractor in North Port, Florida, owned by U.S. Marine Corps veteran Steven McPherson. The crew — Steven, Mike and Rick — repairs, textures and finishes drywall for homeowners, property managers and builders across Sarasota and Charlotte counties. Florida license # {BIZ['license']}.</div>
    <h2>From the Corps to the job site</h2>
    <p>Before Veteran Drywall, Steven McPherson served more than a decade in the United States Marine Corps, including four overseas deployments. That’s where the standard comes from: attention to detail, showing up when you say you will, and finishing the job right the first time.</p>
    <p>He brought that standard home to North Port and built a crew around it. When you call Veteran Drywall, Steven answers his own phone — and the people who quote your job are the people who do it.</p>
    <figure style="margin:24px 0"><picture><source type="image/webp" srcset="/assets/images/webp/usmc-veteran-service-photo-american-flag.webp"><img src="/assets/images/jpg-fallbacks/usmc-veteran-service-photo-american-flag.jpg" alt="Steven’s U.S. Marine Corps unit with an American flag during deployment" width="574" height="416" loading="lazy" style="border-radius:18px;width:100%"></picture><figcaption style="font-size:13.5px;color:var(--muted);margin-top:8px">Steven’s Marine Corps unit during deployment.</figcaption></figure>
    <h2>What we stand for</h2>
    <div class="tiles">
      <div class="tile"><b>No subcontractor roulette</b><span>One accountable crew from estimate to walkthrough.</span></div>
      <div class="tile"><b>Straight answers</b><span>Written estimates, realistic timelines, honest limits.</span></div>
      <div class="tile"><b>Respect for your home</b><span>Floors and furniture protected, daily clean-up.</span></div>
      <div class="tile"><b>Finish that disappears</b><span>Texture matching is our specialty, not an afterthought.</span></div>
    </div>
    <div class="verse"><q>Greater love hath no man than this, that a man lay down his life for his friends.</q><small>JOHN 15:13 — THE VERSE ON OUR LOGO</small></div>
    <h2>Meet the crew</h2>
    <div class="team" style="margin-top:14px">
      <div class="member"><picture><source type="image/webp" srcset="/assets/images/team/steven-mcpherson-full-body-portrait-fill.webp"><img src="/assets/images/team/steven-mcpherson-full-body-portrait-fill.jpg" alt="Steven McPherson" width="1024" height="1536" loading="lazy"></picture><div class="mi"><span>Owner · USMC veteran</span><h3>Steven</h3></div></div>
      <div class="member"><picture><source type="image/webp" srcset="/assets/images/team/mike-veteran-drywall-full-body-portrait-fill.webp"><img src="/assets/images/team/mike-veteran-drywall-full-body-portrait-fill.jpg" alt="Mike" width="1024" height="1536" loading="lazy"></picture><div class="mi"><span>Crew</span><h3>Mike</h3></div></div>
      <div class="member"><picture><source type="image/webp" srcset="/assets/images/team/rick-veteran-drywall-full-body-portrait-fill.webp"><img src="/assets/images/team/rick-veteran-drywall-full-body-portrait-fill.jpg" alt="Rick" width="1024" height="1536" loading="lazy"></picture><div class="mi"><span>Crew</span><h3>Rick</h3></div></div>
    </div>
    <h2>Veteran Drywall at a glance</h2>
    <div class="table-wrap"><table class="cost"><tbody>{rows}</tbody></table></div>
  </article>
  {x['aside']()}
</div></section>
''' + x['cta_band']() + '</main>\n' + x['footer']()
    x['write'](path, out)


def faq_page(x):
    path = '/faq/'
    title = 'Drywall FAQ: Repairs, Texture, Water Damage & Cost'
    desc = 'Straight answers on drywall repair, texture matching, water damage, popcorn removal, cost, licensing and service areas from Veteran Drywall in North Port, FL.'
    crumbs = [('Home', '/'), ('FAQ', path)]
    extra = [('Do you provide documentation for HOAs?', 'Yes. License information, written estimates and before/after photos are available on request.'),
             ('Do you do mold remediation?', 'No. If you suspect mold, have it assessed and remediated by a qualified professional first. Once the area is safe and dry, we handle the drywall and finish.'),
             ('Can I send photos instead of scheduling a visit?', 'Yes — the estimate form accepts up to three photos. Many small repairs can be quoted from photos alone.'),
             ('What textures can you match?', 'Knockdown, orange peel, skip trowel, popcorn and smooth (Level 5) on interior walls and ceilings, plus exterior stucco.')]
    faqs = GENERAL_FAQS + extra
    nodes = x['webpage_node'](path, title, desc, crumbs)
    nodes.append(x['faq_node'](path, faqs))
    out = x['head'](path, title, desc, x['graph'](nodes)) + x['header']('faq')
    out += x['page_hero'](crumbs, 'Straight answers', 'Drywall questions, <span class="hl">answered.</span>', 'Everything homeowners, landlords and realtors ask us — about repairs, texture, water damage, costs and how we work.')
    out += f'''<section class="section"><div class="wrap content-grid"><article class="prose">{x['faq_html'](faqs)}</article>{x['aside']()}</div></section>''' + x['cta_band']() + '</main>\n' + x['footer']()
    x['write'](path, out)


def estimate_page(x):
    path = '/free-estimate/'
    title = 'Free Drywall Estimate in 60 Seconds | Veteran Drywall'
    desc = 'Get a free drywall estimate: send photos of holes, cracks, water damage, ceilings or popcorn. Veteran-owned, licensed FL SCC131152687. (941) 527-5924.'
    crumbs = [('Home', '/'), ('Free estimate', path)]
    nodes = x['webpage_node'](path, title, desc, crumbs, ptype='ContactPage')
    out = x['head'](path, title, desc, x['graph'](nodes)) + x['header']()
    out += '<main id="main">' + x['quote_section'](htag='h1') + '''<section class="section-tight"><div class="wrap"><div class="tiles">
      <div class="tile"><b>1 · Send it</b><span>Four quick taps and up to three photos.</span></div>
      <div class="tile"><b>2 · We review</b><span>Steven looks at every request himself.</span></div>
      <div class="tile"><b>3 · Straight answer</b><span>Usually within one business day — call, text or email.</span></div>
      <div class="tile"><b>4 · Written estimate</b><span>Free, no obligation, no pressure.</span></div>
    </div></div></section></main>
''' + x['footer']()
    x['write'](path, out)


def simple_shell(x, path, title, desc, robots, body, active=''):
    nodes = x['webpage_node'](path, title, desc, [('Home', '/'), (title.split('|')[0].strip(), path)] if path != '/404.html' else None)
    return x['head'](path, title, desc, x['graph'](nodes), robots=robots) + x['header'](active) + body + x['footer']()

def privacy_page(x):
    path = '/privacy/'
    body = f'''<main id="main"><section class="page-hero"><div class="wrap"><span class="eyebrow on-dark">Legal</span><h1>Privacy policy</h1><p class="updated">Last updated: September 25, 2026</p></div></section>
<section class="section"><div class="wrap narrow prose">
<p>Veteran Drywall LLC (“we,” “us”) respects your privacy. This policy explains what this website collects and how it’s used.</p>
<h2>Information we collect</h2><p>When you submit our estimate form, we collect what you provide: name, phone, email, job city, the service you need, timing, whether you’re a homeowner/property manager/realtor/contractor/business, your preferred contact method, project details, and any photos you choose to attach. We also record the page you submitted from (and the referring site, if any) so we know which pages and ads are helpful. We don’t ask for sensitive personal information.</p>
<h2>How we use it</h2><p>Only to respond to your request and, if you hire us, to do the work. We don’t sell, rent or share your information with third parties for marketing.</p>
<h2>Form processing</h2><p>Form submissions and photos are processed and stored by Netlify, our hosting provider, and delivered to us. See <a href="https://www.netlify.com/privacy/" target="_blank" rel="noopener">Netlify’s privacy policy</a>.</p>
<h2>Chat assistant</h2><p>The “SOS” chat runs entirely in your browser. It doesn’t send or store your messages anywhere — they disappear when you close the page.</p>
<h2>Cookies &amp; analytics</h2><p>This site does not set tracking cookies. Fonts are hosted on this site. Some project photos are still served from our previous website host, which may log standard technical data (like IP addresses) when delivering files.</p>
<h2>Your choices</h2><p>Prefer not to use the form? Call <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a> (alt. <a href="tel:{BIZ['alt_e164']}">{BIZ['alt']}</a>) or email <a href="mailto:{BIZ['email']}">{BIZ['email']}</a>. To ask about or delete information you’ve submitted, contact us the same way.</p>
<h2>Contact</h2><p>{BIZ['legal']} · North Port, FL 34286 · {BIZ['phone']} · {BIZ['email']}</p>
</div></section></main>
'''
    x['write'](path, simple_shell(x, path, 'Privacy Policy | Veteran Drywall LLC', 'Privacy policy for Veteran Drywall LLC — what our estimate form collects and how we use it.', 'index,follow', body))

def thanks_page(x):
    path = '/thank-you/'
    ic = x['ic']
    body = f'''<main id="main"><section class="hero" style="min-height:70vh;display:flex;align-items:center"><div class="wrap center" style="position:relative">
<div style="font-size:72px">🎖️</div><h1 class="h-xl">Request received. <span class="hl">We’re on it.</span></h1>
<p class="sub" style="margin:18px auto 0">Thanks for reaching out to Veteran Drywall. Expect a call, text or email — usually within one business day.</p>
<div class="btn-row" style="justify-content:center;margin-top:28px"><a class="btn btn-gold btn-lg" href="tel:{BIZ['phone_e164']}">{ic('phone')} Need it faster? Call {BIZ['phone']}</a><a class="btn btn-outline btn-lg" href="/">Back to home</a></div>
</div></section></main>
'''
    x['write'](path, simple_shell(x, path, 'Request Received | Veteran Drywall LLC', 'Thanks — your estimate request is in.', 'noindex,follow', body))

def notfound_page(x):
    body = '''<main id="main"><section class="hero" style="min-height:70vh;display:flex;align-items:center"><div class="wrap center" style="position:relative">
<h1 class="h-xl" style="font-size:clamp(90px,16vw,180px);color:var(--gold)">404</h1><h2 class="h-md">This wall doesn’t exist.</h2>
<p class="sub" style="margin:16px auto 0">The page was moved, removed, or never hung in the first place.</p>
<div class="btn-row" style="justify-content:center;margin-top:26px"><a class="btn btn-gold btn-lg" href="/">Back to home</a><a class="btn btn-outline btn-lg" href="/free-estimate/">Free estimate</a></div>
</div></section></main>
'''
    x['write']('/404.html', simple_shell(x, '/404.html', 'Page Not Found | Veteran Drywall', 'Page not found.', 'noindex,follow', body))
