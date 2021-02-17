# state file generated using paraview version 5.9.0-RC1

#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------
abs_path = os.path.dirname(os.path.abspath(__file__))
# get the material library
materialLibrary1 = GetMaterialLibrary()
materialLibrary1.LoadMaterials = abs_path+'\\Materials\\ospray_mats.json'

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1490, 548]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [-0.0452331391404632, -0.015172871780395503, 0.0027427635192870947]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.927494869825412, 0.26502581200173375, -0.4517170799964505]
renderView1.CameraFocalPoint = [-0.0452331391404632, -0.015172871780395513, 0.0027427635192870904]
renderView1.CameraViewUp = [-0.24624240271844555, 0.9667494481118903, 0.06899408437541969]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.6156160329983007
renderView1.EnableRayTracing = 1
renderView1.BackEnd = 'OSPRay pathtracer'
renderView1.Shadows = 1
renderView1.SamplesPerPixel = 128
renderView1.VolumeAnisotropy = 1.0
renderView1.ProgressivePasses = 10
renderView1.RouletteDepth = 10
renderView1.LightScale = 10.0
renderView1.Backgroundmode = 'Both'
renderView1.EnvironmentalBG = [0.0, 0.0, 0.0]
renderView1.EnvironmentalBG2 = [0.0, 0.0, 0.0]
renderView1.Background = [0.0, 0.0, 0.0]
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
#layout1 = CreateLayout(name='Layout #1')
#layout1.AssignView(0, renderView1)
#layout1.SetSize(1490, 548)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'STL Reader'
full_Stellaratorstl = STLReader(registrationName='Full_Stellarator.stl', FileNames=[abs_path+'\\SceneObjects\\SCR-1 20121107 - COMPLETE.stl'])

# create a new 'Clip'
half_Stellarator = Clip(registrationName='Half_Stellarator', Input=full_Stellaratorstl)
half_Stellarator.ClipType = 'Plane'
half_Stellarator.HyperTreeGridClipper = 'Plane'
half_Stellarator.Scalars = ['POINTS', '']

# init the 'Plane' selected for 'ClipType'
half_Stellarator.ClipType.Origin = [-1.8587150573730469, 6.402712821960449, -14.561095237731934]

# init the 'Plane' selected for 'HyperTreeGridClipper'
half_Stellarator.HyperTreeGridClipper.Origin = [-1.8587150573730469, 6.402712821960449, -14.561095237731934]

