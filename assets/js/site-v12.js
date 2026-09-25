/* Veteran Drywall — v11 site script. No dependencies.
   Everything on the page works and is visible without this file; it only adds
   interaction and motion. window.VD_OK tells the inline failsafe we loaded. */
(function () {
  'use strict';
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };
  var track = function (ev, data) { try { (window.dataLayer = window.dataLayer || []).push(Object.assign({ event: ev }, data || {})); } catch (e) {} };

  /* ---------- Header, progress bar, action bar ---------- */
  var header = $('.site-header'), bar = $('.progress'), actionbar = $('.actionbar');
  var onScroll = function () {
    var y = window.scrollY || 0, h = d.body.scrollHeight - innerHeight;
    if (header) header.classList.toggle('scrolled', y > 8);
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? Math.min(y / h, 1) : 0) + ')';
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---------- Mobile nav + dropdowns ---------- */
  var burger = $('.burger');
  if (burger) burger.addEventListener('click', function () {
    var open = d.body.classList.toggle('nav-open');
    burger.setAttribute('aria-expanded', open);
  });
  $$('.mobile-nav a').forEach(function (a) { a.addEventListener('click', function () { d.body.classList.remove('nav-open'); if (burger) burger.setAttribute('aria-expanded', 'false'); }); });
  $$('.has-drop > button').forEach(function (b) {
    b.addEventListener('click', function () {
      var li = b.parentNode, open = !li.classList.contains('open');
      $$('.has-drop.open').forEach(function (x) { x.classList.remove('open'); x.firstElementChild.setAttribute('aria-expanded', 'false'); });
      li.classList.toggle('open', open); b.setAttribute('aria-expanded', open);
    });
  });
  d.addEventListener('click', function (e) { if (!e.target.closest('.has-drop')) $$('.has-drop.open').forEach(function (x) { x.classList.remove('open'); x.firstElementChild.setAttribute('aria-expanded', 'false'); }); });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') { d.body.classList.remove('nav-open'); $$('.has-drop.open').forEach(function (x) { x.classList.remove('open'); }); } });

  /* ---------- Split headline words ---------- */
  $$('.split-words').forEach(function (el) {
    var i = 0;
    var walk = function (node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = d.createDocumentFragment();
          n.textContent.split(/([ \t\n\r]+)/).forEach(function (part) {
            if (!part) return;
            if (/^[ \t\n\r]+$/.test(part)) { frag.appendChild(d.createTextNode(part)); return; }
            var s = d.createElement('span'); s.className = 'w'; s.textContent = part;
            s.style.transitionDelay = (i++ * 0.06) + 's'; frag.appendChild(s);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1) walk(n);
      });
    };
    walk(el);
  });

  /* ---------- Reveal + count-up + timeline ---------- */
  var countUp = function (el) {
    var end = parseFloat(el.getAttribute('data-count')), suf = el.getAttribute('data-suffix') || '', t0 = null, dur = 1400;
    if (reduce) { el.textContent = end + suf; return; }
    var step = function (t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 4);
      el.textContent = Math.round(end * e) + suf;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var t = e.target;
        t.classList.add('in');
        if (t.hasAttribute('data-count')) countUp(t);
        if (t.classList.contains('compare')) demoSweep(t);
        io.unobserve(t);
      });
    }, { threshold: 0.14, rootMargin: '0px 0px -40px 0px' });
    $$('.reveal, .split-words, [data-count], .timeline, .compare, .drip, .splash').forEach(function (el) { io.observe(el); });
  } else {
    $$('.reveal, .split-words, .timeline, .drip, .splash').forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- Rotating ticker ---------- */
  var tk = $('.tk-word');
  if (tk && !reduce) {
    var words = (tk.getAttribute('data-words') || '').split('|'), wi = 0;
    setInterval(function () {
      tk.classList.add('out');
      setTimeout(function () { wi = (wi + 1) % words.length; tk.textContent = words[wi]; tk.classList.remove('out'); }, 300);
    }, 2200);
  }

  /* ---------- Hero card tilt ---------- */
  var card = $('.hero-card');
  if (card && !reduce && matchMedia('(pointer:fine)').matches) {
    var vis = card.parentNode;
    vis.addEventListener('pointermove', function (e) {
      var r = vis.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
      card.style.transform = 'rotateY(' + (x * 8) + 'deg) rotateX(' + (-y * 8) + 'deg)';
    });
    vis.addEventListener('pointerleave', function () { card.style.transform = ''; });
  }

  /* ---------- Damage picker ---------- */
  var PICK = window.VD_PICKER || null, panel = $('#pickPanel');
  var setPick = function (key, scroll) {
    if (!PICK || !PICK[key] || !panel) return;
    var p = PICK[key], body = $('.pp-body', panel);
    $$('.ptile').forEach(function (t) { t.setAttribute('aria-pressed', t.getAttribute('data-key') === key); });
    body.classList.add('swap');
    setTimeout(function () {
      $('.pp-tag', panel).textContent = p.tag;
      $('h3', panel).textContent = p.title;
      $('.pp-desc', panel).textContent = p.desc;
      $('.pp-steps', panel).innerHTML = p.steps.map(function (s) { return '<li>' + s + '</li>'; }).join('');
      $('.pp-time', panel).textContent = p.time;
      $('.pp-cost', panel).textContent = p.cost;
      var more = $('.pp-more', panel); more.href = p.url; more.textContent = 'Read the full ' + p.short + ' guide';
      $('.pp-go', panel).setAttribute('data-service', p.service);
      body.classList.remove('swap');
    }, reduce ? 0 : 180);
    if (scroll && innerWidth < 980) panel.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    track('damage_pick', { damage: key });
  };
  $$('.ptile').forEach(function (t) { t.addEventListener('click', function () { setPick(t.getAttribute('data-key'), true); }); });

  /* ---------- Texture lab ---------- */
  var TEX = window.VD_TEXTURES || null;
  $$('.tex-tab').forEach(function (tab) {
    tab.addEventListener('click', function () {
      var k = tab.getAttribute('data-tex');
      $$('.tex-tab').forEach(function (x) { x.setAttribute('aria-selected', x === tab); });
      $$('.compare .layer').forEach(function (l) { l.className = l.className.replace(/\btx-\w+/g, '').trim() + ' tx-' + k; });
      if (TEX && TEX[k]) $('.tex-desc').textContent = TEX[k];
      track('texture_tab', { texture: k });
    });
  });
  var bindCompare = function (c) {
    var r = $('input[type=range]', c);
    if (!r) return;
    var set = function (v) { c.style.setProperty('--pos', v + '%'); r.value = v; };
    r.addEventListener('input', function () { c.dataset.touched = '1'; set(r.value); });
    c._set = set;
  };
  $$('.compare').forEach(bindCompare);
  function demoSweep(c) {
    if (reduce || !c._set) return;
    var t0 = null, dur = 2200;
    var step = function (t) {
      if (c.dataset.touched) return;
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      c._set(50 + Math.sin(p * Math.PI * 2) * 32);
      if (p < 1) requestAnimationFrame(step); else c._set(50);
    };
    setTimeout(function () { requestAnimationFrame(step); }, 400);
  }

  /* ---------- Gallery filter + lightbox ---------- */
  var lb = $('#lightbox'), lbImg = $('#lbImg'), lbCap = $('#lbCap'), shots = [], idx = 0, lastFocus = null;
  var collect = function () { shots = $$('.gallery figure:not(.hide)'); };
  var show = function (i) {
    if (!shots.length) return;
    idx = (i + shots.length) % shots.length;
    var img = $('img', shots[idx]);
    lbImg.src = img.currentSrc || img.src; lbImg.alt = img.alt;
    lbCap.textContent = ($('figcaption', shots[idx]) || {}).textContent || '';
  };
  var openLb = function (fig) { collect(); lastFocus = fig; show(shots.indexOf(fig)); lb.classList.add('open'); $('.lb-close', lb).focus(); };
  var closeLb = function () { lb.classList.remove('open'); if (lastFocus) lastFocus.focus(); };
  if (lb) {
    $$('.gallery figure').forEach(function (f) {
      f.tabIndex = 0; f.setAttribute('role', 'button');
      f.addEventListener('click', function () { openLb(f); });
      f.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openLb(f); } });
    });
    $('.lb-close', lb).addEventListener('click', closeLb);
    $('.lb-prev', lb).addEventListener('click', function () { show(idx - 1); });
    $('.lb-next', lb).addEventListener('click', function () { show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') closeLb(); if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1);
    });
  }
  $$('.filter').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-filter');
      $$('.filter').forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
      $$('.gallery figure').forEach(function (fig) { fig.classList.toggle('hide', f !== 'all' && fig.getAttribute('data-cat') !== f); });
    });
  });

  /* ---------- Confetti (reward moment) ---------- */
  var confetti = function () {
    if (reduce) return;
    var c = d.createElement('canvas'); c.className = 'confetti'; d.body.appendChild(c);
    var x = c.getContext('2d'), W = c.width = innerWidth, H = c.height = innerHeight;
    var cols = ['#F2B233', '#FFD36E', '#C8372D', '#FFFFFF', '#1A2F52'], P = [];
    for (var i = 0; i < 160; i++) P.push({ x: W / 2 + (Math.random() - 0.5) * 120, y: H * 0.55, vx: (Math.random() - 0.5) * 16, vy: -Math.random() * 18 - 6, s: Math.random() * 7 + 4, r: Math.random() * 6, vr: (Math.random() - 0.5) * 0.3, c: cols[i % cols.length] });
    var t = 0;
    (function f() {
      x.clearRect(0, 0, W, H);
      P.forEach(function (p) { p.vy += 0.45; p.vx *= 0.99; p.x += p.vx; p.y += p.vy; p.r += p.vr; x.save(); x.translate(p.x, p.y); x.rotate(p.r); x.fillStyle = p.c; x.fillRect(-p.s / 2, -p.s / 4, p.s, p.s / 2); x.restore(); });
      if (++t < 170) requestAnimationFrame(f); else c.remove();
    })();
  };

  /* ---------- Quote wizard ---------- */
  var form = $('#quoteForm');
  var goQuote = function (service) {
    if (form && service) {
      var r = $$('input[name="service"]', form).filter(function (i) { return i.value === service; })[0];
      if (r) { r.checked = true; r.dispatchEvent(new Event('change', { bubbles: true })); }
    }
    if (form) {
      var q = $('#quote'); if (q) q.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
      if (service && form._goto) form._goto(1);
    } else {
      location.href = '/free-estimate/' + (service ? '?service=' + encodeURIComponent(service) : '');
    }
  };
  d.addEventListener('click', function (e) {
    var b = e.target.closest('[data-quote]');
    if (b) { e.preventDefault(); goQuote(b.getAttribute('data-service') || ''); track('quote_cta', { service: b.getAttribute('data-service') || '' }); }
    var tel = e.target.closest('a[href^="tel:"]');
    if (tel) track('call_click', { number: tel.getAttribute('href') });
  });

  if (form) {
    form.noValidate = true;
    var steps = $$('.wz-step', form), cur = 0, fill = $('.wz-bar i', form), meter = $('.wz-meter span', form), meterTip = $('.wz-tip', form);
    var back = $('.wz-back', form), next = $('.wz-next', form), submit = $('.wz-submit', form), err = $('.wz-error', form);
    var picker = $('#photoPicker', form), thumbs = $('.thumbs', form), named = ['photo-1', 'photo-2', 'photo-3'].map(function (n) { return form.elements[n]; });
    var lead = form.elements['lead-source'];
    if (lead) { try { lead.value = (location.pathname + location.search).slice(0, 180) + (d.referrer ? ' | ref: ' + d.referrer.slice(0, 120) : ''); } catch (e) {} }

    var score = function () {
      var f = form.elements, s = 0, tip = '';
      if ($('input[name="service"]:checked', form)) s += 25; else tip = 'Pick what needs fixing';
      if ($('input[name="urgency"]:checked', form)) s += 8;
      if ($('input[name="property-type"]:checked', form)) s += 7;
      if (f['city'] && f['city'].value) s += 10; else if (!tip) tip = 'Add your city';
      var m = (f['message'] && f['message'].value.trim().length) || 0; s += Math.min(20, Math.round(m / 3));
      if (m < 60 && !tip) tip = 'A sentence or two about the damage helps';
      var hasPhoto = named.some(function (i) { return i && i.files && i.files.length; });
      if (hasPhoto) s += 20; else if (!tip) tip = 'Add a photo for +20%';
      if (f['name'] && f['name'].value.trim()) s += 5;
      if (f['phone'] && f['phone'].value.replace(/\D/g, '').length >= 10) s += 5;
      s = Math.min(100, s);
      if (meter) meter.textContent = s + '%';
      if (meterTip) meterTip.textContent = s >= 95 ? 'Perfect — that’s everything we need.' : tip;
    };
    var goto = function (i) {
      cur = Math.max(0, Math.min(steps.length - 1, i));
      steps.forEach(function (s, k) { s.classList.toggle('active', k === cur); });
      if (fill) fill.style.width = ((cur + 1) / steps.length * 100) + '%';
      back.hidden = cur === 0; next.hidden = cur === steps.length - 1; submit.hidden = cur !== steps.length - 1;
      $('.wz-count', form).textContent = 'Step ' + (cur + 1) + ' of ' + steps.length;
      err.classList.remove('show');
    };
    form._goto = goto;
    var valid = function (step) {
      var ok = true;
      $$('input, select, textarea', step).forEach(function (el) { if (ok && !el.checkValidity()) { ok = false; el.reportValidity(); } });
      return ok;
    };
    next.addEventListener('click', function () { if (valid(steps[cur])) { goto(cur + 1); track('quote_step', { step: cur + 1 }); var h = $('.wz-step.active h3', form); if (h) { h.tabIndex = -1; h.focus({ preventScroll: true }); } } });
    back.addEventListener('click', function () { goto(cur - 1); });
    // Auto-advance on step 1 choice — tiny dopamine hit, fewer taps
    $$('input[name="service"]', form).forEach(function (r) { r.addEventListener('change', function () { score(); if (cur === 0 && r.checked && !reduce) setTimeout(function () { goto(1); }, 260); else if (cur === 0) goto(1); }); });
    form.addEventListener('input', score); form.addEventListener('change', score);

    // Photos: one friendly picker distributed into three named inputs Netlify can store
    var setFiles = function (files) {
      files = Array.prototype.slice.call(files || [], 0, 3).filter(function (f) { return /^image\//.test(f.type); });
      thumbs.innerHTML = '';
      named.forEach(function (inp, k) {
        if (!inp) return;
        try { var dt = new DataTransfer(); if (files[k]) dt.items.add(files[k]); inp.files = dt.files; } catch (e) {}
      });
      files.forEach(function (f) { var im = new Image(); im.alt = 'Selected photo'; im.src = URL.createObjectURL(f); thumbs.appendChild(im); });
      var lbl = $('.drop-zone b', form); if (lbl) lbl.textContent = files.length ? files.length + ' photo' + (files.length > 1 ? 's' : '') + ' ready ✓' : 'Tap to add up to 3 photos';
      score();
    };
    if (picker) {
      picker.addEventListener('change', function () { setFiles(picker.files); });
      var dz = picker.parentNode;
      ['dragenter', 'dragover'].forEach(function (ev) { dz.addEventListener(ev, function (e) { e.preventDefault(); dz.classList.add('over'); }); });
      ['dragleave', 'drop'].forEach(function (ev) { dz.addEventListener(ev, function () { dz.classList.remove('over'); }); });
      dz.addEventListener('drop', function (e) { e.preventDefault(); setFiles(e.dataTransfer.files); });
    }
    // Downscale big phone photos so the whole submission stays under Netlify's upload limit
    var shrink = function (file) {
      return new Promise(function (res) {
        if (!file || file.size < 900000 || !window.createImageBitmap) return res(file);
        createImageBitmap(file).then(function (bmp) {
          var k = Math.min(1, 1800 / Math.max(bmp.width, bmp.height)), c = d.createElement('canvas');
          c.width = Math.round(bmp.width * k); c.height = Math.round(bmp.height * k);
          c.getContext('2d').drawImage(bmp, 0, 0, c.width, c.height);
          c.toBlob(function (b) { res(b ? new File([b], file.name.replace(/\.\w+$/, '') + '.jpg', { type: 'image/jpeg' }) : file); }, 'image/jpeg', 0.82);
        }).catch(function () { res(file); });
      });
    };
    form.addEventListener('submit', function (e) {
      if (!valid(steps[cur])) { e.preventDefault(); return; }
      if (!window.fetch || !window.FormData || !window.Promise) return; // native POST fallback
      e.preventDefault();
      submit.disabled = true; submit.textContent = 'Sending…';
      var fd = new FormData(form);
      Promise.all(named.map(function (inp) { return shrink(inp && inp.files && inp.files[0]); })).then(function (files) {
        named.forEach(function (inp, k) { if (!inp) return; fd.delete(inp.name); if (files[k]) fd.append(inp.name, files[k]); });
        return fetch('/', { method: 'POST', body: fd });
      }).then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        $('.wz-body', form).hidden = true;
        $('.wz-done', form).classList.add('show');
        confetti();
        track('generate_lead', { service: (form.elements['service'] && form.elements['service'].value) || '' });
        $('.wz-done', form).scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
      }).catch(function () {
        // Network or host issue: fall back to a normal form POST so the lead is never lost
        submit.textContent = 'Sending…';
        HTMLFormElement.prototype.submit.call(form);
      });
    });

    // Prefill from ?service= (used by service/city pages and ads)
    try {
      var sp = new URLSearchParams(location.search).get('service');
      if (sp) { var r0 = $$('input[name="service"]', form).filter(function (i) { return i.value === sp; })[0]; if (r0) { r0.checked = true; goto(1); } else goto(0); } else goto(0);
    } catch (e2) { goto(0); }
    score();
  }

  /* ---------- Hide mobile action bar while the quote form is on screen ---------- */
  var q = $('#quote');
  if (q && actionbar && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (es) { actionbar.classList.toggle('hide', es[0].isIntersecting); }, { threshold: 0.15 }).observe(q);
  }

  /* ---------- SOS chat (rule-based; only verified facts, never prices or hours) ---------- */
  var fab = $('#chatFab'), chat = $('#chat');
  if (fab && chat) {
    var log = $('#chatLog'), cf = $('#chatForm'), ci = $('#chatText');
    var CTA = '<br><a class="chip-cta" href="/free-estimate/" data-quote>Free estimate</a><a class="chip-cta" href="tel:+19415275924">Call (941) 527-5924</a>';
    var R = [
      [/mold|electric|structural|foundation|asbestos/i, 'Safety first: if you suspect mold, asbestos, an electrical hazard or a structural problem, have the right licensed pro assess it before any drywall work. Once the area is safe and dry, we handle the drywall and finish. Popcorn ceilings in older homes should be tested for asbestos before removal — see our <a href="/popcorn-ceiling-removal/">popcorn ceiling guide</a>.' + CTA],
      [/hurricane|storm|flood|water|leak|soft|stain|wet/i, 'We repair water- and storm-damaged drywall and ceilings — plumbing leaks, AC pan overflows, roof leaks and flood cuts — once the leak is fixed and the area is dry. Details: <a href="/water-damage-drywall-repair/">water damage repair</a>.' + CTA],
      [/popcorn|acoustic/i, 'Yes — we remove popcorn ceilings and refinish them smooth, knockdown or orange peel. Homes built before the mid-1980s should have the texture tested for asbestos first. <a href="/popcorn-ceiling-removal/">How it works</a>.' + CTA],
      [/texture|knockdown|orange peel|skip trowel|level ?5|match/i, 'Texture matching is our specialty — knockdown, orange peel, skip trowel, popcorn and smooth Level 5, plus exterior stucco. <a href="/texture-matching/">See how we match it</a>.' + CTA],
      [/ceiling|sag|crack/i, 'We repair ceiling cracks, sagging drywall, stains and nail pops, then blend the texture so the repair disappears. <a href="/ceiling-repair/">Ceiling repair</a>.' + CTA],
      [/price|cost|how much|estimate|quote|cheap|expensive/i, 'Every job is priced after we see it — estimates are free. For typical national price ranges (so you know what to expect), see our <a href="/drywall-repair-cost/">drywall repair cost guide</a>. Photos make your quote faster.' + CTA],
      [/hole|patch|dent|doorknob|nail pop|repair/i, 'Holes, dents, doorknob damage, nail pops, cracks — no job is too small. We patch, texture-match and leave it paint-ready. <a href="/drywall-repair/">Drywall repair</a>.' + CTA],
      [/property|landlord|realtor|rental|tenant|listing|investor|hoa/i, 'We work with property managers, landlords and realtors on turnover and listing-prep punch lists. <a href="/property-managers/">Punch-list repairs</a>.' + CTA],
      [/new construction|hang|install|remodel|addition|garage|finish/i, 'We hang, tape and finish drywall for remodels, additions and new construction — through to paint-ready. <a href="/new-construction-drywall/">New drywall &amp; remodels</a>.' + CTA],
      [/stucco|exterior/i, 'Yes — exterior stucco repair, matched to your existing texture. <a href="/stucco-repair/">Stucco repair</a>.' + CTA],
      [/paint|trim|baseboard|crown|carpentry|framing/i, 'We handle interior/exterior painting plus framing, carpentry and trim to finish the job. <a href="/painting-trim/">Painting &amp; trim</a>.' + CTA],
      [/photo|picture|image|send/i, 'Photos are the fastest route to a quote — you can attach up to 3 right in our <a href="/free-estimate/">estimate form</a>.' + CTA],
      [/north port|port charlotte|venice|sarasota|englewood|punta gorda|area|serve|where|location|near/i, 'We’re based in North Port and serve Port Charlotte, Venice, Sarasota, Englewood and Punta Gorda across Sarasota and Charlotte counties. <a href="/#areas">Service areas</a>. Nearby but not listed? Call and ask.' + CTA],
      [/license|licensed|insur|lic\b/i, 'Veteran Drywall LLC holds Florida license # SCC131152687 — you can verify it on the state’s <a href="https://www.myfloridalicense.com/wl11.asp" target="_blank" rel="noopener">DBPR license lookup</a>. Need documentation for an HOA or property manager? Ask when you request your estimate.'],
      [/veteran|marine|usmc|owner|steven|who/i, 'Veteran Drywall is owned by Steven McPherson, a U.S. Marine Corps veteran with 10+ years of service and four overseas deployments. He works with his crew, Mike and Rick. <a href="/about/">Our story</a>.'],
      [/hour|open|today|weekend|when|schedule|available|emergency|asap|urgent/i, 'For anything urgent, call (941) 527-5924 — Steven answers his own phone. I won’t promise hours or availability I can’t confirm; the team will give you a real date.' + CTA],
      [/^(hi|hello|hey|yo|sup)\b/i, 'Hey! Tell me what you’re looking at — a hole, crack, ceiling stain, water damage, popcorn ceiling or a remodel — and I’ll point you to the right next step.']
    ];
    var FALL = 'Good question — I don’t want to guess. The team will give you a straight answer: call (941) 527-5924 or send a free estimate request.' + CTA;
    var add = function (html, who) { var m = d.createElement('div'); m.className = 'msg ' + who; if (who === 'bot') m.innerHTML = html; else m.textContent = html; log.appendChild(m); log.scrollTop = log.scrollHeight; return m; };
    var ask = function (q) {
      add(q, 'user');
      var t = d.createElement('div'); t.className = 'msg bot typing'; t.innerHTML = '<i></i><i></i><i></i>'; log.appendChild(t); log.scrollTop = log.scrollHeight;
      setTimeout(function () { t.remove(); var hit = R.filter(function (x) { return x[0].test(q); })[0]; add(hit ? hit[1] : FALL, 'bot'); }, reduce ? 0 : 650);
      track('chat_question');
    };
    var openC = function () { chat.classList.add('open'); fab.setAttribute('aria-expanded', 'true'); if (!log.children.length) add('SOS drywall help is here. What are you looking at — a hole, crack, ceiling stain, water damage, texture issue or a remodel?', 'bot'); ci.focus(); };
    var closeC = function () { chat.classList.remove('open'); fab.setAttribute('aria-expanded', 'false'); fab.focus(); };
    fab.addEventListener('click', function () { chat.classList.contains('open') ? closeC() : openC(); });
    $('#chatX').addEventListener('click', closeC);
    addEventListener('keydown', function (e) { if (e.key === 'Escape' && chat.classList.contains('open')) closeC(); });
    $('#chatStarters').addEventListener('click', function (e) { var b = e.target.closest('button'); if (b) ask(b.textContent); });
    cf.addEventListener('submit', function (e) { e.preventDefault(); var v = ci.value.trim(); if (v) { ci.value = ''; ask(v); } });
  }

  /* ---------- Footer year ---------- */
  $$('.yr').forEach(function (y) { y.textContent = new Date().getFullYear(); });

  window.VD_OK = true;
})();
