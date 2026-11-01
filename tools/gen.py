# 페이지 생성기: 기획안의 메뉴 6개 구조
# B 버전(메인, 루트): '업무별 절차' 메뉴가 있는 버전. 2026-11-01부터 메인.
# A 버전(old/ 폴더, 보관용): '사례·후기' 메뉴가 있던 이전 버전. 검색엔진 색인 차단.
# old/ 페이지는 루트의 CSS·JS·이미지를 같이 쓴다. 예전 b/ 주소와 루트 cases.html은 새 위치로 넘겨 준다.
import os, re
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEL = '055-286-2064'
VER = '20261101n'  # 정적 파일 캐시를 깨기 위한 버전. 파일을 고칠 때 값을 바꾼다.
NAV_A = [('about.html','사무소 소개'),('legal.html','법무사 업무'),('admin.html','행정사 업무'),
       ('fees.html','비용 안내'),('cases.html','사례·후기'),('contact.html','상담 문의')]
NAV_B = [(h,t) if h!='cases.html' else ('process.html','업무별 절차') for h,t in NAV_A]
PAGES = []
BASE = 'https://eonsss.github.io/Law-office-website/'  # 도메인을 사면 이 값만 바꾸고 다시 생성한다.
SITE = '유병열 법무사·행정사 사무소'
# 메인(B) 페이지의 검색 노출용 제목·설명. 광고규정상 성공·실적 표현은 쓰지 않는다.
META = {
  'index.html':  (SITE+' | 마산 경매·개인회생·상속등기', '마산 3·15대로 유병열 법무사·행정사 사무소. 부동산 경매입찰·등기, 개인회생, 파산, 상속 상담. 055-286-2064'),
  'about.html':  ('사무소 소개 | '+SITE, '마산 3·15대로 유병열 법무사·행정사 사무소 대표 소개. 경남지방법무사회·대한법무사협회·대한행정사회 소속, 창원지방법원 마산지원 도보 1분.'),
  'legal.html':  ('법무사 업무 | '+SITE, '부동산 경매입찰, 매매·증여·근저당 등기, 개인회생·파산, 상속등기, 법인등기, 법원 제출 서류 작성 안내. 마산 유병열 법무사 055-286-2064'),
  'admin.html':  ('행정사 업무 | '+SITE, '행정심판, 인허가·신고, 외국인 체류·출입국, 행정처분 의견 제출, 계약서·내용증명, 토지·건축 민원 안내. 마산 유병열 행정사 055-286-2064'),
  'fees.html':   ('비용 안내와 보수 계산기 | '+SITE, '법무사보수표 기준 예상 보수를 바로 계산해 보세요. 등기·경매 등 업무별 기본보수 상한액과 상담 비용 안내.'),
  'process.html':('업무별 절차 안내 | '+SITE, '경매입찰, 개인회생·파산, 상속등기, 매매·증여 등기, 법인등기, 행정심판, 외국인 체류 업무가 어떤 흐름으로 진행되는지 안내합니다. 마산 유병열 법무사·행정사 사무소.'),
  'contact.html':('상담 문의·오시는 길 | '+SITE, '유병열 법무사·행정사 사무소 연락처와 오시는 길. 창원시 마산합포구 3·15대로 217, 2층. 전화 055-286-2064, 평일 09~18시·주말 09~13시.'),
}
LD = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"LegalService","name":"유병열 법무사·행정사 사무소","url":"'''+BASE+'''","image":"'''+BASE+'''img/exterior.jpg","telephone":"+82-55-286-2064","faxNumber":"+82-55-224-2064","email":"byryu210@gmail.com","address":{"@type":"PostalAddress","streetAddress":"3·15대로 217, 2층","addressLocality":"창원시 마산합포구","addressRegion":"경상남도","addressCountry":"KR"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"18:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Saturday","Sunday"],"opens":"09:00","closes":"13:00"}]}</script>
'''  # (파일명, 제목, 설명, 본문, 스크립트, 버전) 버전: 'AB' 공통, 'A'만, 'B'만
MAP = 'https://map.naver.com/p/search/%EB%B2%95%EB%AC%B4%EC%82%AC%20%ED%96%89%EC%A0%95%EC%82%AC%20%EC%9C%A0%EB%B3%91%EC%97%B4%20%EC%82%AC%EB%AC%B4%EC%86%8C'

def page(fn, title, desc, body, scripts='<script src="b.js?v='+VER+'"></script>', only='AB'):
    PAGES.append((fn, title, desc, body, scripts, only))

def render(fn, title, desc, body, scripts, v):
    nav, d, R = (NAV_B, OUT, '') if v=='B' else (NAV_A, os.path.join(OUT,'old'), '../')
    if R:
        body = body.replace('src="img/', 'src="'+R+'img/')
        body = body.replace('srcset="img/', 'srcset="'+R+'img/').replace(', img/', ', '+R+'img/')
        scripts = scripts.replace('<script src="', '<script src="'+R)
    robots = '<meta name="robots" content="noindex">\n' if v=='A' else ''
    full = f'{title} | {SITE}'
    seo = ''
    if v=='B':
        full, desc = META[fn]
        url = BASE + ('' if fn=='index.html' else fn)
        seo = (f'<link rel="canonical" href="{url}">\n<meta property="og:type" content="website">\n'
               f'<meta property="og:site_name" content="{SITE}">\n<meta property="og:locale" content="ko_KR">\n'
               f'<meta property="og:title" content="{full}">\n<meta property="og:description" content="{desc}">\n'
               f'<meta property="og:url" content="{url}">\n<meta property="og:image" content="{BASE}img/exterior.jpg">\n'
               f'<meta name="twitter:card" content="summary_large_image">\n' + (LD if fn=='index.html' else ''))
    menu = ''.join(f'<a href="{h}"{" class=on" if h==fn else ""}>{t}</a>' for h,t in nav)
    html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
{robots}{seo}<link rel="icon" href="{R}img/emblem.jpg">
<script>(function(){{if(!window.matchMedia||!matchMedia("(max-width:819px)").matches||!document.fonts)return;var d=document.documentElement;d.className+=" wf";function ok(){{d.className=d.className.replace(" wf","")}}setTimeout(ok,500);document.fonts.ready.then(ok)}})()</script>
<link rel="stylesheet" href="{R}fonts/pretendard.css?v=1.3.9">
<link rel="stylesheet" href="{R}style.css?v={VER}">
<link rel="stylesheet" href="{R}b.css?v={VER}">
</head>
<body>
<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="brand" href="index.html" aria-label="유병열 법무사·행정사 사무소 홈"><img src="{R}img/emblem.jpg" alt="" width="44" height="41"><span class="bt"><b>유병열</b><small>법무사·행정사</small></span></a>
    <nav class="menu bmenu">{menu}</nav>
    <span class="hbtns"><a class="btn btn-sm" href="tel:0552862064" data-pop="call">전화 상담</a><a class="btn btn-sm" href="sms:01028512064" data-pop="sms">문자 상담</a></span>
  </div>
  <nav class="wrap tabs">{menu}</nav>
</header>
<main>
{body}
</main>
<footer class="footer">
  <div class="wrap foot-in">
    <div class="foot-text">
    <p>유병열 법무사·행정사 사무소<br>창원시 마산합포구 3·15대로 217, 2층 (중앙동 3가)<br><span class="nb">전화 {TEL}</span> · <span class="nb">휴대폰 010-2851-2064</span><br>팩스 055-224-2064<br>byryu210@gmail.com</p>
    <p class="copy">© 유병열 법무사·행정사 사무소. 이 사이트의 내용은 일반적인 안내이며 개별 사건에 대한 법률 판단이 아닙니다.</p>
    </div>
    <img class="foot-logo" src="{R}img/logo-square.png" alt="유병열 법무사·행정사 사무소" width="96" height="96" loading="lazy" decoding="async">
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
<div class="cta"><a class="btn" href="tel:0552862064" data-pop="call">전화 상담</a><a class="btn" href="sms:01028512064" data-pop="sms">문자 상담</a></div>
</div></section>'''

