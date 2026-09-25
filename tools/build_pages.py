#!/usr/bin/env python3
"""Veteran Drywall static page generator (v11).

Run from the project root:  python3 tools/build_pages.py
It writes plain static HTML (no build step needed on Netlify). Edit the
content in tools/content.py, re-run, and push. The /tools folder is blocked
from public access by a rule in netlify.toml.
"""
import json, os, html, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BUILD_DATE = '2026-09-25'
V = 'v12'
CSS = f'/assets/css/site-{V}.css'
JS = f'/assets/js/site-{V}.js'
e = html.escape

# ------------------------------------------------------------------ icons
ICONS = {
 'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
 'star': '<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 'check': '<path d="M20 6L9 17l-5-5"/>',
 'pin': '<path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
 'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>',
 'flag': '<path d="M4 22V4M4 4h13l-2 4 2 4H4"/>',
 'hole': '<path d="M4 4h16v16H4z"/><path d="M10 9l-1.5 3 2 1-1 3 3-2 1.5 1 .5-3 2-1-2.5-1 .5-2-2 1z"/>',
 'crack': '<path d="M4 4h16v16H4z"/><path d="M12 4l-2 5 3 3-3 4 1 4"/>',
 'drop': '<path d="M12 2.7s-7 7.6-7 12.3a7 7 0 0 0 14 0c0-4.7-7-12.3-7-12.3z"/><path d="M9 15a3 3 0 0 0 3 3"/>',
 'ceiling': '<path d="M3 5h18M6 5v3M18 5v3M12 5v5"/><path d="M8 14c0 3 2 6 4 6s4-3 4-6"/><path d="M12 10v4"/>',
 'dots': '<circle cx="6" cy="7" r="1.6"/><circle cx="12" cy="5" r="1.6"/><circle cx="18" cy="8" r="1.6"/><circle cx="8" cy="13" r="1.6"/><circle cx="15" cy="13" r="1.6"/><circle cx="6" cy="19" r="1.6"/><circle cx="12" cy="18" r="1.6"/><circle cx="18" cy="18" r="1.6"/>',
 'popcorn': '<path d="M3 4h18"/><circle cx="6" cy="8" r="2"/><circle cx="11" cy="7.5" r="2"/><circle cx="16" cy="8.5" r="2"/><circle cx="8.5" cy="12" r="1.6"/><circle cx="14" cy="12.5" r="1.6"/><path d="M5 19l3-3M11 20l2-3M17 19l-1-3"/>',
 'house': '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/>',
 'trowel': '<path d="M3 20l8-8"/><path d="M10 7l7-4 4 4-4 7z"/>',
 'roller': '<rect x="3" y="3" width="15" height="6" rx="2"/><path d="M18 6h3v5h-9v3"/><rect x="10" y="14" width="4" height="7" rx="1"/>',
 'clipboard': '<rect x="5" y="4" width="14" height="18" rx="2"/><path d="M9 4V2h6v2M9 11h6M9 15h6M9 19h3"/>',
 'camera': '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
 'send': '<path d="M22 2L11 13M22 2l-7 20-4-9-9-4z"/>',
 'fb': '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
 'caret': '<path d="M6 9l6 6 6-6"/>',
 'dollar': '<path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
 'hammer': '<path d="M15 12l-8.5 8.5a2.1 2.1 0 0 1-3-3L12 9"/><path d="M17.6 15L22 10.6 13.4 2 9 6.4z"/>',
 'users': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
}
def ic(name, cls=''):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><use href="#i-{name}"/></svg>'
def sprite():
    return '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' + ''.join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()) + '</defs></svg>'

# ------------------------------------------------------------------ schema
def city_node(c):
    return {"@type": "City", "name": c['name'] + ", FL", "sameAs": c['wiki']}

