"""Create Fishnet with ArcGIS 10.5.1.

To use run:
    C:/Python27/ArcGIS10.5/python.exe fishnet.py

"""

# Name: CreateFishnet.py
# Description: Creates rectangular cells

# import system module
import arcpy
from arcpy import env


# Parameters depending on configuration:
param = {
    "left": [6, 20, 46, 55],
    "right": [15, 23, 46, 55],
    "up": [6, 23, 46, 55]
}

# set workspace environment
env.workspace = r"C:\Users\Radost\Documents\Doktor\Research\ADV\georeferencing\fishnet"

# Set coordinate system of the output fishnet
env.outputCoordinateSystem = arcpy.SpatialReference(4314)

for key, value in param.items():

    outFeatureClass = "fishnet_{}.shp".format(key)

    # Set the origin of the fishnet
    originCoordinate = '{} {}'.format(str(value[0]), str(value[2]))

    # Set the orientation
    yAxisCoordinate = '{} {}'.format(str(value[0]), str(value[3]))

    # Enter 0 for width and height - these values will be calcualted by the
    # tool
    cellSizeWidth = '0'
    cellSizeHeight = '0'

    # Number of rows and columns together with origin and opposite corner
    # determine the size of each cell
    numRows = str((value[3] - value[2]) * 12)
    numColumns = str((value[1] - value[0]) * 6)

    oppositeCoorner = '{} {}'.format(str(value[1]), str(value[3]))

    # Create a point label feature class
    labels = 'NO_LABELS'

    # Extent is set by origin and opposite corner - no need to use a template
    templateExtent = '#'

    # Each output cell will be a polygon
    geometryType = 'POLYGON'

    arcpy.CreateFishnet_management(
        outFeatureClass, originCoordinate, yAxisCoordinate, cellSizeWidth,
        cellSizeHeight, numRows, numColumns, oppositeCoorner, labels,
        templateExtent, geometryType
    )
