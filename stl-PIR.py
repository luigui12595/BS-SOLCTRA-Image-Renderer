import os
import fileinput
import pymeshlab
import subprocess

PV_PATH = 'C:\\Program Files\\ParaView 5.9.0-RC1-Windows-Python3.8-msvc2017-64bit\\bin\\pvpython.exe'
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
RESULTS_PATH = ABS_PATH + '\\InputFiles\\points_1023_sim'

def get_largest_file(results_dir):
   files = os.listdir(results_dir)
   largest_file_size = 0
   largest_file = ""

   print('Searching the largest file in directory')
   for file in files:
      if os.path.isfile(file):
         size = os.path.getsize(file)
         if size < largest_file_size:
            largest_file_size = size
            largest_file = file
   print('The largest file found is: '+largest_file)
   return largest_file


def csv_to_xyz(input_file):
   print('Converting txt file into xyz file')
   output_file = ABS_PATH + '\\InputFiles\\plasma_surface.xyz'

   with open(input_file, "r") as input:
      with open(output_file, "w") as output:
         for line in input:
            current_line = line.split(",")
            final_line = str(current_line[0]) + " " + str(current_line[1]) + " " + str(current_line[2]) + "\n"
            output.write(final_line)
   print('File created')
   return output_file


def surface_reconstruction(file):
   print('Creating surface mesh object')
   mesh_lab = pymeshlab.MeshSet()
   obj_path = ABS_PATH+'\\SceneObjects\\plasma_surface.ply'

   try:
      print("Loading a xyz point data file")
      mesh_lab.load_new_mesh(file)
      print("Computing normals for each point, 120 neighbour number")
      mesh_lab.apply_filter('compute_normals_for_point_sets', k=120)
      print("Running the surface_reconstruction algorithm Screened Poisson")
      mesh_lab.apply_filter('surface_reconstruction_screened_poisson')
      print("Saving current mesh")
      mesh_lab.save_current_mesh(obj_path)
   except pymeshlab.PyMeshLabEexception as err:
      print(err)
   print('Mesh created')
   return obj_path

def render_images(obj_path):
   print('Preparing the scene to render images')
   with fileinput.FileInput(ABS_PATH+'PhotoRealisticSCR.py', inplace=True, backup='.bak') as file:
      for line in file:
         print(line.replace('${PLASMA_OBJ_PATH}', obj_path), end='')
   # Subprocess Paraview Call
   try:
      print(subprocess.check_output(['.\\'+PV_PATH, ABS_PATH+'PhotoRealisticSCR.py']))
   except:
      print('Error in paraview python subprocess call')
   print('Rendering done')

def main():
   largest_file = get_largest_file(RESULTS_PATH)
   xyz_file_path = csv_to_xyz(largest_file)
   obj_path = surface_reconstruction(xyz_file_path)
   render_images(obj_path)

if __name__ == "__main__":
      main()



