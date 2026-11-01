(function () {
  var nav = document.getElementById('nav');
  var f = function () { nav.classList.toggle('scrolled', window.scrollY > 8); };
  f(); window.addEventListener('scroll', f, { passive: true });
  var io = 'IntersectionObserver' in window && new IntersectionObserver(function (es) { es.forEach(function (e) {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: 0.12 });
  // 페이지가 처음 뜰 때와, 본문이 바뀐 뒤(nav.js)에 호출한다.
  window.siteInit = function () {
    document.querySelectorAll('.reveal:not(.in)').forEach(function (el) { if (io) io.observe(el); else el.classList.add('in'); });
    if (window.siteSliders) window.siteSliders();
  };
  window.siteInit();
})();
