# 페이지 생성기: 기획안의 메뉴 6개 구조
# A 버전(루트): 소개/법무사 업무/행정사 업무/비용 안내/사례·후기/상담 문의
# B 버전(b/ 폴더): '사례·후기' 대신 '업무별 절차' 메뉴. CSS·JS·이미지는 루트 파일을 같이 쓴다.
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEL = '055-286-2064'
VER = '20261101a'  # 정적 파일 캐시를 깨기 위한 버전. 파일을 고칠 때 값을 바꾼다.
NAV_A = [('about.html','사무소 소개'),('legal.html','법무사 업무'),('admin.html','행정사 업무'),
       ('fees.html','비용 안내'),('cases.html','사례·후기'),('contact.html','상담 문의')]
NAV_B = [(h,t) if h!='cases.html' else ('process.html','업무별 절차') for h,t in NAV_A]
PAGES = []  # (파일명, 제목, 설명, 본문, 스크립트, 버전) 버전: 'AB' 공통, 'A'만, 'B'만
MAP = 'https://map.naver.com/p/search/%EB%B2%95%EB%AC%B4%EC%82%AC%20%ED%96%89%EC%A0%95%EC%82%AC%20%EC%9C%A0%EB%B3%91%EC%97%B4%20%EC%82%AC%EB%AC%B4%EC%86%8C'

def page(fn, title, desc, body, scripts='<script src="b.js?v='+VER+'"></script>', only='AB'):
    PAGES.append((fn, title, desc, body, scripts, only))

def render(fn, title, desc, body, scripts, v):
    nav, d, R = (NAV_A, OUT, '') if v=='A' else (NAV_B, os.path.join(OUT,'b'), '../')
    if R:
        body = body.replace('src="img/', 'src="'+R+'img/')
        scripts = scripts.replace('<script src="', '<script src="'+R)
    robots = '<meta name="robots" content="noindex">\n' if v=='B' else ''
    menu = ''.join(f'<a href="{h}"{" class=on" if h==fn else ""}>{t}</a>' for h,t in nav)
    html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | 유병열 법무사·행정사 사무소</title>
<meta name="description" content="{desc}">
{robots}<link rel="icon" href="{R}img/emblem.jpg">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<script>(function(){{if(!window.matchMedia||!matchMedia("(max-width:819px)").matches||!document.fonts)return;var d=document.documentElement;d.className+=" wf";function ok(){{d.className=d.className.replace(" wf","")}}setTimeout(ok,900);document.fonts.ready.then(ok)}})()</script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="{R}style.css?v={VER}">
<link rel="stylesheet" href="{R}b.css?v={VER}">
</head>
<body>
<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="brand" href="index.html" aria-label="유병열 법무사·행정사 사무소 홈"><img src="{R}img/emblem.jpg" alt="" width="44" height="41"><span class="bt"><b>유병열</b><small>법무사·행정사</small></span></a>
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
    <p>유병열 법무사·행정사 사무소<br>창원시 마산합포구 3·15대로 217, 2층 (중앙동 3가)<br><span class="nb">전화 {TEL}</span> · <span class="nb">휴대폰 010-0000-0000</span><br>팩스 055-224-2064<br>byryu210@gmail.com</p>
    <p class="copy">© 유병열 법무사·행정사 사무소. 이 사이트의 내용은 일반적인 안내이며 개별 사건에 대한 법률 판단이 아닙니다.</p>
    </div>
    <img class="foot-logo" src="{R}img/logo-square.png" alt="유병열 법무사·행정사 사무소" width="96" height="96">
  </div>
