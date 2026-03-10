# 0001_variable_basics.py (변수기초)
# 목적: 관객의 물리적 거리에 반응하는 기초 인터랙션(Interactive) 로직 구현
# -------------------------------------------------------
# Scenario:
# - 센서로부터 들어오는 관객의 거리(visitor_distance)를 실시간으로 모니터링함.
# - 설정한 임계값(threshold_distance)보다 관객이 가까워지면 미디어 작품을 자동 재생함.
# - 관객이 범위를 벗어나면 장비의 부하를 줄이기 위해 재생을 즉시 정지함.
#
# Requirements:
# - 관객 거리와 기준 거리 변수 정의 및 초기화
# - 비교 연산자(<)를 활용한 근접 여부 판별
# - 독립적인 실행을 위한 인터랙션 함수(play_artwork) 설계
# -------------------------------------------------------

# 1. 환경 설정 (Environment Setup)
visitor_distance = 1.0    # 현재 관객 거리 (단위: m)
threshold_distance = 1.2  # 트리거 발생 기준 거리 (단위: m)

# 2. 인터랙션 로직 함수 (Interaction Logic Function)
def play_artwork(vis_dist, thr_dist):
    if vis_dist < thr_dist:
        # 관객이 기준 거리 내로 진입했을 때의 액션
        print("play_artwork('start')")
    else:
        # 관객이 기준 거리 밖에 있을 때의 액션
        print("play_artwork('stop')")

# 3. 시스템 실행 (System Execution)
play_artwork(visitor_distance, threshold_distance)