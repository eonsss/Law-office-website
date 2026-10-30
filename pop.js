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
