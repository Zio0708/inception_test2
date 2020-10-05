from fileIO import fileopen
from retrain_run_inference import run_inference_on_image
from thread_test import search_time
from feeder_morter import give_food
import time
time_table = ["22:00", "11:00", "19:45"]
if __name__ == '__main__':

     #init으로 애완동물의 정보를 꺼낸다.
     pet_infos = fileopen() # 제품 실행시 파일에 저장되어있는 애완동물의 정보를 부른다.

     # autofeeder은 thread로 실시간 작동한다.
     com_time = search_time(time_table)#라즈베리 파이가 작동하는 타임 테이블을 만들고 시간을 탐색한다.

     #해당 시간에 맞는 pet의 배식량을 검색한다.
     for pet_ary in pet_infos :
         if pet_ary.foodTime == com_time :
             pet_info = pet_ary
             break;

     pet_foodAmount = pet_info.foodAmount
     pet_foodName = pet_info.foodName
     pet_petName = pet_info.petName

     #해당 시간표가 있을 때 배식량의 20프로를 배식한다.
     give_food(pet_foodName , pet_foodAmount*0.2 )

     #해당 시간표에 맞는 애완동물의 이름을 확인한다.
     pet_petName = "몽몽이"

     #이후에 탐색 기능을 실행하여 시간표의 이름과 일치하는지 확인한다.(정확도 70이상)
     time_check = 0 #3분 탐색을 위한 카운터.

     while pet_petName !=run_inference_on_image():
        #30초마다 재실행한다.
        time_check += 30
        time.sleep(30)
        print("30초가 지나 재탐색을 실시합니다")
        if time_check == 180 : #3분 동안 탐색 후 먹지 않으면 취소한다.
            #취소된 애완동물의 정보는 로그로 저장한다.
            print("3분이 지나 탐색을 중단합니다.")
            break

     #탐색된 뒤에는 해당 배식량에 맞게 배식기능을 돌린다. pet_foodAmount 4/5
     give_food(pet_foodName, pet_foodAmount * 0.8)

     #다시 되돌아가 시간 탐색을 실시한다.

# 제품 실행시 파일에 저장되어있는 애완동물의 정보를 부른다.
# 배식 시간에서 +- 10분으로 라즈베리파이의 시간을 탐색한다. (search) -> 따로 저장해두는게 좋을듯?
# 해당 하는 시간 사이에 있다면 애완동물을 호출하면서 카메라를 작동시킨다.
# 카메라에 애완동물이 탐색
# 참고 : 해당 애완동물 이름 리스트 = 학습된 머신러닝의 라벨 리스트
# 머신러닝 분류 결과 이름에서 애완동물의 이름을 찾아 애완동물 객체를 반환
# 반환된 객체에서 배식량을 호출하여 분할 배식 기능을 작동시킨다
# 배식량(1~5)에서 해당 배식량이 될때까지 모터를 가동.