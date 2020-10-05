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

#if __name__ == '__main__':
#     filewrite()
#     fileopen()

