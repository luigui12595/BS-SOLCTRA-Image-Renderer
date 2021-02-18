import os
import fileinput
import pymeshlab
import subprocess
import time

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
RESULTS_PATH = ABS_PATH + '\\InputFiles\\points_1023_sim'

def replace_in_file(file, order, obj_path):
   # read input file
   fin = open(file, "rt")
   # read file contents to string
   data = fin.read()
   # replace all occurrences of the required string
   if order == 0:
      data = data.replace('${PLASMA_OBJ_PATH}', obj_path)
   elif order == 1:
      data = data.replace(obj_path, '${PLASMA_OBJ_PATH}')
   # close the input file
   fin.close()
   # open the input file in write mode
   fin = open(file, "wt")
   # overrite the input file with the resulting data
   fin.write(data)
   # close the file
   fin.close()

def get_largest_file(results_dir):
   files = os.listdir(results_dir)
   largest_file_size = 0
   largest_file = ""

   print('Searching the largest file in directory')
   for file in files:
      if os.path.isfile(results_dir+'\\'+file):
         size = os.path.getsize(results_dir+'\\'+file)
         if size > largest_file_size:
            largest_file_size = size
            largest_file = results_dir+'\\'+file
   print('The largest file found is: '+largest_file)
   return largest_file


def csv_to_xyz(input_file):
   print('Converting txt file into xyz file')
   output_file = ABS_PATH + '\\InputFiles\\plasma_surface.xyz'

   with open(input_file, "r") as input:
      with open(output_file, "w") as output:
         for line in input:
            current_line = line.split(",")
            final_line = str(current_line[0]) + " " + str(current_line[1]) + " " + str(current_line[2])
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
   replace_in_file(ABS_PATH+'\\PhotoRealisticSCR.py', 0, obj_path)
   # Subprocess Paraview Call
   call_exec = 'pvpython.exe'
   file_exec = ABS_PATH+'\\PhotoRealisticSCR.py'
   try:
      subprocess.check_output([call_exec, file_exec])
   except:
      print('Error in paraview python subprocess call')
   print('Rendering done')
   replace_in_file(ABS_PATH+'\\PhotoRealisticSCR.py', 1, obj_path)

def main():
   #largest_file = get_largest_file(RESULTS_PATH)
   #xyz_file_path = csv_to_xyz(largest_file)
   #obj_path = surface_reconstruction(xyz_file_path)
   #render_images(obj_path)
   start = time.time()
   render_images(surface_reconstruction(csv_to_xyz(get_largest_file(RESULTS_PATH))))
   end = time.time()
   elapsed_time = end - start
   if elapsed_time > 59:
      print('Elapsed time: ' + str((end - start)/60) + ' minutes')
   elif elapsed_time > 3599:
      print('Elapsed time: ' + str((end - start)/3600) + ' hours')
   else:
      print('Elapsed time: '+ str(end - start) + ' seconds')

if __name__ == "__main__":
      main()