# create a new 'PLY Reader'
plasma_volply = PLYReader(registrationName='plasmaSurface.ply', FileNames=['${PLASMA_OBJ_PATH}'])

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from plasma_volply
plasma_volplyDisplay = Show(plasma_volply, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plasma_volplyDisplay.Representation = 'Surface'
plasma_volplyDisplay.AmbientColor = [0.0, 0.3333333333333333, 1.0]
plasma_volplyDisplay.ColorArrayName = ['POINTS', '']
plasma_volplyDisplay.DiffuseColor = [0.0, 0.3333333333333333, 1.0]
plasma_volplyDisplay.MapScalars = 0
plasma_volplyDisplay.InterpolateScalarsBeforeMapping = 0
plasma_volplyDisplay.Opacity = 0.1
plasma_volplyDisplay.SpecularPower = 0.0
plasma_volplyDisplay.Luminosity = 0.0
plasma_volplyDisplay.Diffuse = 0.4
plasma_volplyDisplay.Roughness = 0.0
plasma_volplyDisplay.EdgeTint = [0.0, 0.3333333333333333, 1.0]
plasma_volplyDisplay.SelectTCoordArray = 'None'
plasma_volplyDisplay.SelectNormalArray = 'Normals'
plasma_volplyDisplay.SelectTangentArray = 'None'
plasma_volplyDisplay.RepeatTextures = 0
plasma_volplyDisplay.EdgeColor = [1.0, 1.0, 1.0]
plasma_volplyDisplay.Orientation = [0.0, 0.1, 0.0]
plasma_volplyDisplay.Origin = [0.0, 2.0, 0.0]
plasma_volplyDisplay.OSPRayUseScaleArray = 'All Exact'
plasma_volplyDisplay.OSPRayScaleArray = 'Normals'
plasma_volplyDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
plasma_volplyDisplay.SelectOrientationVectors = 'None'
plasma_volplyDisplay.ScaleFactor = 0.05931179821491242
plasma_volplyDisplay.SelectScaleArray = 'None'
plasma_volplyDisplay.GlyphType = 'Arrow'
plasma_volplyDisplay.GlyphTableIndexArray = 'None'
plasma_volplyDisplay.GaussianRadius = 0.0029655899107456207
plasma_volplyDisplay.SetScaleArray = ['POINTS', 'Normals']
plasma_volplyDisplay.ScaleTransferFunction = 'PiecewiseFunction'
plasma_volplyDisplay.OpacityArray = ['POINTS', 'Normals']
plasma_volplyDisplay.OpacityTransferFunction = 'PiecewiseFunction'
plasma_volplyDisplay.DataAxesGrid = 'GridAxesRepresentation'
plasma_volplyDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
plasma_volplyDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.44475141167640686, 0.938144326210022, 0.5, 0.0, 0.9475138783454895, 0.06185567006468773, 0.5, 0.0, 1.0, 0.0824742317199707, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plasma_volplyDisplay.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plasma_volplyDisplay.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
plasma_volplyDisplay.PolarAxes.Orientation = [0.0, 0.1, 0.0]

# show data from half_Stellarator
half_StellaratorDisplay = Show(half_Stellarator, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
half_StellaratorDisplay.Representation = 'Surface'
half_StellaratorDisplay.AmbientColor = [0.6039215686274509, 0.6039215686274509, 0.6039215686274509]
half_StellaratorDisplay.ColorArrayName = [None, '']
half_StellaratorDisplay.DiffuseColor = [0.6039215686274509, 0.6039215686274509, 0.6039215686274509]
half_StellaratorDisplay.Specular = 0.17
half_StellaratorDisplay.SelectTCoordArray = 'None'
half_StellaratorDisplay.SelectNormalArray = 'None'
half_StellaratorDisplay.SelectTangentArray = 'None'
half_StellaratorDisplay.Scale = [0.01, 0.01, 0.01]
half_StellaratorDisplay.Origin = [0.08, -0.08, 0.15]
half_StellaratorDisplay.OSPRayUseScaleArray = 'All Exact'
half_StellaratorDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
half_StellaratorDisplay.OSPRayMaterial = 'Metal_Titanium_cast'
half_StellaratorDisplay.SelectOrientationVectors = 'None'
half_StellaratorDisplay.ScaleFactor = 9.29299430847168
half_StellaratorDisplay.SelectScaleArray = 'None'
half_StellaratorDisplay.GlyphType = 'Arrow'
half_StellaratorDisplay.GlyphTableIndexArray = 'None'
half_StellaratorDisplay.GaussianRadius = 0.464649715423584
half_StellaratorDisplay.SetScaleArray = [None, '']
half_StellaratorDisplay.ScaleTransferFunction = 'PiecewiseFunction'
half_StellaratorDisplay.OpacityArray = [None, '']
half_StellaratorDisplay.OpacityTransferFunction = 'PiecewiseFunction'
half_StellaratorDisplay.DataAxesGrid = 'GridAxesRepresentation'
half_StellaratorDisplay.PolarAxes = 'PolarAxesRepresentation'
half_StellaratorDisplay.ScalarOpacityUnitDistance = 1.180113630994298
half_StellaratorDisplay.OpacityArrayName = [None, '']

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
half_StellaratorDisplay.PolarAxes.Scale = [0.01, 0.01, 0.01]

# ----------------------------------------------------------------
# restore active source
SetActiveSource(plasma_volply)
# ----------------------------------------------------------------
#First shot
myview = GetActiveView()

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection3.png", myview,
        ImageResolution=[1442, 794],
        OverrideColorPalette="Black Background")

renderView1.CameraPosition = [0.8323841860299734, 0.6627173102524578, -0.03675367334754709]
renderView1.CameraFocalPoint = [-0.04436423774158871, -0.016654970694077606, -0.004967882750537885]
renderView1.CameraViewUp = [-0.6099962080596103, 0.790064001009236, 0.060856392122559444]

myview = GetActiveView()

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection4.png", myview,
        ImageResolution=[1442, 794],
        OverrideColorPalette="Black Background")

renderView1.CameraPosition = [-0.0452331391404632, 1.3274609417900813, 0.0027427635192870947]
renderView1.CameraFocalPoint = [-0.0452331391404632, -0.015172871780395503, 0.0027427635192870947]
renderView1.CameraViewUp = [-1.0, 0.0, 0.0]

myview = GetActiveView()

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection4.png", myview,
        ImageResolution=[1442, 794],
        OverrideColorPalette="Black Background")

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')