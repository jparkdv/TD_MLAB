# 0005_elif_statements.py (다중 조건문)
# 목적: 시스템 상태 모니터링에 따른 실시간 RGB LED 색상 신호 매핑 구현
# -------------------------------------------------------
# Scenario:
# - 통합 관제 시스템의 현재 상태(system_status)를 시각적인 색상 데이터로 변환함.
# - 정상(Normal), 경고(Warning), 오류(Error) 등 각 단계에 최적화된 RGB 값을 할당함.
# - 정의되지 않은 상태값이 들어올 경우, 기본값(White)을 출력하여 시스템의 상시 가동 확인.
#
# Requirements:
# - 시스템 상태 문자열 변수 정의 및 초기화
# - if-elif-else 다중 조건문을 활용한 상태별 로직 분기
# - RGB 튜플(Tuple) 구조를 활용한 색상 데이터 출력 함수(set_rgb_color) 설계
# -------------------------------------------------------

# 1. 상태 변수 설정 (Status Definition)
system_status = "warning"  # 모니터링 중인 장비의 현재 상태

# 2. 색상 신호 생성 엔진 (Color Signal Generation Engine)
def set_rgb_color(status):
    # 각 상태 문자열에 대응하는 RGB(Red, Green, Blue) 채널 값 할당
    if status == "normal":
        # 안전/정상 상태: 녹색(Green) 출력
        print("set_rgb_color((0, 255, 0))")
    elif status == "warning":
        # 주의/경고 상태: 노란색(Yellow) 출력
        print("set_rgb_color((255, 255, 0))")
    elif status == "error":
        # 위험/오류 상태: 빨간색(Red) 출력
        print("set_rgb_color((255, 0, 0))")
    else:
        # 알 수 없는 상태(Undefined): 흰색(White) 기본값 출력
        print("set_rgb_color((255, 255, 255))")

# 3. 디스플레이 업데이트 (Signal Execution)
set_rgb_color(system_status)