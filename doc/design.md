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

## 파일 이름 변경 기능

### 기능 개요
- `rename_file()`: 파일의 이름을 직접 변경하는 기능
- `EsafeDatasetScanner`: 데이터셋 폴더 내의 모든 파일을 스캔하고 이름을 변경하는 기능

### 구현 세부사항
1. `rename_file()`
   - 입력: 현재 파일명, 새 파일명, (선택적) 폴더 경로
   - 동작: 파일 시스템의 rename 기능을 사용하여 파일명 변경
   - 예외처리: 파일이 존재하지 않을 경우 FileNotFoundError 발생

2. `EsafeDatasetScanner`
   - 초기화: 지정된 폴더 내의 모든 ESAFE 데이터셋 파일 스캔
   - `rename_all()`: 모든 파일의 이름을 표준 형식으로 일괄 변경
   - 진행상황 표시: tqdm을 사용한 진행률 표시
