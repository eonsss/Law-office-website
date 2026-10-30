# B 버전 페이지 생성기: 기획안의 메뉴 6개 구조(소개/법무사 업무/행정사 업무/비용 안내/사례·후기/상담 문의)
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEL = '055-286-2064'
VER = '20261030o'  # 정적 파일 캐시를 깨기 위한 버전. 파일을 고칠 때 값을 바꾼다.
NAV = [('about.html','사무소 소개'),('legal.html','법무사 업무'),('admin.html','행정사 업무'),
       ('fees.html','비용 안내'),('cases.html','사례·후기'),('contact.html','상담 문의')]
MAP = 'https://map.naver.com/p/search/%EB%B2%95%EB%AC%B4%EC%82%AC%20%ED%96%89%EC%A0%95%EC%82%AC%20%EC%9C%A0%EB%B3%91%EC%97%B4%20%EC%82%AC%EB%AC%B4%EC%86%8C'

def page(fn, title, desc, body, scripts='<script src="b.js?v='+VER+'"></script>'):
    menu = ''.join(f'<a href="{h}"{" class=on" if h==fn else ""}>{t}</a>' for h,t in NAV)
    html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | 유병열 법무사·행정사 사무소</title>
<meta name="description" content="{desc}">
<link rel="icon" href="img/emblem.jpg">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="style.css?v={VER}">
<link rel="stylesheet" href="b.css?v={VER}">
</head>
<body>
<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="brand" href="index.html" aria-label="유병열 법무사·행정사 사무소 홈"><img src="img/emblem.jpg" alt="" width="44" height="41"><span class="bt"><b>유병열</b><small>법무사·행정사</small></span></a>
    <nav class="menu bmenu">{menu}</nav>
    <span class="hbtns"><a class="btn btn-sm" href="tel:0552862064" data-pop="call">전화 상담</a><a class="btn btn-sm" href="sms:01000000000" data-pop="sms">문자 상담</a></span>
  </div>
  <nav class="wrap tabs">{menu}</nav>
</header>
<main>
{body}
</main>
<footer class="footer">
  <div class="wrap foot-in">
    <div class="foot-text">
    <p>유병열 법무사·행정사 사무소 · 경남지방법무사회 소속<br>창원시 마산합포구 3·15대로 217, 2층 (중앙동 3가)<br>전화 {TEL} · 휴대폰 010-0000-0000<br>팩스 055-224-2064<br>byryu210@gmail.com</p>
    <p class="copy">© 유병열 법무사·행정사 사무소. 이 사이트의 내용은 일반적인 안내이며 개별 사건에 대한 법률 판단이 아닙니다.</p>
    </div>
    <img class="foot-logo" src="img/logo-square.png" alt="유병열 법무사·행정사 사무소" width="96" height="96">
  </div>
</footer>
<div class="fabs"><a href="tel:0552862064" data-pop="call">전화 상담</a><a href="sms:01000000000" data-pop="sms">문자 상담</a></div>
<script src="pop.js?v={VER}"></script>
{scripts}
</body>
</html>
'''
    open(os.path.join(OUT, fn), 'w', encoding='utf-8').write(html)

def head(eyebrow, h1, sub=''):
    s = f'<p class="sub">{sub}</p>' if sub else ''
    return f'<section class="phead"><div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1>{s}</div></section>'

CTA = f'''<section class="section tinted"><div class="wrap ctabox reveal">
<div><h2>먼저 편하게 문의해 보세요</h2><p class="sub">사안에 따라 진행 방식과 비용이 달라질 수 있어 상담 후 안내해 드립니다.</p></div>
<div class="cta"><a class="btn" href="tel:0552862064" data-pop="call">전화 상담</a><a class="btn" href="sms:01000000000" data-pop="sms">문자 상담</a></div>
</div></section>'''

# ---------- 홈
home = f'''
<section class="hero">
  <div class="wrap hero-in">
    <p class="eyebrow reveal">창원지방법원 마산지원 도보 1분</p>
    <h1 class="reveal">복잡한 법원 서류,<br>처음부터 끝까지 직접 챙깁니다.</h1>
    <p class="lead reveal">부동산 경매입찰과 등기, 개인회생·파산, 상속까지.<br class="pc">법무사·행정사가 직접 상담하고 직접 작성합니다.</p>
    <div class="cta reveal"><a class="btn" href="tel:0552862064" data-pop="call">전화 상담</a><a class="btn" href="sms:01000000000" data-pop="sms">문자 상담</a><a class="btn btn-ghost" href="fees.html">예상 보수 계산</a></div>
  </div>
  <div class="wrap hero-photo reveal"><img src="img/exterior.jpg" alt="마산합포구 3·15대로변 유병열 법무사·행정사 사무소 전경" width="1600" height="1200"></div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">업무 안내</p>
    <h2>어떤 일이 필요하신가요?</h2>
    <div class="grid cards">
      <a class="card link reveal" href="legal.html#auction"><span class="num">경매·공매</span><h3>부동산 경매입찰</h3><p>입찰 서류 작성과 매수신청 대리, 낙찰 후 등기까지.</p><span class="more">자세히 보기</span></a>
      <a class="card link reveal" href="legal.html#registry"><span class="num">등기</span><h3>부동산 등기</h3><p>매매·증여·상속 소유권이전, 근저당 설정과 말소.</p><span class="more">자세히 보기</span></a>
      <a class="card link reveal" href="legal.html#rehab"><span class="num">채무</span><h3>개인회생·파산</h3><p>신청서와 변제계획안 등 서류 작성. 상담은 비밀이 유지됩니다.</p><span class="more">자세히 보기</span></a>
      <a class="card link reveal" href="legal.html#inherit"><span class="num">상속</span><h3>상속 서류</h3><p>상속등기, 상속포기·한정승인 심판청구서 작성.</p><span class="more">자세히 보기</span></a>
    </div>
    <p class="note"><a class="tl" href="legal.html">법무사 업무 전체 보기</a> · <a class="tl" href="admin.html">행정사 업무 전체 보기</a></p>
  </div>
