import arcpy
import os

arcpy.ImportToolbox('test.pyt')
dataset = os.path.normpath(os.path.join(os.getcwd(), 'slap_test.gdb')
result = arcpy.slaptest.SlapTest('slap_test.gdb/points')
result.saveToFile('test.rlt')

