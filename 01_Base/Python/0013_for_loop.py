# 0013_for_loop.py (for 반복문)
# 목적: for 반복문을 활용한 시스템 상태 로그 전수 조사 및 실시간 경보 시스템 구현
# -------------------------------------------------------
# Scenario:
# - 전시 운영 중 발생하는 수많은 장비 상태 로그(status_log)를 자동으로 순회함.
# - 개별 로그를 분석하여 'Error'와 같은 치명적인 결함을 즉시 탐지함.
# - 위험 요소 발견 시 관리자에게 즉각 경보(Alert)를 발송하고, 평시에는 현재 상태를 보고함.
#
# Requirements:
# - 장비 상태 데이터를 포함하는 로그 리스트 생성
# - for 문을 활용한 리스트 요소의 반복 순회(Iteration) 로직 설계
# - if-else 조건문을 결합하여 특정 상태값("Error")에 대한 우선적 필터링
# - f-string을 활용한 동적 상태 보고 메시지 출력
# -------------------------------------------------------

# 1. 상태 로그 데이터 입력 (Log Data Ingestion)
status_log = ["Normal", "Normal", "Error", "Warning", "Normal"]

# 2. 실시간 자동 모니터링 루프 (Real-time Monitoring Loop)
# 리스트 내의 모든 항목을 'status'라는 변수에 담아 하나씩 검사합니다.
for status in status_log:
    # [검사] 현재 로그가 'Error' 상태인지 판별
    if status == "Error":
        # 치명적 결함 발견 시 긴급 경보 출력
        print("ALERT: System Error Detected!")
    else:
        # 정상 또는 주의 상태일 경우 현재 상황 보고
        print(f"System Status: {status}")

# 3. 분석 완료 보고 (End of Analysis)
print("Log analysis completed.")