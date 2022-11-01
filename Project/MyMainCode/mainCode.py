#region ENVIRONMENT SETTINGS
from Directories import Directories
from InputFileAndCommandFiles import Create
from Postprocessing import Postprocess
from Plotting import plottingPhase1Results
from Plotting import plottingPhase2Results
#endregion 

#region CREATE DIRECTORIES
directories = Directories()
directories.createDirectories(1)
#endregion

#region CREATE INPUT AND COMMAND FILES
files = Create ()
files.createInputFiles(1)
#files.createPhase2InputFiles()
#files.createCaseStudyInputFiles()
#files.createLsdynaCommandFile(1)
#files.createLsdynaPhase2CommandFile()
#files.createLsdynaCaseStudyCommandFile()
#files.createLsPrePostCommandFile(1)
#files.createLsPrePostPhase2CommandFile()
#endregion

#region POSTPROCESSING
#postprocess = Postprocess ()
#postprocess.runLsprepostPhase1()
#postprocess.collectDataPhase1()
#postprocess.runLsprepostPhase2()
#postprocess.collectDataPhase2()
#endregion

#region PLOTTING
#plots = plottingPhase2Results ()
#plots.readingPhase2Results()
#plots.analyzingPhase2Results()
#plots.contactForce()
#plots.interactionDiagram()
#plots.plottingPhase1Results().displacement()
#plots.plottingPhase1Results().velocity()
#plots.plottingPhase1Results().lengthEffects()
#plots.plottingPhase1Results().energy()
#plots.annotate()
#plots.pieChart()
#plots.Acceleration()
#endregion


