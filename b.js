(function () {
  var nav = document.getElementById('nav');
  var f = function () { nav.classList.toggle('scrolled', window.scrollY > 8); };
  f(); window.addEventListener('scroll', f, { passive: true });
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else els.forEach(function (el) { el.classList.add('in'); });
})();
