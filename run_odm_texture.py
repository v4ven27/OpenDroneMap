#!/usr/bin/python

import sys
import os
import subprocess as sp

def help():
	print 'ABOUT: This script is used to run the odm_texturing', \
	'and odm_georeferencing modules independently'
	print 'USAGE: ./run_odm_texture.py <inputMeshPLYFile> <bundleFile> <resizedImagesPath> <imagesListFile> <outputDirectory>'
	return;

if len(sys.argv) < 6:
	print 'ERROR: Insufficient number of arguments provided'
	help()
	
inputFile=sys.argv[1] 			# Input mesh file in PLY format
bundleFile=sys.argv[2] 			# Bundle file containing camera poses in the same order as the images in imageList 
resizedImagePath=sys.argv[3] 	# Path to the image_resized folder in the odm project directory
imagesListFile=sys.argv[4] 		# Contains a list of only image filenames
outputDirectory=sys.argv[5]		# Path to output directory
#coordsFile=sys.argv[6]

sp.call(['mkdir' , outputDirectory])

odmBinariesPath="/home/venkat/Libraries/ODM/OpenDroneMap/build/bin/"
odmTexturing=odmBinariesPath+"odm_texturing"
odmGeoreferencing=odmBinariesPath+"odm_georef"

#Run ODM texturing module with arguments provided
sp.call([odmTexturing, "-inputModelPath", inputFile, "-bundleFile", bundleFile, "-imagesPath", resizedImagePath, "-imagesListPath", imagesListFile, "-outputFolder", outputDirectory+"/", "-bundleResizedTo", "2400"])
inputTexturedMesh=outputDirectory+"/odm_textured_model.obj"
print ('Finished writing textured mesh to %s' % inputTexturedMesh)

#Run ODM georeferencing module with arguments
#sp.call([odmGeoreferencing, "-inputFile", inputTexturedMesh, "-bundleFile", bundleFile, "-inputCoordFile", coordsFile])