# ---------- 홈
home = f'''
<section class="hero">
  <div class="wrap hero-in">
    <p class="eyebrow reveal">창원지방법원 마산지원 도보 1분</p>
    <h1 class="reveal">복잡한 법원 서류,<br>처음부터 끝까지 직접 챙깁니다.</h1>
    <p class="lead reveal">부동산 경매입찰과 등기, 개인회생·파산, 상속까지.<br class="pc">법무사·행정사가 직접 상담하고 직접 작성합니다.</p>
    <div class="cta reveal"><a class="btn" href="tel:0552862064" data-pop="call">전화 상담</a><a class="btn" href="sms:01028512064" data-pop="sms">문자 상담</a><a class="btn btn-ghost" href="fees.html">예상 보수 계산</a></div>
  </div>
  <div class="wrap hero-photo reveal"><picture><source type="image/webp" srcset="img/exterior-800.webp 800w, img/exterior-1200.webp 1200w, img/exterior-1600.webp 1600w" sizes="(max-width:1140px) 100vw, 1080px"><img src="img/exterior.jpg" alt="마산합포구 3·15대로변 유병열 법무사·행정사 사무소 전경" width="1600" height="1200" fetchpriority="high" decoding="async"></picture></div>
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
page('legal.html', '법무사 업무', '부동산 경매입찰·등기, 개인회생·파산, 상속 서류 작성 등 법무사 업무 안내.', legal, only='A')
# 메인(B)에만 추가한 법무사 업무 (2026-11-01)
LEGAL_ADD = svc('corp','05','법인등기','회사를 세우거나 임원·본점·목적 등이 바뀐 법인','법인 설립등기|임원 변경 등 각종 변경등기|필요 서류 안내'.split('|')) + \
  svc('court','06','법원 제출 서류 작성','돈을 돌려받지 못했거나 법원에 서류를 내야 하는 분','지급명령 신청서 작성|가압류·가처분 신청서 작성|공탁 서류 작성'.split('|'), '<p class="svc-note">소송 대리가 필요한 사건은 변호사 업무라 해당 전문가를 안내해 드립니다.</p>')
legal_b = legal.replace("</div></section>" + CTA, LEGAL_ADD + "</div></section>" + CTA, 1)
assert legal_b != legal
# 메인(B) 법무사 업무 메뉴에서는 비밀 유지·세무사·변호사 안내 문구를 뺀다 (2026-11-01 요청)
legal_b = re.sub(r'<p class="svc-note">.*?</p>', '', legal_b)
page('legal.html', '법무사 업무', '', legal_b, only='B')

# ---------- 행정사
admin = head('행정사 업무', '행정 서류도 함께 도와드립니다', '행정사 업무 범위는 사안에 따라 달라 상담 때 정확히 안내해 드립니다.') + '<section class="section"><div class="wrap svcs">' + \
  svc('appeal','01','행정심판','행정기관의 처분이 억울하다고 느끼시는 분','행정심판 청구서 작성|필요 서류 안내'.split('|')) + \
  svc('permit','02','인허가·신고','영업이나 사업에 필요한 허가·신고를 준비하시는 분','각종 인허가·신고 서류 작성|제출 대행'.split('|')) + \
  '</div></section>' + CTA
page('admin.html', '행정사 업무', '행정심판 청구서 작성, 각종 인허가·신고 서류 작성 등 행정사 업무 안내.', admin, only='A')
# 메인(B)에만 추가한 행정사 업무 (2026-11-01)
ADMIN_ADD = svc('visa','03','외국인 체류·출입국','국내에 머무는 외국인, 외국인 가족이나 근로자를 초청하려는 분','체류 기간 연장·자격 변경 서류 작성|출입국 관련 민원 서류 제출 대행'.split('|')) + \
  svc('disposal','04','행정처분 의견 제출','영업정지·면허 취소 등 처분을 앞두고 사전 통지를 받은 분','의견서 작성|처분 전 소명 자료 정리'.split('|')) + \
  svc('contract','05','계약서·내용증명 작성','계약 내용을 문서로 남기거나 상대방에게 의사를 분명히 전하려는 분','각종 계약서 작성|내용증명 작성'.split('|')) + \
  svc('land','06','토지·건축 민원','토지 이용이나 건축과 관련해 관청에 신청할 일이 있는 분','농지·개발행위 등 토지 관련 신청 서류 작성|건축 관련 민원 서류 작성과 제출 대행'.split('|'))
admin_b = admin.replace("</div></section>" + CTA, ADMIN_ADD + "</div></section>" + CTA, 1)
assert admin_b != admin
page('admin.html', '행정사 업무', '', admin_b, only='B')

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
      <li><span>휴대폰</span><a href="tel:01028512064">010-2851-2064</a></li>
      <li><span>팩스</span><b class="blue">055-224-2064</b></li>
      <li><span>이메일</span><a href="mailto:byryu210@gmail.com">byryu210@gmail.com</a></li>
      <li><span>블로그</span><a href="https://blog.naver.com/byryu2101" target="_blank" rel="noopener">blog.naver.com/byryu2101</a></li>
      <li><span>위치</span><div><b class="blue" id="addr">창원시 마산합포구 3·15대로 217, 2층 (중앙동 3가)<br>창원지방법원 마산지원 도보 1분</b><p class="visit-note">출장이 잦아 <b>방문 전에 전화 또는 문자로 방문 예약</b>을 하시는 것을 추천드립니다.</p></div></li>
    </ul>
    <div class="cta"><a class="btn" href="tel:0552862064" data-pop="call">전화 상담</a><a class="btn" href="sms:01028512064" data-pop="sms">문자 상담</a><a class="btn btn-ghost" href="{MAP}" target="_blank" rel="noopener">네이버 지도</a></div>
    <p class="note" style="margin-top:20px">상담 비용은 <a class="tl" href="fees.html">비용 안내</a>에서 확인하실 수 있어요.</p>
  </div>
  <a class="map reveal" href="{MAP}" target="_blank" rel="noopener" aria-label="네이버 지도에서 사무소 위치 보기"><img src="img/map.jpg?v={VER}" alt="사무소 위치 지도" loading="lazy"></a>
</div></section>
<section class="section tinted"><div class="wrap"><p class="eyebrow">FAQ</p><h2>자주 묻는 질문</h2><div class="qas"><details class="qa reveal"><summary>소유권이전등기(매매)에는 어떤 서류가 필요한가요?</summary><p>매도인은 신분증, 인감증명서(매도용), 인감도장, 등기권리증(또는 등기식별정보)이 필요하고, 매수인은 신분증, 도장, 주민등록초본이 필요합니다. 부동산거래계약 신고필증과 취득세 납부 영수증도 함께 제출합니다. 부동산 종류와 거래 방식에 따라 추가 서류가 있을 수 있어, 계약 전에 문의하시면 정확히 안내해 드립니다.</p></details><details class="qa reveal"><summary>상속등기는 꼭 해야 하나요? 기한이 있나요?</summary><p>상속으로 부동산을 취득한 사실을 안 날부터 3년 이내에 상속등기를 신청해야 하며, 정당한 사유 없이 기간이 지나면 과태료가 부과될 수 있습니다. 협의분할로 상속인이 여러 명일 때는 협의서와 인감증명서 등 서류가 많아지니 미리 상담받으시길 권해 드립니다.</p></details><details class="qa reveal"><summary>임차권등기명령은 어떤 경우에 신청하나요?</summary><p>임대차 계약이 끝났는데도 보증금을 돌려받지 못한 채 이사해야 할 때 신청합니다. 법원의 명령을 받아 등기를 하면 이사하거나 주민등록을 옮긴 뒤에도 기존에 갖춘 대항력과 우선변제권이 유지됩니다. 신청서 작성과 서류 준비를 도와드립니다.</p></details><details class="qa reveal"><summary>개인회생과 개인파산은 어떻게 다른가요?</summary><p>개인회생은 일정한 소득이 있는 분이 법원이 인가한 변제계획에 따라 정해진 기간 동안 일부를 갚고 나머지를 면책받는 절차입니다. 개인파산은 갚을 능력이 부족한 분이 채무의 면책을 신청하는 절차입니다. 어떤 절차가 맞는지는 소득, 재산, 채무 내용에 따라 달라 상담 후 안내해 드리며, 신청서류 작성과 제출을 돕습니다.</p></details><details class="qa reveal"><summary>경매 입찰도 대리해 주시나요?</summary><p>권리분석과 현황 조사 등 재산취득 상담, 매수신청 대리, 낙찰 후 소유권이전등기까지 도와드립니다. 물건마다 확인할 사항이 달라 입찰 전에 먼저 상담해 보시길 권해 드립니다.</p></details><details class="qa reveal"><summary>방문 전에 예약이 필요한가요?</summary><p>출장이 잦아 사무소를 비울 수 있으니 방문 전에 전화 또는 문자로 예약해 주세요. 영업시간 외에도 문자로 상담하실 수 있습니다.</p></details></div><p class="note">개별 사건의 내용에 따라 달라질 수 있으니, 정확한 내용은 상담으로 확인해 주세요.</p></div></section>'''
page('contact.html', '상담 문의', '유병열 법무사·행정사 사무소 연락처와 오시는 길.', contact, only='A')
# 메인(B): 지도 높이를 왼쪽 정보(영업시간~위치) 높이에 맞춘다 (b.css .cvisit)
contact_b = contact.replace('<div class="wrap visit">', '<div class="wrap visit cvisit">', 1)
# 제목 아래 여백을 다른 메뉴(소개 등)와 같게: 빈 부제 줄을 둔다
contact_b = contact_b.replace('<h1>전화 한 통이면 충분합니다</h1>', '<h1>전화 한 통이면 충분합니다</h1><p class="sub">&nbsp;</p>', 1)
assert contact_b != contact
page('contact.html', '상담 문의', '', contact_b, '<script src="b.js?v='+VER+'"></script><script src="cmap.js?v='+VER+'"></script>', only='B')
# ---------- 업무별 절차 (B 버전 전용)
# 광고규정 고려: 성공률·처리 실적·후기 표현을 쓰지 않는다.
# 셀프 처리 안내서가 되지 않도록 큰 흐름과 '전문가가 필요한 이유'만 쓴다.
# 서류 이름, 서식 작성법, 금액·비율, 기한 계산 같은 실무 내용은 넣지 않는다.
PTABS = [('auction','경매입찰'),('rehab','개인회생'),('bankrupt','개인파산'),('inherit','상속등기'),
         ('deal','매매·증여'),('corp','법인등기'),('appeal','행정심판'),('visa','체류·비자')]
