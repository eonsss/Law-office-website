(function () {
  const { TABLES, FIXED, calc } = window.FEE;
  const $ = (id) => document.getElementById(id);
  const kind = $('kind'), amount = $('amount'), quick = $('quick');
  const rValue = $('rValue'), rSub = $('rSub'), hint = $('hint') || $('amountHint');

  const won = (n) => n.toLocaleString('ko-KR') + '원';
  const short = (n) => {
    const eok = Math.floor(n / 1e8), man = Math.round((n % 1e8) / 1e4);
    return (eok ? eok + '억' : '') + (man ? (eok ? ' ' : '') + man.toLocaleString('ko-KR') + '만' : '') + '원';
  };

  Object.entries(TABLES).forEach(([k, t]) => kind.add(new Option(t.name, k)));
  Object.entries(FIXED).forEach(([k, t]) => kind.add(new Option(t.name, k)));

  function render() {
    const key = kind.value, t = TABLES[key], f = FIXED[key];
    const field = amount.closest('.field');
    quick.innerHTML = '';
    if (f) {
      $('amountLabel').textContent = '금액 입력 불필요';
      amount.value = '';
      amount.disabled = true;
      $('amountHint').textContent = '말소등기는 금액과 관계없이 정액입니다.';
      rValue.classList.remove('empty');
      rValue.textContent = won(f.fee);
      rSub.textContent = '부가세·공과금 별도';
      return;
    }
    amount.disabled = false;
    $('amountLabel').textContent = t.label;
    $('amountHint').textContent = t.hint;
    t.quick.forEach((v) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.textContent = short(v);
      b.onclick = () => { amount.value = v.toLocaleString('ko-KR'); update(); };
      quick.appendChild(b);
    });
    update();
  }

  function update() {
    const key = kind.value;
    if (FIXED[key]) return;
    const n = parseInt(amount.value.replace(/[^\d]/g, ''), 10);
    if (!n) {
      rValue.classList.add('empty');
      rValue.textContent = '금액을 입력해 주세요';
      rSub.textContent = TABLES[key].extra || '';
      return;
    }
    const fee = calc(TABLES[key], n);
    rValue.classList.remove('empty');
    rValue.textContent = won(fee);
    rSub.textContent = short(n) + ' 기준 · 부가세·공과금 별도' + (TABLES[key].extra ? ' · ' + TABLES[key].extra : '');
  }

  amount.addEventListener('input', () => {
    const d = amount.value.replace(/[^\d]/g, '').slice(0, 13);
    amount.value = d ? Number(d).toLocaleString('ko-KR') : '';
    update();
  });
  kind.addEventListener('change', () => { amount.value = ''; render(); });
  render();

  // nav shadow
  const nav = $('nav');
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // reveal on scroll
  const els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((es) => es.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { threshold: 0.12 });
    els.forEach((el) => io.observe(el));
  } else els.forEach((el) => el.classList.add('in'));
})();
