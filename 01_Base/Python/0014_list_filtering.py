# 0014_list_filtering.py (리스트 필터링)
# 목적: 반복문과 조건문을 결합하여 특정 상태(Error) 데이터만 선별 추출 및 수집
# -------------------------------------------------------
# Scenario:
# - 전체 운영 리포트(all_reports)에서 시스템 안정성을 위협하는 오류 항목만 추출함.
# - 추출된 오류 데이터는 별도의 리스트(error_list)에 저장하여 후속 정밀 분석에 활용함.
# - 최종적으로 발생한 오류의 총수량을 파악하여 시스템 교체 및 수리 여부를 결정함.
#
# Requirements:
# - 원본 데이터 리스트와 수집용 빈 리스트(Empty List) 생성
# - for 문을 통한 전수 조사 및 if 문을 활용한 특정 문자열 필터링
# - .append() 메소드를 사용하여 선별된 데이터를 새로운 리스트에 축적
# - 필터링된 결과물 및 데이터의 총 길이(len) 출력
# -------------------------------------------------------

# 1. 원본 데이터 및 수집 바구니 준비 (Initial Data & Buffer)
all_reports = ["Normal", "Error", "Normal", "Error", "Warning"]
error_list = []

# 2. 선별적 데이터 수집 루프 (Selective Collection Loop)
for report in all_reports:
    # 현재 리포트가 'Error'인 경우에만 수집 실행
    if report == "Error":
        # 조건에 맞는 데이터를 error_list에 추가
        error_list.append(report)

# 3. 최종 필터링 결과 보고 (Filtered Results Report)
print("Collected Error Reports:", error_list)
print("Total Error Count:", len(error_list))