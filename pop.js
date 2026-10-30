(function () {
  var INFO = {
    call: { title: '전화 상담', num: '055-286-2064', href: 'tel:0552862064', go: '전화 걸기',
            note: '영업시간 외에도 문자로 상담하실 수 있습니다.' },
    sms:  { title: '문자 상담', num: '010-0000-0000', href: 'sms:01000000000', go: '문자 보내기',
            note: '영업시간 외에도 문자로 상담하실 수 있습니다.' }
  };
  var box, last;
  function build() {
    box = document.createElement('div');
    box.className = 'pop';
    box.hidden = true;
    box.innerHTML =
      '<div class="pop-bg" data-x></div>' +
      '<div class="pop-card" role="dialog" aria-modal="true" aria-labelledby="pop-t">' +
      '<p class="pop-t" id="pop-t"></p><p class="pop-n"></p><p class="pop-s"></p>' +
      '<div class="pop-b"><button type="button" class="btn btn-ghost pop-copy">번호 복사</button>' +
      '<a class="btn pop-go"></a></div>' +
      '<button type="button" class="pop-x" data-x aria-label="닫기">닫기</button></div>';
    document.body.appendChild(box);
    box.addEventListener('click', function (e) { if (e.target.hasAttribute('data-x')) close(); });
    box.querySelector('.pop-copy').addEventListener('click', function (e) {
      var n = box.querySelector('.pop-n').textContent, b = e.currentTarget;
      function done() { b.textContent = '복사됐어요'; setTimeout(function () { b.textContent = '번호 복사'; }, 1500); }
      if (navigator.clipboard) navigator.clipboard.writeText(n).then(done, function () {});
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !box.hidden) close(); });
  }
  function open(k, from) {
    if (!box) build();
    var d = INFO[k];
    box.querySelector('.pop-t').textContent = d.title;
    box.querySelector('.pop-n').textContent = d.num;
    box.querySelector('.pop-s').textContent = d.note;
    var go = box.querySelector('.pop-go'); go.textContent = d.go; go.href = d.href;
    last = from; box.hidden = false; document.body.style.overflow = 'hidden';
    box.querySelector('.pop-x').focus();
  }
  function close() { box.hidden = true; document.body.style.overflow = ''; if (last) last.focus(); }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-pop]');
    if (!a) return;
    e.preventDefault();
    open(a.getAttribute('data-pop'), a);
  });
})();

// 푸터 로고의 높이를 푸터 글 블록의 높이에 맞춘다 (넓은 화면에서만).
(function () {
  var t = document.querySelector('.foot-text'), l = document.querySelector('.foot-logo');
  if (!t || !l) return;
  function fit() {
    if (window.innerWidth < 620) { l.style.width = l.style.height = ''; return; }
    var h = Math.round(t.getBoundingClientRect().height);
    l.style.setProperty('width', h + 'px', 'important');
    l.style.setProperty('height', h + 'px', 'important');
  }
  fit();
  window.addEventListener('resize', fit);
  window.addEventListener('load', fit);
})();

// 프로필 사진 좌우 넘기기
(function () {
  document.querySelectorAll('.slider').forEach(function (sl) {
    var box = sl.querySelector('.slides'), n = box.children.length, dots = sl.querySelector('.sl-dots');
    for (var i = 0; i < n; i++) dots.appendChild(document.createElement('i'));
    function cur() { return Math.round(box.scrollLeft / box.clientWidth); }
    function mark() { Array.prototype.forEach.call(dots.children, function (d, k) { d.className = k === cur() ? 'on' : ''; }); }
    function go(k) { box.scrollTo({ left: ((k % n) + n) % n * box.clientWidth, behavior: 'smooth' }); }
    sl.querySelector('.prev').addEventListener('click', function () { go(cur() - 1); });
    sl.querySelector('.next').addEventListener('click', function () { go(cur() + 1); });
    box.addEventListener('scroll', mark, { passive: true });
    mark();
  });
})();
