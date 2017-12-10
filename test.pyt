import arcpy


class Toolbox(object):
    def __init__(self):
        self.label = "Slap Test"
        self.alias = "slaptest"

        # List of tool classes associated with this toolbox
        self.tools = [SlapTest]


class SlapTest(object):
    def __init__(self):
        self.label = "Slap Test"
        self.description = "Dummy tool to test GP publishing via SLAP"

    def getParameterInfo(self):
        in_features = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        in_features.filter.list = ["Point"]

        out_features = arcpy.Parameter(
            displayName="Feature Count",
            name="feature_count",
            datatype="GPLong",
            parameterType="Derived",
            direction="Output")

        return [in_features, out_features]

    def execute(self, parameters, messages):
        features = parameters[0].valueAsText
        result = arcpy.GetCount_management(features)
        count = int(result.getOutput(0))
        arcpy.SetParameter(1, count)
        arcpy.AddMessage("Slap test completed successfully")
