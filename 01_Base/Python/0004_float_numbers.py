# 0004_float_numbers.py (실수자료형)
# 목적: 목표 조도 대비 현재 밝기를 분석하여 정밀 광도 보정 로직 구현
# -------------------------------------------------------
# Scenario:
# - 전시 작품의 최적 시각 효과를 위해 설정된 목표 밝기(target_brightness)를 유지함.
# - 실시간 조도 센서로부터 감지된 밝기(current_brightness)를 기준값과 비교함.
# - 광량이 부족할 경우 시스템은 자동으로 출력 증강(increase) 신호를 보냄.
# - 목표치 충족 시 장비 소모를 방지하기 위해 현 상태 유지(maintain) 모드로 전환함.
#
# Requirements:
# - 목표 및 현재 조도 변수 설정 (Float Type: 0.0 ~ 1.0)
# - 부등호 연산자를 통한 광량 부족 여부 실시간 판별
# - 상태 진단 및 보정 명령 출력을 위한 매개변수 기반 함수(check_lighting) 설계
# -------------------------------------------------------

# 1. 조도 설정 파라미터 (Lighting Parameters)
target_brightness = 0.75   # 작품의 표준 권장 밝기
current_brightness = 0.45  # 현재 센서 측정 밝기

# 2. 광도 보정 엔진 (Luminance Correction Engine)
def check_lighting(current, target):
    # 현재 밝기가 목표 수치에 미달하는지 검사
    if current < target:
        # 광량이 부족한 경우 조도 증강 명령 하달
        print("check_lighting('increase')")
    else:
        # 목표 조도 도달 또는 초과 시 상태 유지
        print("check_lighting('maintain')")

# 3. 캘리브레이션 실행 (Run Calibration)
check_lighting(current_brightness, target_brightness)