def business_node():
    return {
        "@type": ["GeneralContractor", "HomeAndConstructionBusiness"],
        "@id": SITE + "/#business",
        "name": BIZ['legal'],
        "alternateName": [BIZ['name'], "Veteran Drywall North Port"],
        "description": BIZ['description'],
        "url": SITE + "/",
        "telephone": BIZ['phone_e164'],
        "email": BIZ['email'],
        "image": [SITE + "/assets/images/og/veteran-drywall-og-v11.jpg", SITE + "/assets/images/webp/veteran-drywall-crew-hero.webp"],
        "logo": {"@type": "ImageObject", "url": SITE + "/assets/images/veteran-drywall-icon-512.png", "width": 512, "height": 512},
        "address": {"@type": "PostalAddress", "streetAddress": BIZ['street'], "addressLocality": "North Port", "addressRegion": "FL", "postalCode": "34286", "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": 27.0723, "longitude": -82.1959},
        "areaServed": [city_node(c) for c in CITIES] + [
            {"@type": "AdministrativeArea", "name": "Sarasota County, FL", "sameAs": "https://en.wikipedia.org/wiki/Sarasota_County,_Florida"},
            {"@type": "AdministrativeArea", "name": "Charlotte County, FL", "sameAs": "https://en.wikipedia.org/wiki/Charlotte_County,_Florida"}],
        "contactPoint": [
            {"@type": "ContactPoint", "telephone": BIZ['phone_e164'], "contactType": "customer service", "areaServed": "US-FL", "availableLanguage": "en"},
            {"@type": "ContactPoint", "telephone": BIZ['alt_e164'], "contactType": "customer service", "description": "Alternate line", "areaServed": "US-FL"}],
        "founder": {"@id": SITE + "/#steven"},
        "employee": [{"@id": SITE + "/#steven"}, {"@type": "Person", "name": "Mike", "jobTitle": "Drywall finisher"}, {"@type": "Person", "name": "Rick", "jobTitle": "Drywall finisher"}],
        "slogan": "Military-grade craftsmanship. Flawless finishes.",
        "knowsAbout": ["Drywall repair", "Drywall installation", "Drywall finishing", "Texture matching", "Knockdown texture", "Orange peel texture", "Skip trowel texture", "Level 5 drywall finish", "Popcorn ceiling removal", "Water-damaged drywall repair", "Hurricane and storm damage drywall repair", "Ceiling repair", "Stucco repair", "Interior painting", "Exterior painting", "Framing", "Finish carpentry and trim"],
        "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license", "name": "Florida contractor license " + BIZ['license'], "identifier": BIZ['license'], "recognizedBy": {"@type": "GovernmentOrganization", "name": "Florida Department of Business and Professional Regulation", "url": "https://www2.myfloridalicense.com/"}},
        "sameAs": [BIZ['facebook']],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Drywall and finishing services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@id": SITE + "/" + s['slug'] + "/#service"}} for s in SERVICES]},
        "priceRange": "Free estimates",
        "paymentAccepted": None,
    }

def graph(page_nodes):
    biz = {k: v for k, v in business_node().items() if v is not None}
    base = [
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Veteran Drywall", "publisher": {"@id": SITE + "/#business"}, "inLanguage": "en-US"},
        biz,
        {"@type": "Person", "@id": SITE + "/#steven", "name": "Steven McPherson", "jobTitle": "Owner", "worksFor": {"@id": SITE + "/#business"},
         "description": "U.S. Marine Corps veteran (10+ years of service, four overseas deployments) and owner of Veteran Drywall LLC in North Port, Florida.",
         "image": SITE + "/assets/images/team/steven-mcpherson-full-body-portrait-fill.jpg"},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": base + page_nodes}, ensure_ascii=False, indent=1)

def webpage_node(path, title, desc, crumbs, ptype="WebPage", extra=None):
    url = SITE + path
    n = {"@type": ptype, "@id": url + "#webpage", "url": url, "name": title, "description": desc,
         "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#business"},
         "dateModified": BUILD_DATE, "inLanguage": "en-US",
         "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/assets/images/og/veteran-drywall-og-v11.jpg"}}
    if crumbs:
        n["breadcrumb"] = {"@id": url + "#breadcrumb"}
    if extra: n.update(extra)
    out = [n]
    if crumbs:
        out.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": nm, "item": SITE + p} for i, (nm, p) in enumerate(crumbs)]})
    return out

def faq_node(path, faqs):
    return {"@type": "FAQPage", "@id": SITE + path + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs]}

def strip_tags(s):
    import re
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()

# ------------------------------------------------------------------ chrome
FONTS = 'https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap'

