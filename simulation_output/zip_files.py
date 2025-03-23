# zip all the files in "./salesagent_neg/"

import os
import zipfile

zip_file_name = "./salesagent_neg_wo_dup_chitchat_e10.zip"
if os.path.exists(zip_file_name):
    os.remove(zip_file_name)

with zipfile.ZipFile(zip_file_name, "w") as zip_file:
    for root, dirs, files in os.walk("./salesagent_neg_wo_dup_chitchat_e10//"):
        for file in files:
            zip_file.write(os.path.join(root, file))
