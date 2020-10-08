import os

from retrain_run_inference import run_inference_on_image
from PetInfo import Pet
def filewrite(petInfo):
    petInfo_petName = petInfo.petName
    petInfo_foodName = petInfo.foodName
    petInfo_foodAmount = petInfo.foodAmount
    petTxt = petInfo_petName + ".txt"
    f = open(petTxt, 'w')
    petInfo_data = petInfo_petName+" "+petInfo_foodName +" "+ petInfo_foodAmount
    f.write(petInfo_data)
    f.close()
def fileopen():
    f = open("pet_info.txt", 'r')
    pet_infos =[]
    while True:
        line = f.readline()
        if not line: break
        pet_line = line.split(" ")
        pet_info = Pet(pet_line[0],pet_line[1],pet_line[2],pet_line[3])
        pet_infos.append(pet_info)
    f.close()
    return pet_infos

def search_new_image():
    files_Path = "/home/pi/capture/"  # 파일들이 들어있는 폴더
    file_name_and_time_lst = []
    # 해당 경로에 있는 파일들의 생성시간을 함께 리스트로 넣어줌.
    for f_name in os.listdir(f"{files_Path}"):
        written_time = os.path.getctime(f"{files_Path}{f_name}")
        file_name_and_time_lst.append((f_name, written_time))
    # 생성시간 역순으로 정렬하고,
    sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
    # 가장 앞에 이는 놈을 넣어준다.
    recent_file = sorted_file_lst[0]
    recent_file_name = recent_file[0]
    return recent_file_name

#if __name__ == '__main__':
#     filewrite()
#     fileopen()