def head(path, title, desc, schema, robots='index,follow,max-image-preview:large', preload=''):
    canon = SITE + path
    return f'''<!DOCTYPE html>
<html lang="en-US" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0A1528">
<meta name="geo.region" content="US-FL">
<meta name="geo.placename" content="North Port">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Veteran Drywall">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/images/og/veteran-drywall-og-v11.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Veteran Drywall crew — USMC veteran-owned drywall contractor in North Port, FL">
<meta name="twitter:card" content="summary_large_image">
<script>(function(d){{var r=d.documentElement;r.className=r.className.replace('no-js','js');if(!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches))r.className+=' motion';setTimeout(function(){{if(!window.VD_OK)r.classList.remove('motion')}},3500)}})(document);</script>
<link rel="preload" href="/assets/fonts/big-shoulders-display-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/plus-jakarta-sans-var.woff2" as="font" type="font/woff2" crossorigin>
{preload}<link rel="stylesheet" href="{CSS}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/images/veteran-drywall-icon-192.png">
<link rel="apple-touch-icon" href="/assets/images/veteran-drywall-icon-512.png">
<link rel="manifest" href="/site.webmanifest">
<script type="application/ld+json">
{schema}
</script>
</head>
'''

def nav_services_drop():
    items = ''.join(f'<a href="/{s["slug"]}/"><span class="di">{ic(s["icon"])}</span><span><b>{e(s["name"])}</b><small>{e(s["blurb"])}</small></span></a>' for s in SERVICES)
    return items

def header(active=''):
    def cur(k): return ' aria-current="page"' if active == k else ''
    areas = ''.join(f'<a href="/areas/{c["slug"]}/"><span class="di">{ic("pin")}</span><span><b>{e(c["name"])}</b><small>{e(c["county"])}</small></span></a>' for c in CITIES)
    m_services = ''.join(f'<a href="/{s["slug"]}/">{e(s["name"])}</a>' for s in SERVICES)
    m_areas = ''.join(f'<a href="/areas/{c["slug"]}/">{e(c["name"])}</a>' for c in CITIES)
    return f'''<body>
{sprite()}
<a class="skip-link" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
<div class="topbar"><div class="wrap">
  <div class="tb-items"><span>{ic('flag')}USMC veteran owned &amp; operated</span><span class="tb-hide">{ic('shield')}FL Lic. # {BIZ['license']}</span><span class="tb-hide">{ic('star')}Free written estimates</span></div>
  <a class="tb-hide" href="tel:{BIZ['phone_e164']}">Call {BIZ['phone']}</a>
</div></div>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="Veteran Drywall — home"><img src="/assets/images/veteran-drywall-header-logo-transparent.webp" alt="Veteran Drywall LLC logo" width="1500" height="458"></a>
    <nav aria-label="Main">
      <ul class="menu">
        <li class="has-drop"><button type="button" aria-expanded="false">Services {ic('caret','caret')}</button><div class="drop">{nav_services_drop()}</div></li>
        <li class="has-drop"><button type="button" aria-expanded="false">Service Areas {ic('caret','caret')}</button><div class="drop narrow-drop">{areas}</div></li>
        <li><a href="/drywall-repair-cost/"{cur('cost')}>Cost Guide</a></li>
        <li><a href="/about/"{cur('about')}>About</a></li>
        <li><a href="/faq/"{cur('faq')}>FAQ</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a class="nav-phone" href="tel:{BIZ['phone_e164']}"><span class="ph-ic">{ic('phone')}</span><span><small>Call or text</small>{BIZ['phone']}</span></a>
      <a class="btn btn-gold btn-sm" href="/free-estimate/" data-quote>Free Estimate</a>
      <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobileNav"><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobileNav">
  <h4>SERVICES</h4><div class="m-grid">{m_services}</div>
  <h4>SERVICE AREAS</h4><div class="m-grid">{m_areas}</div>
  <h4>MORE</h4>
  <a href="/drywall-repair-cost/">Cost Guide</a><a href="/about/">About Us</a><a href="/faq/">FAQ</a>
  <a class="btn btn-gold btn-lg btn-block" href="tel:{BIZ['phone_e164']}">{ic('phone')} Call {BIZ['phone']}</a>
</div>
'''

