import nibabel as nib
from PIL import Image
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

def nii_to_jpg_fon(veri_cekilecek_path,kaydedilecek_path):
    # path = 'yeni_dosya/volume-0.nii'
    path = veri_cekilecek_path

    nii_img = nib.load(str(path))

    degisken = []
    degisken.append(path.split("/"))
    degisken = degisken[0][-1:]
    try:
        os.mkdir(f'{kaydedilecek_path}/{degisken[0]}')
    except:
        pass

    nii_data = nii_img.get_fdata()
    shape = nii_data.shape
    for i in range(shape[2]):
        layer = nii_data[:,:,i]
        image = Image.fromarray(layer).convert('L')
        image = image.rotate(90)
        image.save(f'{kaydedilecek_path}/{degisken[0]}/layer_name_{i}.jpg')

    file_list = []
    for dirname, _, filenames in os.walk(f'{kaydedilecek_path}/{degisken[0]}'):
        for filename in filenames:
            file_list.append((dirname, filename))

    return len(file_list),kaydedilecek_path

