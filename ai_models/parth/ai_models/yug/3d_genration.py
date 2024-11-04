# 3d_generation.py
import open3d as o3d

class MeshGenerator:
    def __init__(self):
        pass
    
    def generate_3d_model(self):
        # Create a simple 3D sphere model as an example
        mesh = o3d.geometry.TriangleMesh.create_sphere(radius=1.0)
        mesh.compute_vertex_normals()
        return mesh
