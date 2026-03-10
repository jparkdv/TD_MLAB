# 0032_list_comprehension.py (리스트 컴프리헨션 기초)
# 목적: 반복문과 조건문을 한 줄로 결합하여 효율적인 데이터 처리 리스트 생성
# -------------------------------------------------------
# Scenario:
# - 전시용 소스 파일 중 특정 키워드('Night')가 포함된 파일만 선별함.
# - 선별된 파일들에 일괄적으로 상태 표시 태그('_ready')를 추가함.
# -------------------------------------------------------

# 1. 원본 파일 리스트
all_files = ["Seoul_Day.jpg", "Seoul_Night.jpg", "Busan_Night.png", "Jeju_Sea.jpg", "ThePuzzle_Night.mp4"]

# [방법 A] 기존의 for 문 방식 (비교용)
night_files_old = []
for f in all_files:
    if "Night" in f:
        night_files_old.append(f)
print(f"1. 기존 방식 결과: {night_files_old}")

# [방법 B] 리스트 컴프리헨션 방식 (Modern Python)
# 💡 힌트: [f for f in all_files if "Night" in f]
# 여기서 한 발 더 나아가 파일명 뒤에 "_ready"를 붙여보세요.
# 💡 구조: [파일명 + "_ready" for 파일명 in 전체리스트 if "Night" in 파일명]
night_files_new = [f + "_ready" for f in all_files if "Night" in f]

print(f"2. 컴프리헨션 결과: {night_files_new}")

# 3. 추가 미션: 파일명들을 모두 대문자(upper())로 바꿔서 새로운 리스트를 만들어보세요.
# (조건 없이 모든 파일을 대문자로 변환)
upper_files = [f.upper() for f in all_files]
print(f"3. 일괄 대문자 변환: {upper_files}")