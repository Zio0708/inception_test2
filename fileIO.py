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
def fileopen(petInfo_petName):
    petTxt = petInfo_petName + ".txt"
    f = open(petTxt, 'r')
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
# if __name__ == '__main__':
#     filewrite()
#     fileopen()