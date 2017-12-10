import arcpy

arcpy.ImportToolbox('test.pyt')
result = arcpy.slaptest.SlapTest('slap_test.gdb/points')
result.saveToFile('test.rlt')