</section>

<section class="section tinted">
  <div class="wrap about">
    <div class="about-photo reveal"><img src="img/ceo.jpg" alt="유병열 법무사·행정사" loading="lazy" width="506" height="900"></div>
    <div class="about-text">
      <p class="eyebrow">대표 소개</p>
      <h2>유병열 법무사·행정사</h2>
      <p class="lead2">서류 하나하나를 직접 확인하고, 처음 오신 분도 이해할 수 있게 설명드립니다.</p>
      <ul class="badges"><li>법무사</li><li>행정사</li><li>경남지방법무사회 소속</li></ul>
      <a class="btn" href="about.html">대표 소개 더 보기</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap steps">
    <div><p class="eyebrow">진행 순서</p><h2>상담부터 완료까지</h2></div>
    <ol class="flow">
      <li class="reveal"><b>상담</b><span>전화·방문으로 상황을 말씀해 주세요.</span></li>
      <li class="reveal"><b>서류 안내</b><span>필요한 서류와 예상 기간을 안내해 드립니다.</span></li>
      <li class="reveal"><b>접수·진행</b><span>서류를 작성하고 법원·등기소에 접수합니다.</span></li>
      <li class="reveal"><b>완료</b><span>결과를 확인하고 서류를 전달해 드립니다.</span></li>
    </ol>
  </div>
</section>

<section class="section tinted">
  <div class="wrap visit">
    <div>
      <p class="eyebrow">오시는 길</p><h2>법원에서 걸어서 1분</h2>
      <p class="sub">창원시 마산합포구 3·15대로변, 창원지방법원 마산지원에서 도보 1분 거리입니다.</p>
      <div class="cta" style="margin-top:24px"><a class="btn" href="{MAP}" target="_blank" rel="noopener">네이버 지도에서 보기</a><a class="btn btn-ghost" href="contact.html">연락처 보기</a></div>
    </div>
    <a class="map reveal" href="{MAP}" target="_blank" rel="noopener" aria-label="네이버 지도에서 사무소 위치 보기"><img src="img/map.jpg?v={VER}" alt="사무소 위치 지도" loading="lazy"></a>
  </div>
</section>
'''
page('index.html', '마산 경매·개인회생·상속등기', '창원지방법원 마산지원 도보 1분. 부동산 경매입찰·등기, 개인회생·파산, 상속 서류 작성을 법무사·행정사가 직접 상담합니다.', home)

# ---------- 소개
about = head('사무소 소개', '처음부터 끝까지 직접 처리하는 법무사·행정사', '2023년부터 현 위치에서 운영중입니다.') + '''
<section class="section"><div class="wrap about">
  <div class="about-photo reveal"><img src="img/ceo.jpg" alt="유병열 법무사·행정사" width="506" height="900"></div>
  <div class="about-text">
    <h2>유병열</h2>
    <p class="lead2">처음 오신 분도 이해할 수 있게 쉬운 말로 설명드립니다.</p>
    <dl class="career">
      <div><dt>학력</dt><dd>마산상업고등학교 졸업<br>한국방송통신대학교 법학 전공</dd></div>
      <div><dt>자격</dt><dd>법무사<br>행정사</dd></div>
      <div><dt>소속</dt><dd>경남지방법무사회</dd></div>
      <div><dt>사무소</dt><dd>2023년부터 현 위치에서 운영중</dd></div>
    </dl>
  </div>