def proc(id_, name, who, steps, why, note=''):
    li = ''.join(f'<li><b>{t}</b><span>{d}</span></li>' for t,d in steps)
    wl = ''.join(f'<li>{w}</li>' for w in why)
    S = '상담 내용은 비밀이 유지됩니다.'  # 모든 탭에 공통으로 넣는다
    if S not in note: note = (S + ' ' + note).strip()
    n = f'<p class="svc-note">{note}</p>'
    return f"""<article class="svc ppanel" id="{id_}" role="tabpanel" aria-labelledby="tab-{id_}"{"" if id_==PTABS[0][0] else " hidden"}><div class="svc-h"><h2>{name}</h2></div>
<p class="svc-who">{who}</p><ol class="pflow">{li}</ol>
<div class="pwhy"><h3>전문가와 함께 진행하면 좋은 이유</h3><ul class="check">{wl}</ul></div>{n}</article>"""
TABS = '<div class="ptabs" role="tablist" aria-label="업무 선택">' + ''.join(
    f'<a role="tab" id="tab-{i}" href="#{i}" aria-controls="{i}"' + (' class="on" aria-selected="true"' if i==PTABS[0][0] else ' aria-selected="false"') + f'>{t}</a>' for i,t in PTABS) + '</div>'
process = head('업무별 절차', '어떤 순서로 진행되는지 미리 알려 드립니다', '궁금한 업무를 눌러 전체 흐름을 확인해 보세요.') + '<section class="section"><div class="wrap">' + TABS + '<div class="ppanels">' + \
  proc('auction','부동산 경매입찰','경매로 부동산을 취득하려는 분',[
    ('물건 상담','관심 있는 물건의 권리관계와 현황을 함께 살펴봅니다.'),
    ('입찰','입찰 가격과 준비 사항을 상담하고 매수신청을 대리합니다.'),
    ('낙찰 후 절차','매각허가부터 잔금 납부까지 일정을 안내해 드립니다.'),
    ('소유권이전','소유권이전등기와 이어지는 후속 절차를 처리합니다.'),
  ],['권리관계를 놓치면 낙찰 뒤에 예상하지 못한 부담이 생길 수 있습니다.',
     '입찰 서류의 작은 실수로 입찰이 무효가 되는 경우가 있습니다.',
     '낙찰 뒤에도 정해진 일정에 맞춰 처리할 일이 이어집니다.']) + \
  proc('rehab','개인회생','일정한 소득이 있지만 채무를 모두 갚기 어려운 분',[
    ('상담','소득과 재산, 채무 상황을 보고 맞는 절차를 함께 찾습니다.'),
    ('서류 준비와 작성','필요한 자료를 안내하고 신청 서류를 작성합니다.'),
    ('법원 진행','신청 뒤 법원의 보정 요구와 이후 절차에 대응합니다.'),
    ('변제와 면책','인가된 계획대로 변제를 마치면 면책 절차로 이어집니다.'),
  ],['제출 서류가 많고, 진행 중에 법원의 보정 요구가 이어지는 경우가 많습니다.',
     '변제계획을 어떻게 세우느냐에 따라 앞으로의 생활이 달라질 수 있습니다.',
     '상황에 따라 개인회생보다 다른 절차가 더 맞을 수 있습니다.'], '상담 내용은 비밀이 유지됩니다.') + \
  proc('bankrupt','개인파산','소득이나 재산으로 채무를 갚기 어려운 분',[
    ('상담','채무와 소득, 재산, 생활 상황을 보고 맞는 절차를 함께 찾습니다.'),
    ('서류 준비와 작성','필요한 자료를 안내하고 신청 서류를 작성합니다.'),
    ('법원 심리','법원의 심리 과정에서 요구하는 자료에 대응합니다.'),
    ('면책','법원이 면책 여부를 결정합니다.'),
  ],['재산과 채무를 빠짐없이 정확하게 밝혀야 하며, 누락되면 불리해질 수 있습니다.',
     '모든 채무가 면책되는 것은 아니어서 미리 확인이 필요합니다.',
     '개인회생과 파산 중 어느 쪽이 맞는지 판단이 필요합니다.'], '상담 내용은 비밀이 유지됩니다.') + \
  proc('inherit','상속등기','가족이 돌아가셔서 부동산 명의를 정리해야 하는 분',[
    ('상담','상속인과 상속받을 부동산을 확인합니다.'),
    ('서류 준비','필요한 서류를 안내하고 준비를 도와드립니다.'),
    ('상속 방법 정리','상속인 사이에 나누는 방법을 정하고 필요한 서류를 작성합니다.'),
    ('신고와 등기','세금 신고부터 상속등기까지 처리합니다.'),
  ],['상속인이 여럿이거나 연락이 어려운 분이 있으면 서류가 복잡해집니다.',
     '상속포기·한정승인처럼 기한이 정해진 절차가 있어, 늦어지면 선택할 수 있는 방법이 줄어듭니다.',
     '세금 신고와 등기를 정해진 순서와 기한에 맞춰 진행해야 합니다.'], '상속세는 세무사 업무라 해당 전문가를 안내해 드립니다.') + \
  proc('deal','부동산 매매·증여 등기','부동산을 사고팔거나 가족에게 증여하는 분',[
    ('상담','거래 내용과 부동산의 권리관계를 확인합니다.'),
    ('서류 준비','당사자별로 필요한 서류를 안내하고 준비를 도와드립니다.'),
    ('세금 신고','등기 전에 필요한 세금 신고와 납부를 안내해 드립니다.'),
    ('등기 신청과 완료','등기소에 소유권이전등기를 신청하고 완료된 서류를 전달해 드립니다.'),
  ],['매매는 잔금 날짜에 맞춰 권리관계를 확인하고 바로 등기해야 안전합니다.',
     '증여는 세금 문제를 함께 살펴봐야 해서 미리 계획하는 것이 좋습니다.',
     '서류가 하나라도 빠지면 보정이 필요해 일정이 늦어질 수 있습니다.'], '증여세·양도세 상담은 세무사 업무라 해당 전문가를 안내해 드립니다.') + \
  proc('corp','법인등기','회사를 세우거나 임원·본점 등이 바뀐 법인',[
    ('상담','설립하려는 내용이나 바뀐 사항을 확인합니다.'),
    ('서류 작성','회사 내부 절차에 맞춰 필요한 서류와 신청서를 작성합니다.'),
    ('등기 신청','관할 등기소에 등기를 신청합니다.'),
    ('완료','등기가 끝나면 바뀐 등기사항을 확인해 드립니다.'),
  ],['변경 사항은 정해진 기간 안에 등기해야 하며, 늦어지면 과태료가 부과될 수 있습니다.',
     '이사회·주주총회 같은 회사 내부 절차가 맞아야 등기를 할 수 있습니다.',
     '회사 형태와 변경 내용에 따라 준비할 것이 크게 달라집니다.']) + \
  proc('appeal','행정심판','행정기관의 처분이 부당하다고 느끼시는 분 (영업정지, 운전면허 취소 등)',[
    ('상담','처분 내용과 그동안의 경위를 확인합니다.'),
    ('청구서 작성','주장과 근거를 정리해 행정심판 청구서를 작성합니다.'),
    ('청구와 심리','행정심판위원회에 청구하고, 심리 과정에서 필요한 자료에 대응합니다.'),
    ('재결','위원회의 판단(재결)을 받아 결과를 안내해 드립니다.'),
  ],['청구할 수 있는 기간이 정해져 있어 처분을 받으면 서둘러 상담해 주세요.',
     '사실관계와 주장을 근거와 함께 정리하는 것이 중요합니다.',
     '처분의 효력을 잠시 멈추는 집행정지 신청을 함께 검토해야 할 수 있습니다.']) + \
  proc('visa','외국인 체류·비자','국내에 머무는 외국인, 외국인 가족이나 근로자를 초청하려는 분',[
    ('상담','체류 목적과 현재 체류 자격을 확인합니다.'),
    ('서류 준비','신청에 필요한 서류를 안내하고 준비를 도와드립니다.'),
    ('신청 대행','출입국 관서에 신청 서류를 제출합니다.'),
    ('결과 안내','처리 결과를 확인하고 이후 일정을 안내해 드립니다.'),
  ],['체류 자격마다 요건과 준비할 것이 다릅니다.',
     '체류 기간이 끝나기 전에 처리해야 불이익을 피할 수 있습니다.',
     '서류가 부족하면 처리가 늦어지거나 다시 신청해야 할 수 있습니다.']) + \
  '</div><p class="note" style="margin-top:24px">위 내용은 일반적인 흐름이며, 사건마다 진행 방법과 필요한 서류가 다릅니다. 내 상황에 맞는 방법은 상담으로 확인해 주세요.</p></div></section>' + CTA
