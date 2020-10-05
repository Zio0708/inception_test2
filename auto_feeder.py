from fileIO import fileopen
from retrain_run_inference import run_inference_on_image
time_table =[]
if __name__ == '__main__':
     pet_infos = fileopen() # 제품 실행시 파일에 저장되어있는 애완동물의 정보를 부른다.

     #라즈베리 파이가 작동하는 타임 테이블을 만들고 시간 탐색
     #시간탐색은 thread로 실시간 작동

     #해당 시간표가 있을 때 배식량의 20프로를 배식한다.
     pet_foodAmount = "1/5"
     time_table_petname = "몽몽이"
     #이후에 탐색 기능을 실행하여 시간표의 이름과 일치하는지 확인한다.(정확도 70이상)
     while time_table_petname !=run_inference_on_image():
        #30초마다 재실행한다.
        print("30초가 지나 재탐색을 실시합니다")
     #탐색된 뒤에는 해당 배식량에 맞게 배식기능을 돌린다. pet_foodAmount 4/5


# 제품 실행시 파일에 저장되어있는 애완동물의 정보를 부른다.
# 배식 시간에서 +- 10분으로 라즈베리파이의 시간을 탐색한다. (search) -> 따로 저장해두는게 좋을듯?
# 해당 하는 시간 사이에 있다면 애완동물을 호출하면서 카메라를 작동시킨다.
# 카메라에 애완동물이 탐색
# 참고 : 해당 애완동물 이름 리스트 = 학습된 머신러닝의 라벨 리스트
# 머신러닝 분류 결과 이름에서 애완동물의 이름을 찾아 애완동물 객체를 반환
# 반환된 객체에서 배식량을 호출하여 분할 배식 기능을 작동시킨다
# 배식량(1~5)에서 해당 배식량이 될때까지 모터를 가동.