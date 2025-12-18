# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("balraj98/horse2zebra-dataset")

# print("Path to dataset files:", path)

import kagglehub
import os 
cwd = os.getcwd()
DATA_DIR = os.path.join(cwd, 'data')
CT_2_MRI_DIR = os.path.join(DATA_DIR, 'ct2mri')
print(CT_2_MRI_DIR)
# # Download latest version
# Download latest version
path = kagglehub.dataset_download("darren2020/ct-to-mri-cgan")
# link: https://www.kaggle.com/datasets/darren2020/ct-to-mri-cgan
print("Path to dataset files:", path)