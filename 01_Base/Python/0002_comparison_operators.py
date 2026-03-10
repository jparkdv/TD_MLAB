# 0002_comparison_operators.py (비교연산자)
# 목적: 전시장 수용 인원 모니터링 및 실시간 입장 통제 시스템 구현
# -------------------------------------------------------
# Scenario:
# - 관객의 안전과 쾌적한 관람 환경을 위해 전시장 내 실시간 인원을 관리함.
# - 최대 수용 인원(max_capacity)을 초과할 경우, 자동으로 입장을 차단하여 과밀 방지.
# - 센서로부터 전달받은 현재 인원(current_visitors)을 기준으로 시스템이 판단함.
#
# Requirements:
# - 현재 관객 수 및 최대 수용 인원 변수 정의 (Integer Type)
# - 비교 연산자(>)를 사용하여 임계값 초과 여부 판별
# - 상황에 따른 입장 승인/거부 로직을 담은 관리 함수(manage_capacity) 설계
# -------------------------------------------------------

# 1. 시스템 설정 (System Configuration)
current_visitors = 12  # 실시간 탐지된 현재 관람객 수
max_capacity = 10      # 전시 공간의 안전 수용 한계치

# 2. 인원 제어 엔진 (Capacity Control Engine)
def manage_capacity(visitors, limit):
    if visitors > limit:
        # 수용 한계를 초과했을 때의 입장 제한 액션
        print("manage_capacity('deny_entry')")
    else:
        # 안전 범위 내에서 입장을 허용하는 액션
        print("manage_capacity('allow_entry')")

# 3. 운영 모드 실행 (Operational Mode)
manage_capacity(current_visitors, max_capacity)