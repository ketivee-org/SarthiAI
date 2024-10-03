# yug_main.py
from image_generation import ImageGenerator
from 3d_generation import MeshGenerator
from texture_mapping import map_texture_to_3d_model, visualize_3d_model_with_texture
import torch

def main():
    # 1. Image Generation
    image_gen = ImageGenerator("path/to/generator_model.pth")
    input_vector = torch.randn(1, 100)  # Random input to generate an image
    generated_image = image_gen.generate_image(input_vector)
    
    # 2. 3D Model Generation
    mesh_gen = MeshGenerator()
    generated_mesh = mesh_gen.generate_3d_model()
    
    # 3. Texture Mapping
    textured_mesh = map_texture_to_3d_model(generated_mesh, generated_image)
    
    # 4. Visualization
    visualize_3d_model_with_texture(textured_mesh)

if __name__ == "__main__":
    main()
