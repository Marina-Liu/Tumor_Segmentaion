import nibabel as nib

path = './BraTS-Data/labelsTr/BRATS_003.nii.gz'

image = nib.load(path)
print("success")