</div></section>
<section class="section tinted"><div class="wrap">
  <p class="eyebrow">사무소 둘러보기</p><h2>편하게 들러 상담하세요</h2>
  <div class="gallery">
    <img class="reveal" src="img/desk.jpg" alt="서류를 작성하는 사무소 내부" loading="lazy">
    <img class="reveal" src="img/interior.jpg" alt="사무소 상담 공간" loading="lazy">
    <img class="reveal" src="img/shelf.jpg" alt="법률 서적이 꽂힌 사무소 서가" loading="lazy">
    <img class="reveal" src="img/street.jpg" alt="3·15대로 간판과 사무소 입구" loading="lazy">
  </div>
</div></section>''' + CTA
page('about.html', '사무소 소개', '유병열 법무사·행정사 대표 소개와 사무소 안내. 경남지방법무사회 소속.', about)

# ---------- 법무사 업무
def svc(id_, num, name, who, items, extra=''):
    li = ''.join(f'<li>{i}</li>' for i in items)
    return f'''<article class="svc reveal" id="{id_}"><div class="svc-h"><span class="num">{num}</span><h2>{name}</h2></div>
<p class="svc-who">{who}</p><ul class="check">{li}</ul>{extra}</article>'''
legal = head('법무사 업무', '주력 업무를 자세히 안내드립니다', '진행 방식과 비용은 사안에 따라 달라질 수 있어, 구체적인 내용은 상담 때 안내해 드립니다.') + '<section class="section"><div class="wrap svcs">' + \
  svc('auction','01','부동산 경매입찰','경매로 부동산을 사려는 분, 입찰 절차가 낯선 분','입찰 서류 작성|매수신청 대리|낙찰 후 소유권이전등기'.split('|')) + \
  svc('registry','02','부동산 등기','집을 사고팔거나 증여하는 분, 대출을 받거나 갚는 분','매매·증여에 따른 소유권이전|근저당권 설정|근저당권 말소'.split('|')) + \
  svc('rehab','03','개인회생·파산','채무 때문에 어려움을 겪는 분','신청서 작성|변제계획안 작성|필요 서류 안내와 제출 대행'.split('|'), '<p class="svc-note">상담 내용은 비밀이 유지됩니다.</p>') + \
  svc('inherit','04','상속','가족이 돌아가셔서 재산 정리가 필요한 분','상속등기|상속포기·한정승인 심판청구서 작성|필요 서류 안내'.split('|'), '<p class="svc-note">상속 세금 관련 상담은 세무사 업무라 해당 전문가를 안내해 드립니다.</p>') + \
  '</div></section>' + CTA
page('legal.html', '법무사 업무', '부동산 경매입찰·등기, 개인회생·파산, 상속 서류 작성 등 법무사 업무 안내.', legal)

# ---------- 행정사
admin = head('행정사 업무', '행정 서류도 함께 도와드립니다', '행정사 업무 범위는 사안에 따라 달라 상담 때 정확히 안내해 드립니다.') + '<section class="section"><div class="wrap svcs">' + \
  svc('appeal','01','행정심판','행정기관의 처분이 억울하다고 느끼시는 분','행정심판 청구서 작성|필요 서류 안내'.split('|')) + \
  svc('permit','02','인허가·신고','영업이나 사업에 필요한 허가·신고를 준비하시는 분','각종 인허가·신고 서류 작성|제출 대행'.split('|')) + \
  '</div></section>' + CTA
page('admin.html', '행정사 업무', '행정심판 청구서 작성, 각종 인허가·신고 서류 작성 등 행정사 업무 안내.', admin)

# ---------- 비용 안내 (계산기 포함)
fees = head('비용 안내', '예상 보수를 미리 확인해 보세요', '대한법무사협회 <b>법무사보수표(2026. 8. 20. 자료 기준)</b>의 기본보수 <b class="hl">상한액</b> <span class="nb">산정 방법으로 계산합니다.</span>') + '''
<section class="section"><div class="wrap">
    <div class="calc reveal">
      <div class="field"><label for="kind">업무 종류</label><select id="kind"></select></div>
      <div class="field">
        <label for="amount" id="amountLabel">금액</label>
        <div class="amount-box"><input id="amount" inputmode="numeric" autocomplete="off" placeholder="0"><span>원</span></div>
        <p class="hint" id="amountHint"></p><div class="quick" id="quick"></div>
      </div>
      <div class="result" id="result" aria-live="polite"><span class="r-label">예상 기본보수 (<b class="hl">상한액</b>)</span><strong class="r-value" id="rValue">금액을 입력해 주세요</strong><span class="r-sub" id="rSub"></span></div>
    </div>
    <ul class="fine">
      <li>표의 금액은 기본보수의 <b class="hl">상한액</b>이며, 사건의 내용에 따라 달라질 수 있습니다. 정확한 금액은 상담 후 안내해 드립니다.</li>
      <li><b class="hl">부가가치세와 등록면허세·교육세·인지·송달료 등 공과금은 포함되지 않습니다.</b></li>
      <li>계산 결과는 참고용입니다.</li>
    </ul>
    <div class="consult reveal"><div><h3>상담 비용 안내</h3><p>30분까지 <b>50,000원</b>, 30분을 초과하면 30분마다 <b>20,000원</b>이 추가됩니다. <span class="hl2">사건을 맡기시는 경우에는 상담료가 적용되지 않습니다.</span></p></div></div>
