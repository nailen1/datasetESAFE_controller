# Dataset ESAFE Controller 모듈 설계

## 목적
- Excel 파일(.xls)의 내용을 분석하여 필요한 변수를 추출
- 추출된 변수를 이용하여 파일명을 체계적으로 변경

## 시스템 구조

### 입력
- 위치: `data/dataset-menuESAFE500068/*.xls`
- 파일 형식: Excel (.xls)
- 현재 파일명 패턴: `BCI_REDM08003V_YYYYMMDDHHMMSS.xls`

### 처리 과정
1. Excel 파일 읽기
2. 필요한 변수 추출
3. 새로운 파일명 생성
4. 파일명 변경

### 사용 기술
- Python
  - pandas: Excel 파일 읽기
  - os/pathlib: 파일 시스템 작업

## 구현 계획
1. Excel 파일 분석기 구현
2. 파일명 생성기 구현
3. 파일 시스템 작업 처리기 구현
4. 메인 컨트롤러 구현
