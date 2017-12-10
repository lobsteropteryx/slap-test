import arcpy
import os

arcpy.ImportToolbox('test.pyt')
dataset = os.path.normpath(os.path.join(os.getcwd(), 'slap_test.gdb'))
result = arcpy.slaptest.SlapTest(os.path.join(dataset, 'points'))
result.saveToFile('test.rlt')

