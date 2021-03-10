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
# renderView1.KeyLightWarmth = 0.4
# renderView1.KeyLightIntensity = 1.0
# renderView1.FillLightWarmth = 0.6
# renderView1.FillLightKFRatio = 23.5
# renderView1.FillLightElevation = 90.0
# renderView1.BackLightWarmth = 0.6
# renderView1.BackLightKBRatio = 15.5
# renderView1.BackLightElevation = -90.0
# renderView1.HeadLightWarmth = 0.7
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
renderView1.LightScale = 5.0
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
plasma_volply = PLYReader(registrationName='plasma_surface.ply', FileNames=['${PLASMA_OBJ_PATH}'])

# create a new 'STL Reader'
bobinascompletasstl = STLReader(registrationName='bobinas completas.stl', FileNames=[abs_path+'\\SceneObjects\\bobinas_completas.stl'])


# create a new 'Clip'
clip3 = Clip(registrationName='Clip3', Input=bobinascompletasstl)
clip3.ClipType = 'Plane'
clip3.HyperTreeGridClipper = 'Plane'
clip3.Scalars = ['CELLS', 'STLSolidLabeling']

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [0.0015497207641601562, 0.0, -2.002716064453125e-05]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip3.HyperTreeGridClipper.Origin = [0.0015497207641601562, 0.0, -2.002716064453125e-05]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from plasma_volply
plasma_volplyDisplay = Show(plasma_volply, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plasma_volplyDisplay.Representation = 'Surface'
plasma_volplyDisplay.AmbientColor = [0.9176470588235294, 0.45098039215686275, 1.0]
plasma_volplyDisplay.ColorArrayName = [None, '']
plasma_volplyDisplay.DiffuseColor = [0.9176470588235294, 0.45098039215686275, 1.0]
plasma_volplyDisplay.Opacity = 0.05
plasma_volplyDisplay.Specular = 1.0
plasma_volplyDisplay.SpecularPower = 0.0
plasma_volplyDisplay.Luminosity = 0.0
plasma_volplyDisplay.Diffuse = 0.4
plasma_volplyDisplay.Roughness = 0.0
plasma_volplyDisplay.SelectTCoordArray = 'None'
plasma_volplyDisplay.SelectNormalArray = 'None'
plasma_volplyDisplay.SelectTangentArray = 'None'
plasma_volplyDisplay.RepeatTextures = 0
plasma_volplyDisplay.EdgeColor = [1.0, 1.0, 1.0]
plasma_volplyDisplay.Orientation = [90.0, 0.0, 0.0]
plasma_volplyDisplay.OSPRayUseScaleArray = 'All Exact'
plasma_volplyDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
plasma_volplyDisplay.SelectOrientationVectors = 'None'
plasma_volplyDisplay.ScaleFactor = 0.05931179821491242
plasma_volplyDisplay.SelectScaleArray = 'None'
plasma_volplyDisplay.GlyphType = 'Arrow'
plasma_volplyDisplay.GlyphTableIndexArray = 'None'
plasma_volplyDisplay.GaussianRadius = 0.0029655899107456207
plasma_volplyDisplay.SetScaleArray = [None, '']
plasma_volplyDisplay.ScaleTransferFunction = 'PiecewiseFunction'
plasma_volplyDisplay.OpacityArray = [None, '']
plasma_volplyDisplay.OpacityTransferFunction = 'PiecewiseFunction'
plasma_volplyDisplay.DataAxesGrid = 'GridAxesRepresentation'
plasma_volplyDisplay.PolarAxes = 'PolarAxesRepresentation'



# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
plasma_volplyDisplay.PolarAxes.Orientation = [90.0, 0.0, 0.0]

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
half_StellaratorDisplay.OSPRayMaterial = 'Metal_Aluminium_normal'
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

# show data from clip3
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.AmbientColor = [0.0, 0.0, 0.0]
clip3Display.ColorArrayName = ['POINTS', '']
clip3Display.DiffuseColor = [0.0, 0.0, 0.0]
clip3Display.SelectTCoordArray = 'None'
clip3Display.SelectNormalArray = 'None'
clip3Display.SelectTangentArray = 'None'
clip3Display.Position = [0.0, 0.0, 0.01]
clip3Display.Scale = [0.023, 0.023, 0.023]
clip3Display.Orientation = [90.0, 0.0, 0.0]
clip3Display.Origin = [0.06, 0.0, -0.0]
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.SelectOrientationVectors = 'None'
clip3Display.ScaleFactor = 3.668600082397461
clip3Display.SelectScaleArray = 'STLSolidLabeling'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'STLSolidLabeling'
clip3Display.GaussianRadius = 0.18343000411987306
clip3Display.SetScaleArray = [None, '']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = [None, '']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityUnitDistance = 2.525444527899339
clip3Display.OpacityArrayName = ['CELLS', 'STLSolidLabeling']

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip3Display.PolarAxes.Translation = [0.0, 0.0, 0.01]
clip3Display.PolarAxes.Scale = [0.023, 0.023, 0.023]
clip3Display.PolarAxes.Orientation = [90.0, 0.0, 0.0]


# ----------------------------------------------------------------
# restore active source
SetActiveSource(plasma_volply)
# ----------------------------------------------------------------
#First shot
myview = GetActiveView()

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection1.png", myview,
        ImageResolution=[1442, 794])

