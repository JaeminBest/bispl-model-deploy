"""
inference.py

DEMO inference script for VESSL. This script is used to run inference on a single image or a directory of images.
this demo is only for Medical X-VL dataset and models.
"""

import SPMM as spmm
import torch

# pv_to_smiles
spmm_pv_to_smiles_model = torch.load("spmm_pv_to_smiles_model.pth")
spmm_pv_to_smiles_model(test_input1, test_input2, test_input3)

# smiles_to_pv
spmm_smiles_to_pv_model = torch.load("spmm_smiles_to_pv_model.pth")
spmm_smiles_to_pv_model(test_input1, test_input2, test_input3)

# prediction
spmm_prediction_model = torch.load("spmm_prediction_model.pth")
spmm_prediction_model(test_input1, test_input2, test_input3)

# retro_reaction
spmm_retro_reaction_model = torch.load("spmm_retro_reaction_model.pth")
spmm_retro_reaction_model(test_input1, test_input2, test_input3)