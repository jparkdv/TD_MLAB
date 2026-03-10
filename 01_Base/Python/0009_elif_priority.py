# 0009_elif_priority.py (다중 elif 우선순위)
# 목적: 안전, 보안, 전력을 통합 분석하여 시스템의 최종 동작 상태를 결정하는 중앙 제어 유닛 구현
# -------------------------------------------------------
# Scenario:
# - 전시장의 모든 센서 데이터를 종합하여 시스템의 가동 우선순위를 결정함.
# - [우선순위 1] 비상 상황(Emergency): 인명 및 장비 보호를 위해 다른 모든 상태를 무시하고 즉시 정지.
# - [우선순위 2] 보안(Privacy): 안전이 확보된 상태에서 관객의 사생활 보호 정책을 다음으로 적용.
# - [우선순위 3] 자원(Battery): 정책적 문제가 없을 시, 현재 가용 에너지를 체크하여 운영 모드 결정.
# - 모든 조건이 충족될 경우에만 시스템의 표준 운영(Normal Recording)을 승인함.
#
# Requirements:
# - 비상 상태(Boolean), 보안 모드(Boolean), 배터리 수치(Integer) 변수 정의
# - 다중 if-elif-else 구조를 활용한 계층적 우선순위 로직 설계
# - 복합 상태를 진단하고 최종 명령을 하달하는 통합 제어 함수(master_control) 구현
# -------------------------------------------------------

# 1. 통합 상태 모니터링 데이터 (Integrated Status Data)
emergency_status = False  # 비상 정지 신호
privacy_mode = False      # 프라이버시 보호 모드
battery_level = 15        # 현재 배터리 잔량 (%)

# 2. 중앙 제어 마스터 엔진 (Central Control Master Engine)
def master_control(is_emergency, is_privacy, battery):
    # [Level 1] 최상위 안전 점검
    if is_emergency:
        print("CRITICAL: Emergency Stop!")
        
    # [Level 2] 차순위 보안 정책 적용
    elif is_privacy:
        print("Privacy Active: Cameras OFF")
        
    # [Level 3] 운영 자원 상태 확인
    elif battery < 20:
        print("Low Battery: Saving Mode")
        
    # [Level 4] 모든 검증 통과 시 표준 운영 가동
    else:
        print("System Normal: Recording...")

# 3. 마스터 시스템 가동 (Execute Master System)
master_control(emergency_status, privacy_mode, battery_level)