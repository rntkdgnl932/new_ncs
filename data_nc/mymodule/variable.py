# pyqt5 부분
rowcount = 0
colcount = 0
rehi_ = 'none'
thisRow = 0
thisCol = 0
table_datas = ""
onCharacter = 0
onDunjeon = "none"
onHunt = "none"
onMaul = "none"

isgloballoop = False

# 기존 오토모드 관련###############################################
one_cla_id = "none"
one_cla_pw = "none"
two_cla_id = "none"
two_cla_pw = "none"
# 1번
mynumber_1 = 0
mylevel_1 = 0
mymoney_1 = 0
mypower_1 = 0
mypotion_1 = 9999
myId_1 = 0
# 2번
mynumber_2 = 0
mylevel_2 = 0
mymoney_2 = 0
mypower_2 = 0
mypotion_2 = 9999
myId_2 = 0
# 현재실행중인 클라우드
now_cla = 'none'
global_howcla = 'none'

# 나크 관련
# 버젼
# import os

dir_path = "C:\\my_games\\nightcrow\\data_nc"
file_path = dir_path + "\\mymodule\\version.txt"

with open(file_path, "r", encoding='utf-8-sig') as file:
    version_ = file.read()
    print("version???", version_)

this_game = "나이트크로우"

# 자동모드 관련
potion_count = 0

# 던전 진행중 여부
now_dungeon_ing = False
skill_checked_ = False
now_ing_schedule = "none"
# 강제로 돈벌기
forcee_not_sub = False
force_sub_quest = False
onForceGold = 5000000
onForceGoldSpot = "none"
onForceGoldSpot_go = "none"
onCollection = False

just_one = False

# 얼음 동굴
who_attack_ = False

# 일일퀘스트
sub_quest_count = 0

# 가방 열어 골드 파악하는거 서브퀘스트일때 and 300초마다
bag_open_count = 0