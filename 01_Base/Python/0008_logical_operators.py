# 0008_logical_operators.py (논리 연산자)
# 목적: 프라이버시 보호 정책 및 움직임 감지 기반 지능형 녹화 제어 시스템
# -------------------------------------------------------
# Scenario:
# - 관객의 사생활 보호를 위해 프라이버시 모드(is_privacy_mode)를 최우선으로 적용함.
# - 프라이버시 모드가 활성화된 경우, 모든 움직임 감지 및 녹화 기능을 즉시 차단함.
# - 보호 모드가 해제된 상태에서만 움직임(motion_detected)에 반응하여 녹화 시스템을 가동함.
# - 이벤트가 없는 평시에는 시스템을 절전(Energy Saving) 상태로 유지하여 운영 효율을 높임.
#
# Requirements:
# - 프라이버시 및 모션 감지 상태 변수 정의 (Boolean)
# - 논리 연산자 'not'을 활용한 모드 반전 및 조건 결합 로직 구축
# - 상황별 기록 승인/차단 및 절전 상태 출력 함수(manage_privacy) 설계
# -------------------------------------------------------

# 1. 보안 및 감지 설정 (Security & Detection Settings)
privacy_mode = True      # 프라이버시 보호 모드 (True: 녹화 금지)
motion_detected = True   # 실시간 움직임 감지 여부

# 2. 지능형 프라이버시 관리 엔진 (Intelligent Privacy Management Engine)
def manage_privacy(is_privacy, is_motion):
    # [1단계] 프라이버시 보호 정책 확인 (최우선순위)
    if is_privacy:
        print("Privacy Mode ON: Recording Disabled")
    
    # [2단계] 보호 모드 해제(not) 상태에서 움직임이 발생했는지 확인
    elif not is_privacy and is_motion:
        print("Motion Detected: Recording Started")
    
    # [3단계] 감지된 이벤트가 없는 평상시 상태
    else:
        print("System Standby (Energy Saving)")

# 3. 보안 프로토콜 실행 (Execute Security Protocol)
manage_privacy(privacy_mode, motion_detected)