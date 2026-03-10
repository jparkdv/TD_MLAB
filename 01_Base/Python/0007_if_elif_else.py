# 0007_if_elif_else.py (if-elif-else 구조와 우선순위)
# 목적: 다중 센서 기반 비상 상황 감지 및 시스템 즉각 정지(E-Stop) 제어
# -------------------------------------------------------
# Scenario:
# - 화재, 지진 등 인명 및 장비 피해가 예상되는 비상 상황 발생 시 시스템을 즉시 정지함.
# - 비상 정지 신호(emergency_status)는 시스템 모드와 상관없이 최우선 순위로 처리함.
# - 정상 운영(Operation) 모드에서는 지속적인 모니터링 상태를 유지함.
# - 유지보수(Maintenance) 및 대기 상태에서는 별도의 안전 프로토콜을 가동함.
#
# Requirements:
# - 비상 상태(Boolean) 및 운영 모드(String) 변수 설정
# - if-elif-else 구조를 활용한 우선순위 기반 조건 분기
# - 비상 정지 및 운영 상태 보고를 위한 안전 점검 함수(check_safety) 구현
# -------------------------------------------------------

# 1. 안전 모니터링 지표 (Safety Monitoring Indicators)
emergency_status = True   # 비상 상황 발생 여부 (True: 즉시 정지 필요)
system_mode = "Operation" # 현재 시스템 가동 모드

# 2. 통합 안전 제어 유닛 (Integrated Safety Control Unit)
def check_safety(is_emergency, mode):
    # [최우선 순위] 비상 상황 발생 시 모든 프로세스 즉시 차단
    if is_emergency:
        print("EMERGENCY STOP! System Halted.")
    
    # [2순위] 정상 운영 상태 확인
    elif mode == "Operation":
        print("Normal Operation Continuing...")
    
    # [3순위] 기타 대기 또는 유지보수 상태
    else:
        print("System Idle / Maintenance Mode")

# 3. 실시간 안전 점검 실행 (Execute Safety Audit)
check_safety(emergency_status, system_mode)