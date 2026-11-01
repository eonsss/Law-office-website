// 업무별 절차 탭: 누른 업무만 보이게 하고, 주소의 #auction 같은 해시로 바로 열 수 있게 한다.
(function () {
  var tabs = [].slice.call(document.querySelectorAll('.ptabs [role=tab]'));
  if (!tabs.length) return;
  function show(id, push) {
    var ok = tabs.some(function (t) { return t.getAttribute('aria-controls') === id; });
    if (!ok) id = tabs[0].getAttribute('aria-controls');
    tabs.forEach(function (t) {
      var on = t.getAttribute('aria-controls') === id;
      t.setAttribute('aria-selected', on); t.classList.toggle('on', on); t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if (push && history.replaceState) history.replaceState(null, '', '#' + id);
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function (e) { e.preventDefault(); show(t.getAttribute('aria-controls'), true); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (!d) return;
      var n = tabs[(i + d + tabs.length) % tabs.length]; n.focus(); n.click();
    });
  });
  window.addEventListener('hashchange', function () { show(location.hash.slice(1)); });
  show(location.hash.slice(1));
})();
