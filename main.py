import requests
import xml.etree.ElementTree as ET
import pandas as pd


# 상품 정보 조회 함수
def get_product_info(keyword, key):
    base_url = 'http://openapi.11st.co.kr/openapi/OpenApiService.tmall'
    params = {
        'key': key,  # OpenAPI 가입 시 발급받는 32자리 문자 Key
        'apiCode': 'ProductSearch',  # OpenAPI 서비스 코드 → 상품검색 : ProductSearch
        'keyword': keyword,  # 검색 요청 값
        'pageSize': 200,  # 한페이지에 출력되는 상품 수(Default 50, 최대 200)
        'sortCd': 'CP',  # 인기도순
    }
    response = requests.get(base_url, params=params)
    return response.text


# 상품 정보 파싱 함수
def parse_product(xml_data):
    root = ET.fromstring(xml_data)
    products = root.find('Products')

    product_list = []

    for product in products.findall('Product'):
        product_info = {
            'ProductName': product.find('ProductName').text,  # 상품 이름
            'ProductPrice': product.find('ProductPrice').text,  # 상품 가격
            'ProductImage': product.find('ProductImage').text  # 상품 이미지 URL
        }
        product_list.append(product_info)

    return product_list


# 중복된 상품명 제거 함수
def remove_duplicates_by_name(product_list):
    new_list = []
    seen = set()  # 중복 체크를 위한 set

    for product in product_list:
        # 상품 이름을 기준으로 중복 제거
        product_name = product['ProductName']
        if product_name not in seen:
            seen.add(product_name)
            new_list.append(product)

    return new_list


# 엑셀 파일 저장 함수
def save_as_excel(data, filename):
    df = pd.DataFrame(data)  # 데이터프레임 생성
    df.to_excel(filename, index=False)  # 엑셀 파일로 저장, 인덱스는 저장하지 않음


# 실행 코드
key = '{your_api_key}'  # API Key
keyword = ''  # 검색 키워드줄

product_list = []  # 상품 정보를 저장할 리스트
for pageNum in range(1, 101):  # 총 100개 페이지 요청
    xml_data = get_product_info(keyword, key)
    products = parse_product(xml_data)
    for product in products:
        product_list.append(product)

# 중복된 상품명 제거
product_list = remove_duplicates_by_name(product_list)

save_as_excel(product_list, 'product_info.xlsx')  # 엑셀 파일로 저장
