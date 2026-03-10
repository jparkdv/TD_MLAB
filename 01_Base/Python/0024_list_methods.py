# 0024_list_methods.py
# 목적: 리스트의 주요 메서드(append, insert, remove)를 사용하여 데이터 편집하기
# -------------------------------------------------------
# Scenario:
# - 전시 중 관람객의 피드백을 반영하여 BGM 플레이리스트를 실시간으로 수정함.
# - 새로운 곡을 리스트 맨 뒤에 추가하거나, 특정 순서에 중요한 곡을 삽입함.
# - 더 이상 사용하지 않는 곡은 리스트에서 삭제하여 시스템을 최적화함.
# - 리스트가 변할 때마다 결과를 출력하여 변경 사항을 확인함.
# -------------------------------------------------------

# 1. 초기 리스트 구성
playlist = ["Opening", "Midpoint", "Closing"]
print(f"1. 초기 상태: {playlist}")

# 2. 맨 뒤에 추가 (append)
playlist.append("Encore") # 결과: [..., "Encore"]

# 3. 특정 위치(인덱스 1)에 삽입 (insert)
# "Opening"과 "Midpoint" 사이에 "Intro"가 들어갑니다.
playlist.insert(1, "Intro") 
print(f"2. 삽입 후: {playlist}")

# 4. 다양한 삭제 방법 실습
# (1) 이름으로 삭제 (remove)
playlist.remove("Midpoint") 

# (2) 위치 번호로 삭제 (del)
# 현재 인덱스 2에 있는 "Closing"을 삭제합니다.
del playlist[2] 

# (3) 맨 마지막 데이터 뽑아내기 (pop)
# 리스트 끝에 있던 "Encore"를 삭제합니다.
playlist.pop() 

# 5. 최종 결과 확인
# 모든 공정을 거치고 남은 정예 멤버들만 출력됩니다.
print(f"3. 최종 상태: {playlist}") # 결과: ['Opening', 'Intro']