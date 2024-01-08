# 11번가 상품 정보 크롤러

## 🌐 프로젝트 개요

이 프로젝트는 [11번가의 OpenAPI](https://openapi.11st.co.kr/openapi/OpenApiFrontMain.tmall?expCnt=1)를 사용해서 원하는 키워드에 대한 상품 정보를
검색하고, 엑셀 파일로 저장하는 파이썬 프로젝트입니다.

## 🛠️ 프로젝트 개발 환경

프로젝트는 아래 환경에서 개발되었습니다.

> OS: macOS Sonoma   
> IDE: Pycharm  
> Python: 3.8.0

## ✅ 실행 방법

해당 프로젝트를 추가로 개발 혹은 실행시켜보고 싶으신 경우 아래의 절차에 따라 진행해주세요

#### 1. 가상 환경을 생성합니다.

```commandline
python3 -m venv venv
```

#### 2. 가상 환경을 활성화합니다.

```commandline
source venv/bin/activate
```

#### 3. 필요한 라이브러리 다운로드합니다.

- pandas
- requests
- xml.etree.ElementTree
- openpyxl

```commandline
pip install pandas requests openpyxl
```

#### 4. 11번가 OpenAPI에 가입하여 32자리 11ST OPEN API KEY를 발급받습니다.

```text
abcdefghijklmnopqrstuvwxyz123456
```

#### 5. main.py 파일의 key 변수에 발급받은 Key를 입력합니다. (60번째 줄)

```python
key = 'abcdefghijklmnopqrstuvwxyz123456'  # API Key
```

#### 6. keyword 변수에 원하는 검색 키워드를 입력합니다. (61번째 줄)

```python
keyword = '검색 키워드'  # 검색 키워드
```

#### 7. pageNum 범위를 지정합니다. (64번째 줄)

```python
for pageNum in range(1, 101):  # 총 100개 페이지 요청
```

#### 8. 프로그램을 실행하면, 검색된 상품 정보가 product_info.xlsx 파일로 저장됩니다.

## 📊 생성된 엑셀 파일

이 엑셀 파일에는 다음과 같은 3가지 열(column)이 있습니다:

- ProductName: 상품의 이름을 나타냅니다.
- ProductPrice: 상품의 가격을 나타냅니다.
- ProductImage: 상품의 이미지 URL을 나타냅니다.

각 행(row)은 한 개의 상품 정보를 나타내며, 상품 이름, 가격, 이미지 URL의 정보가 담겨 있습니다.

참고) 중복된 상품명을 가진 상품은 제거되어, 각 상품명은 유일(unique)합니다.