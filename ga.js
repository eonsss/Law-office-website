// 방문 통계(구글 애널리틱스 GA4)와 주요 버튼 클릭 기록.
// 메뉴 이동(nav.js)은 GA4 기본 설정(브라우저 기록 변경 시 페이지뷰)이 자동으로 센다.
(function () {
  var ID = 'G-B27CZJTQ6P';
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { dataLayer.push(arguments); };
  gtag('js', new Date());
  gtag('config', ID);
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID;
  document.head.appendChild(s);

  function send(name, el, extra) {
    var p = { page: location.pathname.replace(/^.*\//, '') || 'index.html',
              button: (el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40) };
    for (var k in extra) p[k] = extra[k];
    gtag('event', name, p);
  }
  // 캡처 단계에서 받아 팝업(pop.js)이 기본 동작을 막아도 기록된다.
  document.addEventListener('click', function (e) {
    var el = e.target.closest && e.target.closest('a,button,[role=tab]');
    if (!el) return;
    var pop = el.getAttribute('data-pop'), h = el.getAttribute('href') || '';
    if (pop === 'call') return send('click_call_button', el);       // 전화 상담 버튼 (팝업 열림)
    if (pop === 'sms') return send('click_sms_button', el);         // 문자 상담 버튼 (팝업 열림)
    if (/^tel:/.test(h)) return send('call_start', el, { number: h.slice(4) });  // 실제 전화 걸기
    if (/^sms:/.test(h)) return send('sms_start', el, { number: h.slice(4) });   // 실제 문자 보내기
    if (/^mailto:/.test(h)) return send('click_email', el);
    if (el.classList.contains('pop-copy')) return send('copy_number', el, { number: (document.querySelector('.pop-n') || {}).textContent });
    if (/map\.naver\.com/.test(h)) return send('click_map', el);
    if (/blog\.naver\.com/.test(h)) return send('click_blog', el);
    if (el.getAttribute('role') === 'tab') return send('process_tab', el, { tab: el.getAttribute('aria-controls') });
  }, true);
})();
