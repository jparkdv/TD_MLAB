# 0018_function_return.py (함수 반환값)
# 목적: return을 활용하여 함수가 계산한 결과값을 프로그램으로 돌려받기
# -------------------------------------------------------
# Scenario:
# - 전시장의 전력 소비량을 미리 계산하여 과부하를 방지하는 시스템을 구축함.
# - 프로젝터는 1대당 200W, 스피커는 1대당 50W의 전력을 소비함.
# - 함수는 장비의 대수를 입력받아 '총 전력량'을 계산하고, 그 값을 반환(return)함.
# - 반환된 값을 변수에 저장하여 최종 보고서 메시지에 활용함.
# -------------------------------------------------------

# 1. 전력 계산 엔진 정의 (Power Calculation Engine)
def calculate_power(projectors, speakers):
    # 장비별 대수에 따른 총 전력량(W) 계산
    total_power = (projectors * 200) + (speakers * 50)
    
    # 계산된 결과값을 프로그램의 메인 흐름으로 반환
    return total_power

# 2. 시스템 가동 및 결과값 수집 (System Execution)
# A홀: 프로젝터 2대, 스피커 4대 세팅
# 함수가 반환한 600W라는 값을 hall_a_power 변수에 저장합니다.
hall_a_power = calculate_power(2, 4)

# 3. 최종 결과 출력 (Final Report)
print(f"[전력 점검] Hall A의 총 전력 소비량은 {hall_a_power}W 입니다.")