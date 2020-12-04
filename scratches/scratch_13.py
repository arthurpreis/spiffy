import open3d
import numpy as np
import mayavi

def test_mesh():
    """A very pretty picture of spherical harmonics translated from
    the octaviz example."""
    pi = np.pi
    cos = np.cos
    sin = np.sin
    A = 40
    x = []
    y = []
    z = []
    r = 1
    for i in range(A):
        for j in range(A):
            phi = j*(2*pi/A)
            theta = i*(pi/A)
            x.append(r * sin(phi) * cos(theta))
            y.append(r * cos(phi))
            z.append( r * sin(phi) * sin(theta))
    return x, y, z


# import data
x = []
y = []
z = []
with open("./CoordenadasFMais.txt",'r') as file:
    for i, line in enumerate(file):
        if i%10 == 0:
            s = line.split()
            x.append(float(s[0]))
            y.append(float(s[1]))
            z.append(float(s[2]))

vec = np.array([x,y,z])
vec = np.transpose(vec)
pcd = open3d.geometry.PointCloud()
pcd.points = open3d.utility.Vector3dVector(vec)
print(vec.shape)

#np_points = np.array(test_mesh())
#points = np.array([np_points[0],np_points[1],np_points[2]])
#np_points = np.transpose(points)
##np_points = np.random.rand(100, 3)
##print(type(points))
##print(points.shape)
#
## From numpy to Open3D
#
#pcd.points = open3d.utility.Vector3dVector(np_points)
#print(pcd.has_normals())
pcd.estimate_normals()
#print(pcd.has_normals())
## From Open3D to numpy
##open3d.visualization.draw_geometries([pcd])
radii = [1e-6,
         1e-5,
         1e-4,
         1e-3,
         1e-2,
         1e-1,
         1e+0,
         1e+1,
         1e+2
         ]
#rec_mesh = open3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
#    pcd, open3d.utility.DoubleVector(radii))
#rec_mesh, bleh = open3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=10, width=0, scale=1.5, linear_fit=False, n_threads=- 1)
alpha = 0.03
tetra_mesh, pt_map = open3d.geometry.TetraMesh.create_from_point_cloud(pcd)
rec_mesh = open3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(
        pcd, alpha, tetra_mesh, pt_map)
#print(type(rec_mesh))
open3d.visualization.draw_geometries([pcd, rec_mesh])
#
#
#
## transform to 3d vector
## transform to point cloud
## build mesh
#
## mayavi mesh