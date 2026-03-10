# 0006_nested_if.py (중첩 조건문)
# 목적: 전원 상태 및 배터리 잔량에 따른 지능형 성능 모드 최적화 시스템 구현
# -------------------------------------------------------
# Scenario:
# - 장비의 전원 공급 여부를 우선 확인한 후, 가용 배터리 자원에 따라 성능을 차등화함.
# - 배터리가 충분할 때는 작품의 고해상도 출력을 지원(High Performance)함.
# - 배터리가 부족해지면 시스템 부하를 낮추는 절전 모드(Power Saving)로 자동 전환함.
# - 전원 자체가 차단된 경우에는 시스템 오프 상태임을 명확히 보고함.
#
# Requirements:
# - 전원 상태(Boolean) 및 배터리 수치(Integer) 변수 정의
# - 중첩 조건문(Nested if)을 활용한 단계별 전력 관리 로직 구축
# - 배터리 구간별(80 초과 / 20~80 / 20 미만) 성능 모드 출력 함수(manage_power) 설계
# -------------------------------------------------------

# 1. 전력 모니터링 변수 (Power Monitoring Variables)
power_on = True       # 메인 시스템 전원 인가 여부
battery_level = 15    # 현재 감지된 배터리 잔량 (%)

# 2. 지능형 전력 제어 유닛 (Intelligent Power Control Unit)
def manage_power(is_active, level):
    # [1단계] 시스템 활성화 상태 확인
    if is_active:
        # [2단계] 배터리 잔량에 따른 성능 모드 세부 분기
        if level > 80:
            # 배터리 충분: 최대 출력 모드
            print("manage_power('High Performance Mode')")
        elif 20 <= level <= 80:
            # 배터리 보통: 표준 밸런스 모드
            print("manage_power('Standard Mode')")
        else:
            # 배터리 부족: 저전력 보호 모드
            print("manage_power('Power Saving Mode')")
    else:
        # 시스템 비활성화 상태 보고
        print("manage_power('Device is Off')")

# 3. 전력 관리 프로세스 실행 (Execute Management Process)
manage_power(power_on, battery_level)