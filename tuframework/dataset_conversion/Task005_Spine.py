#    Copyright 2020 Division of Medical Image Computing, German Cancer Research Center (DKFZ), Heidelberg, Germany
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


import shutil
from batchgenerators.utilities.file_and_folder_operations import *
from tuframework.paths import tuFramework_raw_data
import os
#
if __name__ == "__main__":
    """
    This is the KiTS dataset after Nick fixed all the labels that had errors. Downloaded on Jan 6th 2020    
    """
    base = "/home/ubuntu/liuyiyao/Data/Spine_format"
    task_id = 6
    task_name = "Spine"
    foldername = "Task%03.0d_%s" % (task_id, task_name)

    out_base = join(tuFramework_raw_data, foldername)
    imagestr = join(out_base, "imagesTr")
    imagests = join(out_base, "imagesTs")
    labelstr = join(out_base, "labelsTr")
    if not os.path.isdir(imagestr):
        os.makedirs(imagestr)
    if not os.path.isdir(imagests):
        os.makedirs(imagests)
    if not os.path.isdir(labelstr):
        os.makedirs(labelstr)

    train_patient_names = []
    test_patient_names = []
    all_cases = subfolders(base, join=False)

    train_patients = all_cases[:]
    test_patients = all_cases[:]

    for p in train_patients:
        curr = join(base, p)
        label_file = join(curr, "segmentation.nii.gz")
        image_file = join(curr, "imaging.nii.gz")
        shutil.copy(image_file, join(imagestr, p + "_0000.nii.gz"))
        shutil.copy(label_file, join(labelstr, p + ".nii.gz"))
        train_patient_names.append(p)

    for p in test_patients:
        curr = join(base, p)
        image_file = join(curr, "imaging.nii.gz")
        shutil.copy(image_file, join(imagests, p + "_0000.nii.gz"))
        test_patient_names.append(p)

    json_dict = {}
    json_dict['name'] = "Spine"
    json_dict['description'] = "Spine segmentation"
    json_dict['tensorImageSize'] = "4D"
    json_dict['reference'] = "Spine"
    json_dict['licence'] = ""
    json_dict['release'] = "0.0"
    json_dict['modality'] = {
        "0": "MR",
    }
    json_dict['labels'] = {
        "0": "Background",
        "1": "S",
        "2": "L5",
        "3": "L4",
        "4": "L3",
        "5": "L2",
        "6": "L1",
        "7": "T12",
        "8": "T11",
        "9": "T10",
        "10": "T9",
        "11": "L5 / S",
        "12": "L4 / L5",
        "13": "L3 / L4",
        "14": "L2 / L3",
        "15": "L1 / L2",
        "16": "T12 / L1",
        "17": "T11 / T12",
        "18": "T10 / T11",
        "19": "T9 / T10"

    }

    json_dict['numTraining'] = len(train_patient_names)
    json_dict['numTest'] = len(test_patient_names)
    json_dict['training'] = [{'image': "./imagesTr/%s.nii.gz" % i.split("/")[-1], "label": "./labelsTr/%s.nii.gz" % i.split("/")[-1]} for i in
                             train_patient_names]
    json_dict['test'] = ["./imagesTs/%s.nii.gz" % i.split("/")[-1] for i in test_patient_names]

    save_json(json_dict, os.path.join(out_base, "dataset.json"))
