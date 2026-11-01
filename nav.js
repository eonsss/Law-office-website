// 메뉴를 눌렀을 때 페이지 전체를 새로 불러오지 않고 본문만 바꾼다.
// 글꼴·CSS·머리글·바닥글을 다시 받거나 다시 그리지 않아 이동이 빠르다.
// 문제가 생기면 언제나 일반 페이지 이동으로 되돌아간다.
(function () {
  if (!(window.fetch && window.history && history.pushState && window.DOMParser && window.URL)) return;
  var cache = {}, pending = {}, busy = false;
  var KEEP = /(?:^|\/)(?:pop|b|nav)\.js(?:\?|$)/;

  function pageUrl(a) {
    if (!a || !a.href || (a.target && a.target !== '_self') || a.hasAttribute('download')) return null;
    var u = new URL(a.href, location.href);
    if (u.origin !== location.origin || !/(\.html|\/)$/.test(u.pathname)) return null;
    return u;
  }
  function get(u) {
    var k = u.pathname;
    if (cache[k]) return Promise.resolve(cache[k]);
    if (!pending[k]) {
      pending[k] = fetch(k, { credentials: 'same-origin' }).then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.text();
      }).then(function (t) { cache[k] = t; delete pending[k]; return t; },
              function (e) { delete pending[k]; throw e; });
    }
    return pending[k];
  }
  function loadScripts(list, i, done) {
    if (i >= list.length) return done();
    var src = list[i];
    if (/calc\.js/.test(src) && window.FEE) return loadScripts(list, i + 1, done); // 전역 상수라 한 번만 실행
    var s = document.createElement('script');
    s.src = src;
    s.onload = s.onerror = function () { s.remove(); loadScripts(list, i + 1, done); };
    document.body.appendChild(s);
  }
  function show(u, push) {
    return get(u).then(function (html) {
      var doc = new DOMParser().parseFromString(html, 'text/html');
      var main = doc.querySelector('main'), cur = document.querySelector('main');
      if (!main || !cur) throw new Error('no main');
      cur.innerHTML = main.innerHTML;
      document.title = doc.title;
      ['.menu', '.tabs'].forEach(function (sel) {
        var a = document.querySelector(sel), b = doc.querySelector(sel);
        if (a && b) a.innerHTML = b.innerHTML;
      });
      if (push) history.pushState(null, '', u.pathname + u.search + u.hash);
      window.scrollTo(0, 0);
      var srcs = [].map.call(doc.querySelectorAll('body script[src]'), function (s) { return s.getAttribute('src'); })
        .filter(function (s) { return !KEEP.test(s); });
      loadScripts(srcs, 0, function () {
        if (window.siteInit) window.siteInit();
        if (u.hash) { var t = document.getElementById(u.hash.slice(1)); if (t) t.scrollIntoView(); }
      });
    });
  }
  function go(u, push) {
    if (busy) return;
    busy = true;
    var t = setTimeout(function () { location.href = u.href; }, 5000);
    show(u, push).then(function () { clearTimeout(t); busy = false; },
      function () { clearTimeout(t); busy = false; location.href = u.href; });
  }

  document.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest && e.target.closest('a');
    var u = pageUrl(a);
    if (!u) return;
    if (u.pathname === location.pathname && u.search === location.search) return; // 같은 페이지(해시 이동 등)는 기본 동작
    e.preventDefault();
    go(u, true);
  });
  window.addEventListener('popstate', function () { go(new URL(location.href), false); });

  // 눌러 보기 전에 미리 받아 두기: 손이 닿거나 마우스를 올릴 때, 그리고 화면이 뜬 뒤 한가할 때
  function warm(e) {
    var u = pageUrl(e.target.closest && e.target.closest('a'));
    if (u && u.pathname !== location.pathname) get(u).catch(function () {});
  }
  document.addEventListener('touchstart', warm, { passive: true });
  document.addEventListener('mouseover', warm);
  window.addEventListener('load', function () {
    setTimeout(function () {
      [].forEach.call(document.querySelectorAll('.menu a'), function (a) {
        var u = pageUrl(a);
        if (u && u.pathname !== location.pathname) get(u).catch(function () {});
      });
    }, 600);
  });
})();