</footer>
<script src="{R}pop.js?v={VER}"></script>
{scripts}
</body>
</html>
'''
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, fn), 'w', encoding='utf-8').write(html)

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
    <p class="note"><a class="tl nb" href="legal.html">법무사 업무 전체 보기</a> · <a class="tl nb" href="admin.html">행정사 업무 전체 보기</a></p>
  </div>
</section>

<section class="section tinted">
  <div class="wrap about">
    <div class="about-photo reveal"><div class="slider" aria-roledescription="carousel" aria-label="대표 사진">
      <div class="slides">
        <img src="img/id.jpg" alt="유병열 법무사·행정사 증명사진" loading="lazy" width="1000" height="1000" style="object-position:center 18%">
        <img src="img/ceo.jpg" alt="유병열 법무사·행정사" width="506" height="900">
        <img src="img/desk.jpg" alt="서류를 작성하는 사무소 내부" loading="lazy" width="900" height="1200">
      </div>
      <button type="button" class="sl-btn prev" aria-label="이전 사진">‹</button>
      <button type="button" class="sl-btn next" aria-label="다음 사진">›</button>
      <div class="sl-dots"></div>
    </div></div>
    <div class="about-text">
      <p class="eyebrow">대표 소개</p>
      <h2>유병열 법무사·행정사</h2>
      <p class="lead2">서류 하나하나를 직접 확인하고, 처음 오신 분도 이해할 수 있게 설명드립니다.</p>
      <ul class="badges"><li>법무사 · 행정사</li><li>경남지방법무사회</li><li>대한법무사협회</li><li>대한행정사회</li></ul>
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
HOME_T, HOME_D = '마산 경매·개인회생·상속등기', '창원지방법원 마산지원 도보 1분. 부동산 경매입찰·등기, 개인회생·파산, 상속 서류 작성을 법무사·행정사가 직접 상담합니다.'
page('index.html', HOME_T, HOME_D, home, only='A')
home_b = home.replace('</ol>\n  </div>\n</section>', '</ol>\n    <p class="note"><a class="tl nb" href="process.html">업무별 절차 자세히 보기</a></p>\n  </div>\n</section>', 1)
assert home_b != home
page('index.html', HOME_T, HOME_D, home_b, only='B')

# ---------- 소개
about = head('사무소 소개', '처음부터 끝까지 직접 처리하는 법무사·행정사', '&nbsp;') + '''
<section class="section"><div class="wrap about">
  <div class="about-photo reveal"><div class="slider" aria-roledescription="carousel" aria-label="대표 사진">
      <div class="slides">
        <img src="img/id.jpg" alt="유병열 법무사·행정사 증명사진" loading="lazy" width="1000" height="1000" style="object-position:center 18%">
        <img src="img/ceo.jpg" alt="유병열 법무사·행정사" width="506" height="900">
        <img src="img/desk.jpg" alt="서류를 작성하는 사무소 내부" loading="lazy" width="900" height="1200">
      </div>
      <button type="button" class="sl-btn prev" aria-label="이전 사진">‹</button>
      <button type="button" class="sl-btn next" aria-label="다음 사진">›</button>
      <div class="sl-dots"></div>
    </div></div>
  <div class="about-text">
    <h2>유병열</h2>
    <p class="lead2">처음 오신 분도 이해할 수 있게 쉬운 말로 설명드립니다.</p>
    <dl class="career">
      <div><dt>학력</dt><dd>마산상업고등학교 졸업<br>한국방송통신대학교 법학과 졸업</dd></div>
      <div><dt>경력</dt><dd>(前) 외환은행<br>(前) 행정직 공무원</dd></div>
      <div><dt>자격</dt><dd>법무사 · 행정사</dd></div>
      <div><dt>소속</dt><dd>경남지방법무사회<br>대한법무사협회<br>대한행정사회</dd></div>
      <div><dt>사무소</dt><dd>2023년부터 현 위치에서 운영중</dd></div>
    </dl>
  </div>
</div></section>
<section class="section tinted"><div class="wrap">
  <p class="eyebrow">사무소 둘러보기</p><h2>편하게 들러 상담하세요</h2>
  <div class="gallery">
    <img class="reveal" src="img/office2.jpg" alt="3·15대로에서 본 사무소 전경" loading="lazy">
    <img class="reveal" src="img/office1.jpg" alt="3·15대로변 유병열 법무사·행정사 사무소 입구" loading="lazy">
    <img class="reveal" src="img/interior.jpg" alt="사무소 상담 공간" loading="lazy">
    <img class="reveal" src="img/shelf.jpg" alt="법률 서적이 꽂힌 사무소 서가" loading="lazy">
  </div>
