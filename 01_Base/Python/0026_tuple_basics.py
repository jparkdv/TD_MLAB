# 0026_tuple_basics.py (튜플 기초와 불변성)
# 목적: 영화 및 전시 영상 제작을 위한 불변의 기술 규격(Technical Specs) 관리
# -------------------------------------------------------
# Scenario:
# - 디지털 영화 및 전시 영상의 마스터 포맷 설정을 관리하는 시스템을 구축함.
# - 해상도(Width, Height)와 초당 프레임 수(FPS)는 제작 공정상 절대 수정되어선 안 됨.
# - 데이터의 무결성을 보장하기 위해 수정이 불가능한 튜플(Tuple)을 사용함.
# - 튜플 언패킹을 통해 복잡한 규격 데이터를 개별 변수로 신속하게 분리함.
#
# Requirements:
# - 영상 규격 데이터(3840, 2160, 24)를 포함하는 튜플 'master_specs' 생성
# - 인덱싱을 활용한 특정 위치(FPS)의 데이터 조회 및 출력
# - 튜플 언패킹을 통한 다중 변수(width, height, fps) 동시 할당
# - 튜플 수정 시도 시 발생하는 에러(TypeError) 확인 및 원인 분석
# -------------------------------------------------------

# 1. 마스터 기술 규격 설정 (Tuple Creation)
# 💡 튜플은 소괄호()를 사용하여 데이터를 묶으며, 리스트와 달리 '읽기 전용'입니다.
master_specs = (3840, 2160, 24)
target_fps = master_specs[2]
print(f"1. Project FPS: {target_fps}")

# 2. 특정 데이터 조회 (Indexing)
# master_specs에서 세 번째 값인 FPS(24) 정보만 가져와서 출력하세요.
master_specs = (3840, 2160, 24)
width, height, fps = master_specs
width = master_specs[0]
height = master_specs[1]
fps = master_specs[2]

print(f"2. Resolution: {width}x{height}, Frame Rate: {fps}fps")

# 3. 데이터 언패킹 (Unpacking)
# 💡 튜플의 값을 artist, id_no, year 변수에 각각 할당하여 출력하세요.
# 힌트: 변수명1, 변수명2, 변수명3 = 튜플명
artist, id_number, year = master_specs
master_specs = ("jei", 20260202, 2026)
artist = master_specs[0]
id_number = master_specs[1]
year = master_specs[2]

print(f"3. Artist: {artist}, ID: {id_number}, Year: {year}")

# 4. 불변성 테스트 (Immutability Test)
# 🚨 아래 코드의 주석을 해제하고 실행하면 에러가 발생합니다.
# master_specs[2] = 60 

# [TA의 백과사전 정리]
# 발생 에러 명칭: TypeError: 'tuple' object does not support item assignment
# 이유: 튜플은 한 번 생성되면 내부 요소를 개별적으로 변경할 수 없는 '불변(Immutable)' 객체입니다.
# 아까처럼 변수 전체를 '새 튜플'로 갈아치울 순 있어도, 튜플 내부의 특정 값만 쏙 빼서 바꾸는 것은 절대 허용되지 않습니다.
# 이 강한 고집 덕분에 시스템의 핵심 규격이 안전하게 보호됩니다.