def cta_band(title='Ready to make that damage <span class="splash navy">disappear?</span>', text='Free written estimate. Send photos and get a straight answer from a local, veteran-owned crew.', service=''):
    ds = f' data-service="{e(service)}"' if service else ''
    href = '/free-estimate/' + (f'?service={service.replace(" ", "+")}' if service else '')
    return f'''<section class="section-tight"><div class="wrap">
  <div class="cta-band reveal">
    <div><h2>{title}</h2><p>{text}</p></div>
    <div class="btn-row"><a class="btn btn-dark btn-lg" href="{href}" data-quote{ds}>Start my free estimate</a><a class="btn btn-outline btn-lg" href="tel:{BIZ['phone_e164']}">{ic('phone')} {BIZ['phone']}</a></div>
  </div>
</div></section>
'''

def footer():
    svc = ''.join(f'<li><a href="/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    ar = ''.join(f'<li><a href="/areas/{c["slug"]}/">{e(c["name"])}, FL</a></li>' for c in CITIES)
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="/assets/images/veteran-drywall-horizontal-logo.webp" alt="Veteran Drywall LLC" width="1500" height="500" loading="lazy">
        <address><strong style="color:#fff">{BIZ['legal']}</strong><br>{BIZ['street']}, North Port, FL 34286<br>
        <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a> · Alt: <a href="tel:{BIZ['alt_e164']}">{BIZ['alt']}</a><br>
        <a href="mailto:{BIZ['email']}">{BIZ['email']}</a><br>
        FL License # {BIZ['license']} · <a href="https://www.myfloridalicense.com/wl11.asp" target="_blank" rel="noopener">Verify</a></address>
        <p style="margin-top:14px;font-style:italic;color:var(--gold-2)">“Greater love hath no man than this…” — John 15:13</p>
      </div>
      <div><h4>SERVICES</h4><ul>{svc}</ul></div>
      <div><h4>SERVICE AREAS</h4><ul>{ar}</ul></div>
      <div><h4>COMPANY</h4><ul>
        <li><a href="/about/">About Steven &amp; the crew</a></li>
        <li><a href="/drywall-repair-cost/">Drywall repair cost guide</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/free-estimate/">Free estimate</a></li>
        <li><a href="{BIZ['facebook']}" target="_blank" rel="noopener">Facebook</a></li>
        <li><a href="/privacy/">Privacy policy</a></li>
      </ul></div>
    </div>
    <div class="foot-bottom"><span>© <span class="yr">2026</span> {BIZ['legal']}. Veteran owned &amp; operated. Semper Fi.</span><span>Serving Sarasota &amp; Charlotte Counties, Florida</span></div>
  </div>
</footer>
<nav class="actionbar" aria-label="Quick actions">
  <a class="ab-call" href="tel:{BIZ['phone_e164']}">{ic('phone')} Call now</a>
  <a class="ab-quote" href="/free-estimate/" data-quote>{ic('camera')} Free estimate</a>
</nav>
<button class="chat-fab" id="chatFab" type="button" aria-expanded="false" aria-controls="chat" aria-label="Open SOS drywall help chat">
  <span class="sos" aria-hidden="true">SOS</span>
  <img src="/assets/images/veteran-drywall-chat-sos-icon.webp" alt="" width="72" height="72" loading="lazy">
</button>
<div class="chat" id="chat" role="dialog" aria-label="Veteran Drywall help chat">
  <div class="chat-head"><div><b>SOS Drywall Help</b><small><span class="pulse-dot"></span>Instant answers · real crew follow-up</small></div><button class="chat-x" id="chatX" type="button" aria-label="Close chat">×</button></div>
  <div class="chat-log" id="chatLog" aria-live="polite"></div>
  <div class="chat-starters" id="chatStarters">
    <button type="button">I have water damage</button><button type="button">Hole in my wall</button><button type="button">Match my texture</button><button type="button">Popcorn ceiling</button><button type="button">How much does it cost?</button><button type="button">Are you licensed?</button><button type="button">I'm a property manager</button>
  </div>
  <form class="chat-form" id="chatForm"><label class="sr-only" for="chatText">Your question</label><input id="chatText" type="text" placeholder="Ask about drywall, texture, stucco…" autocomplete="off" maxlength="300"><button type="submit" aria-label="Send">{ic('send')}</button></form>
  <p class="chat-fine">Automated assistant — answers general questions only. Pricing &amp; scheduling are confirmed by the team.</p>
</div>
<script src="{JS}" defer></script>
</body>
</html>
'''

def page_hero(crumbs, eyebrow, h1, sub, service='', img=None, extra=''):
    cr = ''.join(f'<li><a href="{p}">{e(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{e(n)}</li>' for i, (n, p) in enumerate(crumbs))
    ds = f' data-service="{e(service)}"' if service else ''
    href = '/free-estimate/' + (f'?service={service.replace(" ", "+")}' if service else '')
    im = ''
    if img:
        im = f'<div class="ph-img reveal"><picture><source type="image/webp" srcset="{img[0]}"><img src="{img[1] or img[0]}" alt="{e(img[2])}" width="{img[3]}" height="{img[4]}" fetchpriority="high"></picture></div>'
    return f'''<main id="main">
<section class="page-hero">
  <div class="wrap">
    <nav aria-label="Breadcrumb"><ol class="crumbs">{cr}</ol></nav>
    <div class="page-hero-grid">
      <div>
        <span class="eyebrow on-dark">{eyebrow}</span>
        <h1 class="split-words">{h1}</h1>
        <p class="sub">{sub}</p>
        <div class="btn-row"><a class="btn btn-gold btn-lg" href="{href}" data-quote{ds}>Get my free estimate</a><a class="btn btn-outline btn-lg" href="tel:{BIZ['phone_e164']}">{ic('phone')} {BIZ['phone']}</a></div>
        <div class="hero-trust"><span>{ic('flag')}USMC veteran owned</span><span>{ic('shield')}FL Lic. # {BIZ['license']}</span><span>{ic('star')}Free written estimates</span></div>
        {extra}
      </div>
      {im}
    </div>
  </div>
</section>
'''

def faq_html(faqs, cls=''):
    return '<div class="faq ' + cls + '">' + ''.join(
        f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div class="a"><p>{a}</p></div></details>' for i, (q, a) in enumerate(faqs)) + '</div>'

def aside(current_slug='', service=''):
    ds = f' data-service="{e(service)}"' if service else ''
    href = '/free-estimate/' + (f'?service={service.replace(" ", "+")}' if service else '')
    AC = ' aria-current="page"'
    svc = ''.join(f'<li><a href="/{s["slug"]}/"{AC if s["slug"] == current_slug else ""}>{e(s["name"])}<span>→</span></a></li>' for s in SERVICES)
    return f'''<aside class="aside">
  <div class="dark-card">
    <span class="eyebrow on-dark">Free estimate</span>
    <h3>Send photos. Get a straight answer.</h3>
    <p>Most estimates come back within one business day. Steven answers his own phone.</p>
    <a class="btn btn-gold btn-block" href="{href}" data-quote{ds}>Start my estimate</a>
    <a class="btn btn-outline btn-block" style="margin-top:10px" href="tel:{BIZ['phone_e164']}">{ic('phone')} {BIZ['phone']}</a>
  </div>
  <div class="card"><h3>All services</h3><ul>{svc}</ul></div>
  <div class="card"><h3>Licensed in Florida</h3><p>{BIZ['legal']} · License # {BIZ['license']}. <a class="link-arrow" href="https://www.myfloridalicense.com/wl11.asp" target="_blank" rel="noopener">Verify on DBPR</a></p></div>
</aside>'''

def write(path, content):
    out = os.path.join(ROOT, path.strip('/'), 'index.html') if not path.endswith('.html') else os.path.join(ROOT, path.strip('/'))
    if path == '/': out = os.path.join(ROOT, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f: f.write(content)
    print('wrote', os.path.relpath(out, ROOT), len(content))

# ------------------------------------------------------------------ pages
def service_page(s):
    path = f'/{s["slug"]}/'
    crumbs = [('Home', '/'), ('Services', '/#services'), (s['name'], path)]
    nodes = webpage_node(path, s['title'], s['desc'], crumbs, extra={"mainEntity": {"@id": SITE + path + "#service"}})
    nodes.append({"@type": "Service", "@id": SITE + path + "#service", "name": s['name'], "serviceType": s['service_type'],
                  "description": strip_tags(s['answer']), "provider": {"@id": SITE + "/#business"},
                  "areaServed": [city_node(c) for c in CITIES], "url": SITE + path,
                  "audience": {"@type": "Audience", "audienceType": "Homeowners, landlords, property managers and realtors"}})
    nodes.append(faq_node(path, s['faqs']))
    body = head(path, s['title'], s['desc'], graph(nodes)) + header() + page_hero(crumbs, s['eyebrow'], s['h1'], s['sub'], s['form_value'], s.get('img'))
    tiles = ''.join(f'<div class="tile"><b>{e(a)}</b><span>{b}</span></div>' for a, b in s['fixes'])
    steps = ''.join(f'<li><strong>{e(a)}.</strong> {b}</li>' for a, b in s['steps'])
    cost = s.get('cost_html', '')
    local = s.get('local_html', '')
    extra = s.get('extra_html', '')
    area_links = ''.join(f'<a href="/areas/{c["slug"]}/">{e(s["short"].capitalize())} in {e(c["name"])}<small>{e(c["county"])}</small></a>' for c in CITIES)
    body += f'''<section class="section"><div class="wrap content-grid">
  <article class="prose">
    <div class="answer reveal"><strong>Quick answer</strong>{s['answer']}</div>
    <h2>What we fix</h2>
    <div class="tiles">{tiles}</div>
    <h2>How we do it</h2>
    <ol>{steps}</ol>
    {extra}
    {cost}
    {local}
    <h2>{e(s['name'])} FAQ</h2>
    {faq_html(s['faqs'])}
  </article>
  {aside(s['slug'], s['form_value'])}
</div></section>
<section class="section-tight paper"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Local service</span><h2 class="h-md">{e(s['name'])} across Sarasota &amp; Charlotte County</h2></div>
  <div class="related">{area_links}</div>
</div></section>
''' + cta_band(service=s['form_value']) + '</main>\n' + footer()
    write(path, body)

def city_page(c):
    path = f'/areas/{c["slug"]}/'
    crumbs = [('Home', '/'), ('Service Areas', '/#areas'), (c['name'] + ', FL', path)]
    title = c['title']; desc = c['desc']
    nodes = webpage_node(path, title, desc, crumbs, extra={"about": [{"@id": SITE + "/#business"}, city_node(c)], "spatialCoverage": city_node(c)})
    nodes.append(faq_node(path, c['faqs']))
    body = head(path, title, desc, graph(nodes)) + header() + page_hero(crumbs, f'{e(c["county"])} · Local crew', c['h1'], c['sub'], '', c.get('img'))
    svc_links = ''.join(f'<a href="/{s["slug"]}/">{e(s["name"])}<small>{e(s["blurb"])}</small></a>' for s in SERVICES)
    other = ''.join(f'<a href="/areas/{o["slug"]}/">{e(o["name"])}, FL<small>{e(o["county"])}</small></a>' for o in CITIES if o['slug'] != c['slug'])
    hoods = ', '.join(c['nearby'])
    body += f'''<section class="section"><div class="wrap content-grid">
  <article class="prose">
    <div class="answer reveal"><strong>Quick answer</strong>{c['answer']}</div>
    {c['body_html']}
    <h2>Neighborhoods &amp; nearby communities</h2>
    <p>We regularly work in and around {e(c['name'])}, including {e(hoods)}. Not sure if you're in range? Call <a href="tel:{BIZ['phone_e164']}">{BIZ['phone']}</a> — if it's close, we can usually make it work.</p>
    <h2>Drywall services in {e(c['name'])}</h2>
    <div class="related">{svc_links}</div>
    <h2>{e(c['name'])} drywall FAQ</h2>
    {faq_html(c['faqs'])}
  </article>
  {aside()}
</div></section>
<section class="section-tight paper"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Also serving</span><h2 class="h-md">Other cities we cover</h2></div>
  <div class="related">{other}</div>
</div></section>
''' + cta_band(title=f'Drywall damage in {e(c["name"])}? <span class="splash navy">Let’s fix it.</span>') + '</main>\n' + footer()
    write(path, body)

def quote_form(heading_level='h2'):
    opts = ''.join(f'<label class="opt"><input type="radio" name="service" value="{e(s["form_value"])}" required><span><em aria-hidden="true">{s["emoji"]}</em>{e(s["form_label"])}</span></label>' for s in SERVICES)
    opts += '<label class="opt"><input type="radio" name="service" value="Not sure — need advice" required><span><em aria-hidden="true">🤔</em>Not sure — need advice</span></label>'
    city_opts = ''.join(f'<option>{e(c["name"])}</option>' for c in CITIES) + '<option>Other nearby area</option>'
    return f'''<form class="wizard" id="quoteForm" name="quote" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="bot-field" enctype="multipart/form-data">
  <input type="hidden" name="form-name" value="quote">
  <input type="hidden" name="lead-source" value="">
  <p hidden><label>Leave this empty: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
  <div class="wz-body">
    <div class="wz-top"><b class="wz-count">Step 1 of 4</b><span class="wz-meter">Quote accuracy: <span>0%</span></span></div>
    <div class="wz-bar" aria-hidden="true"><i></i></div>
    <fieldset class="wz-step active" style="border:0">
      <legend class="sr-only">What needs fixing?</legend>
      <h3>What needs fixing?</h3><p class="hint">Tap one — you can explain the details in a sec.</p>
      <div class="opt-grid">{opts}</div>
    </fieldset>
    <fieldset class="wz-step" style="border:0">
      <legend class="sr-only">Timing and property</legend>
      <h3>How soon &amp; who's asking?</h3><p class="hint">Helps us route you to the right next step.</p>
      <div class="field"><span class="lbl">Timing</span><div class="opt-grid">
        <label class="opt"><input type="radio" name="urgency" value="ASAP" required><span><em aria-hidden="true">⚡</em>ASAP</span></label>
        <label class="opt"><input type="radio" name="urgency" value="This week" required><span><em aria-hidden="true">📅</em>This week</span></label>
        <label class="opt"><input type="radio" name="urgency" value="Flexible / planning" required><span><em aria-hidden="true">🧭</em>Flexible / planning</span></label>
      </div></div>
      <div class="field"><span class="lbl">I'm a…</span><div class="opt-grid">
        <label class="opt"><input type="radio" name="property-type" value="Homeowner" required><span><em aria-hidden="true">🏡</em>Homeowner</span></label>
        <label class="opt"><input type="radio" name="property-type" value="Property manager / landlord" required><span><em aria-hidden="true">🔑</em>Property manager / landlord</span></label>
        <label class="opt"><input type="radio" name="property-type" value="Realtor" required><span><em aria-hidden="true">🪧</em>Realtor</span></label>
        <label class="opt"><input type="radio" name="property-type" value="Contractor / builder" required><span><em aria-hidden="true">🦺</em>Contractor / builder</span></label>
        <label class="opt"><input type="radio" name="property-type" value="Business / commercial" required><span><em aria-hidden="true">🏢</em>Business</span></label>
      </div></div>
    </fieldset>
    <fieldset class="wz-step" style="border:0">
      <legend class="sr-only">Project details</legend>
      <h3>Show us the damage</h3><p class="hint">Photos = faster, more accurate quote. <span class="wz-tip" style="color:var(--gold-deep);font-weight:700"></span></p>
      <div class="field"><label for="city">Job location</label><select id="city" name="city" required><option value="">Choose your city…</option>{city_opts}</select></div>
      <div class="field"><label for="msg">What's going on?</label><textarea id="msg" name="message" rows="4" required placeholder="e.g. Ceiling stain about 2 ft wide in the living room after an AC leak — knockdown texture."></textarea></div>
      <div class="field js-only"><span class="lbl">Photos (optional, up to 3)</span>
        <label class="drop-zone">{ic('camera')}<b>Tap to add up to 3 photos</b><small>Phone photos are fine — we shrink them automatically</small><input id="photoPicker" type="file" accept="image/*" multiple></label>
        <div class="thumbs"></div>
      </div>
      <div class="no-js-only" style="display:none">
        <input type="file" name="photo-1" accept="image/*"><input type="file" name="photo-2" accept="image/*"><input type="file" name="photo-3" accept="image/*">
      </div>
    </fieldset>
    <fieldset class="wz-step" style="border:0">
      <legend class="sr-only">Contact details</legend>
      <h3>Where do we send it?</h3><p class="hint">No spam, no pressure — just your estimate.</p>
      <div class="f2">
        <div class="field"><label for="fname">Name</label><input id="fname" name="name" required autocomplete="name"></div>
        <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" required autocomplete="tel" inputmode="tel" pattern="[0-9()+.\\-\\s]{{10,}}"></div>
      </div>
      <div class="field"><label for="email">Email (optional)</label><input id="email" name="email" type="email" autocomplete="email"></div>
      <div class="field"><span class="lbl">Best way to reach you</span><div class="opt-grid">
        <label class="opt"><input type="radio" name="preferred-contact" value="Call" checked><span><em aria-hidden="true">📞</em>Call</span></label>
        <label class="opt"><input type="radio" name="preferred-contact" value="Text"><span><em aria-hidden="true">💬</em>Text</span></label>
        <label class="opt"><input type="radio" name="preferred-contact" value="Email"><span><em aria-hidden="true">✉️</em>Email</span></label>
      </div></div>
    </fieldset>
    <div class="wz-error" role="alert">Something went wrong — please call {BIZ['phone']}.</div>
    <div class="wz-nav">
      <button class="wz-back" type="button" hidden>← Back</button>
      <button class="btn btn-dark wz-next" type="button">Continue →</button>
      <button class="btn btn-gold wz-submit" type="submit" hidden>Send my free estimate request</button>
    </div>
    <p class="wz-fine">Free · No obligation · Reply usually within one business day · <a href="/privacy/">Privacy</a></p>
  </div>
  <div class="wz-done" role="status" aria-live="polite">
    <div class="big" aria-hidden="true">🎖️</div>
    <h3>Request received. We're on it.</h3>
    <p>Thanks — your request is in Steven's hands. Here's what happens next:</p>
    <ol><li>We review your details and photos.</li><li>You get a call, text or email — usually within one business day.</li><li>If needed, we set a time to look in person, then send a written estimate.</li></ol>
    <div class="btn-row" style="justify-content:center;margin-top:22px"><a class="btn btn-gold" href="tel:{BIZ['phone_e164']}">{ic('phone')} Need it faster? Call now</a></div>
  </div>
</form>'''

def quote_section(dark=True, htag='h2'):
    return f'''<section class="section {'dark grain' if dark else ''}" id="quote">
  <div class="wrap quote-shell">
    <div>
      <span class="eyebrow on-dark">Free estimate · 60 seconds</span>
      <{htag} class="h-lg">Tell us what's wrong. <span class="hl drip">We'll make it right.</span></{htag}>
      <p class="lede">Four quick taps and a photo or two. Most estimates come back within one business day — and Steven answers his own phone if you'd rather talk.</p>
      <ul class="contact-list">
        <li><a href="tel:{BIZ['phone_e164']}"><span class="ci">{ic('phone')}</span><span>{BIZ['phone']}<small>Call or text · main line</small></span></a></li>
        <li><a href="tel:{BIZ['alt_e164']}"><span class="ci">{ic('phone')}</span><span>{BIZ['alt']}<small>Alternate line</small></span></a></li>
        <li><a href="mailto:{BIZ['email']}"><span class="ci">{ic('mail')}</span><span>{BIZ['email']}<small>Email</small></span></a></li>
        <li><div><span class="ci">{ic('pin')}</span><span>North Port, FL 34286<small>Serving Sarasota &amp; Charlotte County</small></span></div></li>
      </ul>
    </div>
    {quote_form()}
  </div>
</section>'''

def build_all():
    from pages import home_page, cost_page, about_page, faq_page, estimate_page, privacy_page, thanks_page, notfound_page
    ctx = dict(head=head, header=header, footer=footer, graph=graph, webpage_node=webpage_node, faq_node=faq_node, ic=ic,
               cta_band=cta_band, page_hero=page_hero, faq_html=faq_html, aside=aside, quote_section=quote_section,
               quote_form=quote_form, write=write, e=e, city_node=city_node, BUILD_DATE=BUILD_DATE, V=V)
    home_page(ctx)
    for s in SERVICES: service_page(s)
    for c in CITIES: city_page(c)
    cost_page(ctx); about_page(ctx); faq_page(ctx); estimate_page(ctx); privacy_page(ctx); thanks_page(ctx); notfound_page(ctx)
    # sitemap
    urls = [('/', '1.0', 'weekly')] + [(f'/{s["slug"]}/', '0.9', 'monthly') for s in SERVICES] + [(f'/areas/{c["slug"]}/', '0.8', 'monthly') for c in CITIES] + \
           [('/drywall-repair-cost/', '0.8', 'monthly'), ('/about/', '0.6', 'yearly'), ('/faq/', '0.6', 'monthly'), ('/free-estimate/', '0.7', 'yearly'), ('/privacy/', '0.2', 'yearly')]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        f'  <url><loc>{SITE}{u}</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>{cf}</changefreq><priority>{p}</priority></url>\n' for u, p, cf in urls) + '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sm)
    print('wrote sitemap.xml with', len(urls), 'urls')

if __name__ == '__main__':
    build_all()
