# 0003_boolean_logic.py (불리언 자료형)
# 목적: 전원 상태 및 운영 시간을 결합한 시스템 자동 활성화 로직 구현
# -------------------------------------------------------
# Scenario:
# - 전시 장비의 무분별한 가동을 방지하기 위해 전원 상태와 운영 시간을 동시 검전함.
# - 물리적인 전원(power_on)이 공급되고 있으며, 현재 시각이 관람 시간(10시~18시) 내에 있을 때만 시스템을 활성화함.
# - 두 조건 중 하나라도 충족되지 않을 경우, 안전과 에너지 절약을 위해 시스템을 비활성화 상태로 유지함.
#
# Requirements:
# - 전원 상태(Boolean) 및 현재 시간(Integer) 변수 정의
# - 논리 연산자 'and'와 범위 비교 연산자를 결합한 복합 조건문 설계
# - 시스템 활성화/비활성화 상태를 결정하는 제어 함수(check_system) 구현
# -------------------------------------------------------

# 1. 운영 환경 변수 (Operating Environment Variables)
power_on = True      # 메인 전원 공급 상태 (True: 공급 중)
current_hour = 14    # 현재 시각 (24시간 형식)

# 2. 시스템 스케줄링 엔진 (System Scheduling Engine)
def check_system(is_on, hour):
    # 전원이 켜져 있고(True), 시간이 10시 이상 18시 미만인 경우
    if is_on and 10 <= hour < 18:
        # 모든 운영 조건 충족 시 시스템 활성화
        print("check_system('activate')")
    else:
        # 전원 차단 혹은 운영 시간 외일 경우 시스템 비활성화
        print("check_system('deactivate')")

# 3. 자동 제어 프로세스 가동 (Automatic Control Process)
check_system(power_on, current_hour)