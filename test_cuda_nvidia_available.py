import os
import torch

# Set CUDA_VISIBLE_DEVICES to enable specific GPUs
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # Set to the ID of your GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("device: ", device)