import os
import cv2
from keras.models import load_model
import numpy as np
import keras
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
def degerlendirme(image):
    new_model = keras.models.load_model("kidney_model")

    img = cv2.imread(image)

    img = cv2.resize(img, (28,28))
    if img.shape[2] ==1:
        img = np.dstack([img, img, img])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img=np.array(img)

    img = img/255
    degisken=[]
    degisken.append(img)
    deger = np.array(degisken)
    sinif=new_model.predict(deger)
    etiket = np.argmax(sinif)

    deger_1 = "{:.1f}".format(sinif[0][0] * 10)
    deger_2 = "{:.1f}".format(sinif[0][1] * 10)
    deger_3 = "{:.1f}".format(sinif[0][2] * 10)
    deger_4 = "{:.1f}".format(sinif[0][3] * 10)


    if etiket ==0:
        tani = "Kist"

    elif etiket ==1:
        tani = "Normal"
    elif etiket ==2:
        tani = "Taş"
    elif etiket ==3:
        tani = "Tümör"
    else:
        tani = "Bulunamadı"



    return [deger_1,deger_2,deger_3,deger_4,etiket,tani]
