"""
inference.py

DEMO inference script for VESSL. This script is used to run inference on a single image or a directory of images.
this demo is only for Medical X-VL dataset and models.
"""

medical_x_vl = __import__("Medical_X-VL")
import torch

# detection
medical_x_vl_detection_model = torch.load("medical_x_vl_detection_model.pth")
medical_x_vl_detection_model(test_input1, test_input2, test_input3)

# generation
medical_x_vl_generation_model = torch.load("medical_x_vl_generation_model.pth")
medical_x_vl_generation_model(test_input1, test_input2, test_input3)

# vqa
medical_x_vl_vqa_model = torch.load("medical_x_vl_vqa_model.pth")
medical_x_vl_vqa_model(test_input1, test_input2, test_input3)

# finetune_correction
medical_x_vl_finetune_correction_model = torch.load("medical_x_vl_finetune_correction_model.pth")
medical_x_vl_finetune_correction_model(test_input1, test_input2, test_input3)