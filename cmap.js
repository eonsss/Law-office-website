// 상담 문의: PC 화면에서 지도 아래쪽을 '창원지방법원 마산지원 도보 1분' 줄 아래쪽에 맞춘다.
(function () {
  var map = document.querySelector('.cvisit .map'), addr = document.getElementById('addr'), info = document.querySelector('.cvisit .info');
  if (!map || !addr || !info) return;
  var mq = window.matchMedia('(min-width:820px)');
  function fit() {
    if (!document.contains(map)) return;
    if (!mq.matches) { map.style.height = ''; map.style.aspectRatio = ''; return; }
    var h = addr.getBoundingClientRect().bottom - info.getBoundingClientRect().top;
    if (h > 200) { map.style.aspectRatio = 'auto'; map.style.height = Math.round(h) + 'px'; }
  }
  fit();
  window.addEventListener('resize', fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
  window.addEventListener('load', fit);
})();