</div></section>''' + CTA
page('about.html', '사무소 소개', '유병열 법무사·행정사 대표 소개와 사무소 안내. 경남지방법무사회·대한법무사협회·대한행정사회 소속.', about)

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
    <div class="consult reveal"><div><h3>상담 비용 안내</h3><p>개별적 상담·자문은 <b>건당 150,000원</b>,<br>계속적 상담·자문은 <b>월 600,000원</b>이<br class="mbr"> 각각 <b>상한액</b>입니다. <span class="hl2">사건을 맡기시는 경우에는 상담료가 적용되지 않습니다.</span></p></div></div>
</div></section>
''' + CTA
page('fees.html', '비용 안내와 보수 계산기', '법무사보수표 기준 예상 보수 계산기와 상담 비용 안내.', fees,
     '<script src="calc.js?v='+VER+'"></script><script src="main.js?v='+VER+'"></script>')

# ---------- 사례·후기
cases = head('사례·후기', '처리 사례와 후기', '의뢰인 정보가 드러나지 않도록 동의를 받은 내용만 게시합니다.') + '''
<section class="section"><div class="wrap">
  <p class="note ex-note">아래는 안내 형식을 보여 드리는 <b>예시</b>이며, 실제 의뢰인의 사례가 아닙니다.</p>
  <div class="cards"><div class="card reveal"><span class="ex">예시</span><h3>상속등기</h3><p><b>상황</b> 부모님이 돌아가신 뒤 자녀 3명이 아파트를 상속하게 된 경우</p><p><b>진행</b> 상속인 확인과 가족관계 서류 준비 → 상속재산분할협의서 작성 → 취득세 신고·납부 → 상속등기 신청</p></div><div class="card reveal"><span class="ex">예시</span><h3>개인회생</h3><p><b>상황</b> 여러 금융기관에 채무가 있어 월 변제가 어려운 근로소득자의 경우</p><p><b>진행</b> 채무 내역과 소득·재산 확인 → 신청서와 변제계획안 등 서류 작성 → 법원 제출</p></div><div class="card reveal"><span class="ex">예시</span><h3>경매 입찰</h3><p><b>상황</b> 거주할 아파트를 경매로 취득하려는 경우</p><p><b>진행</b> 권리분석과 현황 조사 → 입찰가 상담 → 매수신청 대리 → 낙찰 후 소유권이전등기</p></div><div class="card reveal"><span class="ex">예시</span><h3>임차권등기</h3><p><b>상황</b> 임대차 계약이 끝났지만 보증금을 돌려받지 못한 채 이사해야 하는 경우</p><p><b>진행</b> 임대차계약서와 주민등록 서류 확인 → 임차권등기명령 신청서 작성 → 법원 제출 → 명령 후 임차권등기</p></div></div>
  <div class="empty reveal" style="margin-top:28px"><h3>더 많은 업무 이야기는 블로그에서 확인하세요</h3>
  <a class="btn" href="https://blog.naver.com/byryu2101" target="_blank" rel="noopener">네이버 블로그 가기</a></div>
</div></section>'''
page('cases.html', '사례·후기', '유병열 법무사·행정사 사무소의 처리 사례와 블로그.', cases, only='A')

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
</div></section>
<section class="section tinted"><div class="wrap"><p class="eyebrow">FAQ</p><h2>자주 묻는 질문</h2><div class="qas"><details class="qa reveal"><summary>소유권이전등기(매매)에는 어떤 서류가 필요한가요?</summary><p>매도인은 신분증, 인감증명서(매도용), 인감도장, 등기권리증(또는 등기식별정보)이 필요하고, 매수인은 신분증, 도장, 주민등록초본이 필요합니다. 부동산거래계약 신고필증과 취득세 납부 영수증도 함께 제출합니다. 부동산 종류와 거래 방식에 따라 추가 서류가 있을 수 있어, 계약 전에 문의하시면 정확히 안내해 드립니다.</p></details><details class="qa reveal"><summary>상속등기는 꼭 해야 하나요? 기한이 있나요?</summary><p>상속으로 부동산을 취득한 사실을 안 날부터 3년 이내에 상속등기를 신청해야 하며, 정당한 사유 없이 기간이 지나면 과태료가 부과될 수 있습니다. 협의분할로 상속인이 여러 명일 때는 협의서와 인감증명서 등 서류가 많아지니 미리 상담받으시길 권해 드립니다.</p></details><details class="qa reveal"><summary>임차권등기명령은 어떤 경우에 신청하나요?</summary><p>임대차 계약이 끝났는데도 보증금을 돌려받지 못한 채 이사해야 할 때 신청합니다. 법원의 명령을 받아 등기를 하면 이사하거나 주민등록을 옮긴 뒤에도 기존에 갖춘 대항력과 우선변제권이 유지됩니다. 신청서 작성과 서류 준비를 도와드립니다.</p></details><details class="qa reveal"><summary>개인회생과 개인파산은 어떻게 다른가요?</summary><p>개인회생은 일정한 소득이 있는 분이 법원이 인가한 변제계획에 따라 정해진 기간 동안 일부를 갚고 나머지를 면책받는 절차입니다. 개인파산은 갚을 능력이 부족한 분이 채무의 면책을 신청하는 절차입니다. 어떤 절차가 맞는지는 소득, 재산, 채무 내용에 따라 달라 상담 후 안내해 드리며, 신청서류 작성과 제출을 돕습니다.</p></details><details class="qa reveal"><summary>경매 입찰도 대리해 주시나요?</summary><p>권리분석과 현황 조사 등 재산취득 상담, 매수신청 대리, 낙찰 후 소유권이전등기까지 도와드립니다. 물건마다 확인할 사항이 달라 입찰 전에 먼저 상담해 보시길 권해 드립니다.</p></details><details class="qa reveal"><summary>방문 전에 예약이 필요한가요?</summary><p>출장이 잦아 사무소를 비울 수 있으니 방문 전에 전화 또는 문자로 예약해 주세요. 영업시간 외에도 문자로 상담하실 수 있습니다.</p></details></div><p class="note">개별 사건의 내용에 따라 달라질 수 있으니, 정확한 내용은 상담으로 확인해 주세요.</p></div></section>'''
page('contact.html', '상담 문의', '유병열 법무사·행정사 사무소 연락처와 오시는 길.', contact)
# ---------- 업무별 절차 (B 버전 전용)
# 광고규정 고려: 성공률·처리 실적·후기 표현을 쓰지 않고, 일반적인 법원 절차만 설명한다.
def proc(id_, num, name, who, steps, note):
    li = ''.join(f'<li><b>{t}</b><span>{d}</span></li>' for t,d in steps)
    return f"""<article class="svc reveal" id="{id_}"><div class="svc-h"><span class="num">{num}</span><h2>{name}</h2></div>
<p class="svc-who">{who}</p><ol class="pflow">{li}</ol><p class="svc-note">{note}</p></article>"""
JUMP = '<nav class="pjump" aria-label="업무 바로가기"><a href="#auction">경매입찰</a><a href="#rehab">개인회생</a><a href="#bankrupt">파산</a><a href="#inherit">상속등기</a></nav>'
process = head('업무별 절차', '어떤 순서로 진행되는지 미리 알려 드립니다', '주요 업무가 법원·등기소에서 어떻게 진행되는지 단계별로 정리했습니다.') + '<section class="section"><div class="wrap">' + JUMP + '<div class="svcs">' + \
  proc('auction','01','부동산 경매입찰','경매로 부동산을 취득하려는 분',[
    ('물건 확인과 권리분석 상담','매각물건명세서, 등기사항증명서, 현황조사서 등을 함께 보며 인수해야 할 권리나 점유 관계가 있는지 확인합니다.'),
    ('입찰 준비','입찰 가격을 정하고, 입찰보증금(보통 최저매각가격의 10%)과 위임장·인감증명서 등 필요한 서류를 준비합니다.'),
    ('매각기일 입찰','법원에서 기일입찰표를 작성해 제출합니다. 매수신청 대리를 맡기시면 직접 법원에 가지 않으셔도 됩니다.'),
    ('매각허가결정','최고가매수신고인이 되면 법원이 매각허가 여부를 결정하고, 이의 기간이 지나면 확정됩니다.'),
    ('대금 납부','법원이 정한 대금지급기한까지 잔금을 납부합니다. 대출을 받는 경우 일정을 미리 맞춰 둡니다.'),
    ('소유권이전등기','대금을 낸 뒤 소유권이전과 기존 권리의 말소 등기를 법원에 촉탁 신청합니다. 점유자가 있으면 인도명령 신청을 검토합니다.'),
  ], '물건마다 확인할 사항이 다르므로 입찰 전에 먼저 상담해 주세요.') + \
  proc('rehab','02','개인회생','일정한 소득이 있지만 채무를 모두 갚기 어려운 분',[
    ('상담','소득, 재산, 채무 내역을 확인하고 개인회생 신청이 가능한지, 다른 절차가 맞는지 살펴봅니다.'),
    ('서류 준비','소득 증빙, 재산 자료, 부채증명서 등 필요한 서류 목록을 안내해 드립니다.'),
    ('신청서·변제계획안 작성과 제출','신청서와 채권자목록, 변제계획안을 작성해 관할 법원에 제출합니다. 필요하면 금지·중지명령 신청도 함께 합니다.'),
    ('개시결정','법원이 서류를 검토하고 보정을 거쳐 회생절차 개시 여부를 결정합니다.'),
    ('채권자집회와 인가','채권자집회를 거쳐 법원이 변제계획을 인가합니다.'),
    ('변제와 면책','인가된 계획에 따라 정해진 기간(원칙 3년) 동안 변제를 마치면 법원이 면책 여부를 결정합니다.'),
  ], '상담 내용은 비밀이 유지됩니다. 진행 기간은 법원과 사건에 따라 다릅니다.') + \
  proc('bankrupt','03','개인파산','소득이나 재산으로 채무를 갚을 능력이 부족한 분',[
    ('상담','채무 규모와 소득, 재산, 생활 상황을 확인하고 파산 절차가 맞는지 살펴봅니다.'),
    ('서류 준비','재산 목록, 수입·지출 자료, 채권자 목록, 진술서 등에 필요한 자료를 안내해 드립니다.'),
    ('파산·면책 신청서 작성과 제출','파산 신청서와 면책 신청서를 작성해 관할 법원에 제출합니다.'),
    ('파산선고','법원이 심리 후 파산을 선고합니다. 사건에 따라 파산관재인이 선임되어 재산과 채무를 조사합니다.'),
    ('면책 심리','법원이 면책 여부를 판단하기 위해 심리하고, 채권자에게 이의 기회가 주어집니다.'),
    ('면책결정','면책이 결정되고 확정되면 채무에 대한 책임이 면제됩니다. 세금·벌금 등 일부 채무는 면책되지 않습니다.'),
  ], '상담 내용은 비밀이 유지됩니다. 진행 기간은 법원과 사건에 따라 다릅니다.') + \
  proc('inherit','04','상속등기','가족이 돌아가셔서 부동산 명의를 정리해야 하는 분',[
    ('상담','상속인이 누구인지, 상속받을 부동산이 무엇인지 확인합니다.'),
    ('서류 준비','돌아가신 분의 기본증명서·가족관계증명서·제적등본 등과 상속인들의 서류를 준비합니다.'),
    ('상속 방법 결정','법정상속분대로 할지, 상속인끼리 협의해 나눌지 정합니다. 협의로 나누면 상속재산분할협의서를 작성합니다.'),
    ('취득세 신고·납부','상속 개시일이 속한 달의 말일부터 6개월 안에 부동산 소재지 관할 관청에 신고·납부합니다.'),
    ('상속등기 신청','등기소에 상속을 원인으로 한 소유권이전등기를 신청합니다.'),
    ('완료','등기가 끝나면 등기필정보 등 서류를 전달해 드립니다.'),
  ], '상속포기·한정승인은 상속이 시작된 것을 안 날부터 3개월 안에 가정법원에 신고해야 하니 서둘러 상담해 주세요. 상속세는 세무사 업무라 해당 전문가를 안내해 드립니다.') + \
  '</div><p class="note" style="margin-top:24px">위 내용은 일반적인 절차 안내이며, 개별 사건에 따라 순서와 필요 서류가 달라질 수 있습니다.</p></div></section>' + CTA
page('process.html', '업무별 절차 안내', '부동산 경매입찰, 개인회생, 개인파산, 상속등기가 어떤 순서로 진행되는지 단계별로 안내합니다.', process, only='B')


for fn,title,desc,body,scripts,only in PAGES:
    for v in only:
        render(fn,title,desc,body,scripts,v)
print('ok')