renderView1.CameraPosition = [0.8323841860299734, 0.6627173102524578, -0.03675367334754709]
renderView1.CameraFocalPoint = [-0.04436423774158871, -0.016654970694077606, -0.004967882750537885]
renderView1.CameraViewUp = [-0.6099962080596103, 0.790064001009236, 0.060856392122559444]

myview = GetActiveView()

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection2.png", myview,
        ImageResolution=[1442, 794])

renderView1.CameraPosition = [-0.0452331391404632, 1.3274609417900813, 0.0027427635192870947]
renderView1.CameraFocalPoint = [-0.0452331391404632, -0.015172871780395503, 0.0027427635192870947]
renderView1.CameraViewUp = [-1.0, 0.0, 0.0]

myview = GetActiveView()

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection3.png", myview,
        ImageResolution=[1442, 794])

renderView1.CameraPosition = [0.19285958547888687, 0.08998402239704861, 1.0815664184341647]
renderView1.CameraFocalPoint = [-0.015632001883241695, -0.024281410898118225, -0.0020373800216847656]
renderView1.CameraViewUp = [-0.020491472618068194, 0.9946808676899923, -0.10094588154762511]

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection4.png", myview,
        ImageResolution=[1442, 794])


renderView1.CameraPosition = [0.6239006219564823, -0.6088086175090884, 1.0053649463453112]
renderView1.CameraFocalPoint = [-0.012662655021393921, 0.035696470396429474, 0.01475844909536612]
renderView1.CameraViewUp = [0.20260194573888096, 0.8752242755986549, 0.4392435759184524]

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection5.png", myview,
        ImageResolution=[1442, 794])

renderView1.CameraPosition = [0.8274378904353794, -0.701595334079012, 0.009496008616149885]
renderView1.CameraFocalPoint = [-0.013174196353669364, 0.022261802504156433, -0.0016703979964895616]
renderView1.CameraViewUp = [0.6524624907429314, 0.7577962738568949, 0.006124173588020346]

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection6.png", myview,
        ImageResolution=[1442, 794])

renderView1.CameraPosition = [-0.04546808757781984, -0.015172871780395503, -1.1066365779482135]
renderView1.CameraFocalPoint = [-0.04546808757781984, -0.015172871780395503, 0.0027427635192870947]

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection7.png", myview,
        ImageResolution=[1442, 794])

Hide(half_Stellarator , renderView1)


renderView1.CameraPosition = [0.8577723812508664, 0.6237187831353067, -0.09541958610278709]
renderView1.CameraFocalPoint = [-0.03910136698851027, -0.01132244864609315, 0.05644429021898878]
renderView1.CameraViewUp = [-0.5848248163641906, 0.8074686282651369, -0.0772939100590022]

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection8.png", myview,
        ImageResolution=[1442, 794])

renderView1.CameraPosition = [-0.03820588473193964, 0.14172988338798861, -0.900545025088518]
renderView1.CameraFocalPoint = [-0.04546808757781984, -0.015172871780395504, 0.0027427635192870934]
renderView1.CameraViewUp = [-0.00013624183082216283, 0.9852470355915852, 0.17113813220950197]

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection9.png", myview,
        ImageResolution=[1442, 794])

Hide(clip3 , renderView1)

renderView1.CameraPosition = [0.8577723812508664, 0.6237187831353067, -0.09541958610278709]
renderView1.CameraFocalPoint = [-0.03910136698851027, -0.01132244864609315, 0.05644429021898878]
renderView1.CameraViewUp = [-0.5848248163641906, 0.8074686282651369, -0.0772939100590022]

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection10.png", myview,
        ImageResolution=[1442, 794])

renderView1.CameraPosition = [0.7134326114793852, 0.10315872607600166, 0.11261315400630009]
renderView1.CameraFocalPoint = [-8.001923561096191e-06, 1.0499730706214905e-05, -4.917383193969727e-07]
renderView1.CameraViewUp = [-0.13939747388174084, 0.9899546992427694, -0.02362282206993334]

SaveScreenshot(abs_path+"\\OutputFiles\\ImageCollection11.png", myview,
        ImageResolution=[1442, 794])

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')