page('process.html', '업무별 절차 안내', '부동산 경매입찰, 개인회생, 개인파산, 상속등기가 어떤 순서로 진행되는지 단계별로 안내합니다.', process, '<script src="b.js?v='+VER+'"></script><script src="ptabs.js?v='+VER+'"></script>', only='B')


for fn,title,desc,body,scripts,only in PAGES:
    for v in only:
        render(fn,title,desc,body,scripts,v)

# 예전 주소를 새 위치로 넘겨 주는 페이지
def redirect(path, to):
    os.makedirs(os.path.dirname(os.path.join(OUT, path)), exist_ok=True)
    open(os.path.join(OUT, path), 'w', encoding='utf-8').write(f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="robots" content="noindex">
<link rel="canonical" href="{to}"><meta http-equiv="refresh" content="0; url={to}">
<script>location.replace("{to}"+location.hash)</script><title>이동 중</title></head>
<body><p><a href="{to}">새 주소로 이동</a></p></body></html>
''')
for fn,title,desc,body,scripts,only in PAGES:
    if 'B' in only: redirect('b/'+fn, '../'+fn)
redirect('cases.html', 'process.html')
# 검색엔진용 사이트맵과 robots.txt (메인 페이지만, old/ 제외)
import datetime
today = datetime.date.today().isoformat()
urls = ''.join(f'  <url><loc>{BASE}{"" if fn=="index.html" else fn}</loc><lastmod>{today}</lastmod></url>\n' for fn in META)
open(os.path.join(OUT,'sitemap.xml'),'w',encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'</urlset>\n')
open(os.path.join(OUT,'robots.txt'),'w',encoding='utf-8').write(f'User-agent: *\nDisallow: /old/\nDisallow: /b/\n\nSitemap: {BASE}sitemap.xml\n')
print('ok')