</div></section>
<section class="section tinted"><div class="wrap"><p class="eyebrow">자주 받는 질문</p><h2>자주 묻는 질문</h2><p class="sub">자주 받는 질문은 곧 등록할 예정입니다. 궁금한 점은 전화로 편하게 문의해 주세요.</p></div></section>''' + CTA
page('fees.html', '비용 안내와 보수 계산기', '법무사보수표 기준 예상 보수 계산기와 상담 비용 안내.', fees,
     '<script src="calc.js?v='+VER+'"></script><script src="main.js?v='+VER+'"></script>')

# ---------- 사례·후기
cases = head('사례·후기', '처리 사례와 후기', '의뢰인 정보가 드러나지 않도록 동의를 받은 내용만 게시합니다.') + '''
<section class="section"><div class="wrap">
  <div class="empty reveal"><h3>사례와 후기를 준비하고 있어요</h3><p>그동안의 업무 이야기는 블로그에서 먼저 확인하실 수 있습니다.</p>
  <a class="btn" href="https://blog.naver.com/byryu2101" target="_blank" rel="noopener">네이버 블로그 가기</a></div>
</div></section>'''
page('cases.html', '사례·후기', '유병열 법무사·행정사 사무소의 처리 사례와 블로그.', cases)

# ---------- 상담 문의
contact = head('상담 문의', '전화 한 통이면 충분합니다') + f'''
<section class="section"><div class="wrap visit">
  <div>
    <ul class="info">
      <li><span>영업시간</span><div class="hours"><p><b>(평일)</b> 09시 ~ 18시</p><p><b>(주말)</b> 09시 ~ 13시</p><p class="hours-note">전화 또는 문자로 영업시간 외에도 상담 가능합니다.</p></div></li>
      <li><span>전화</span><a href="tel:0552862064">{TEL}</a></li>
      <li><span>휴대폰</span><a href="tel:01000000000">010-0000-0000</a></li>
      <li><span>팩스</span><b class="blue">055-224-2064</b></li>
      <li><span>이메일</span><a href="mailto:byryu210@gmail.com">byryu210@gmail.com</a></li>
      <li><span>블로그</span><a href="https://blog.naver.com/byryu2101" target="_blank" rel="noopener">blog.naver.com/byryu2101</a></li>
      <li><span>위치</span><div><b class="blue">창원시 마산합포구 3·15대로 217, 2층 (중앙동 3가)<br>창원지방법원 마산지원 도보 1분</b><p class="visit-note">출장이 잦아 <b>방문 전에 전화 또는 문자로 방문 예약</b>을 하시는 것을 추천드립니다.</p></div></li>
    </ul>
    <div class="cta"><a class="btn" href="tel:0552862064" data-pop="call">전화 상담</a><a class="btn" href="sms:01000000000" data-pop="sms">문자 상담</a><a class="btn btn-ghost" href="{MAP}" target="_blank" rel="noopener">네이버 지도</a></div>
    <p class="note" style="margin-top:20px">상담 비용은 <a class="tl" href="fees.html">비용 안내</a>에서 확인하실 수 있어요.</p>
  </div>
  <a class="map reveal" href="{MAP}" target="_blank" rel="noopener" aria-label="네이버 지도에서 사무소 위치 보기"><img src="img/map.jpg?v={VER}" alt="사무소 위치 지도" loading="lazy"></a>
</div></section>'''
page('contact.html', '상담 문의', '유병열 법무사·행정사 사무소 연락처와 오시는 길.', contact)
print('ok')
