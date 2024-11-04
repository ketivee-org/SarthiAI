# image_generation.py
import torch
from torchvision import transforms
from torchvision.models import resnet18

class ImageGenerator:
    def __init__(self, model_path):
        self.model = torch.load(model_path)
        self.transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor()
        ])

    def generate_image(self, input_vector):
        with torch.no_grad():
            generated_image = self.model(input_vector)
        return generated_image
