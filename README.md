# 유병열 법무사·행정사 사무소 홈페이지

정적 사이트입니다. GitHub Pages로 배포합니다.

- `*.html` 페이지 (생성물)
- `style.css` 디자인
- `calc.js` 법무사보수표(2020. 7. 23. 시행) 기본보수 상한액 산정 데이터
- `main.js` 보수 계산기와 화면 동작
- `img/` 사진과 로고

페이지(`index.html`, `about.html` 등)는 `tools/gen.py`로 생성합니다. 문구를 바꾸려면 이 파일을 고친 뒤 `python3 tools/gen.py`를 실행하세요.

## A/B 버전

- 메인(B 버전): 루트 (`index.html` 등). 메뉴에 '업무별 절차'(`process.html`).
- A 버전(보관용): `old/` 폴더. 메뉴에 '사례·후기'. CSS·JS·이미지는 루트 파일을 같이 쓰고, 검색엔진 색인은 막아 둠(noindex).
- 예전 `b/` 주소와 루트 `cases.html`은 새 위치로 자동 이동합니다.
- 모두 `python3 tools/gen.py` 한 번으로 생성됩니다.
