from string import Template
from subprocess import call
import numpy as np
from timeit import timeit

class ExecuteSedml():
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
	
	self.simulationDataRoot = u"/home/abi/projects/simulation-data"
	self.template = self.simulationDataRoot + u"/sed-ml-templates/ICC-model-simulation.xml"

    def execute(self, stepSize, methodId):
	'''
	http://stackoverflow.com/questions/6385686/python-technique-or-simple-templating-system-for-plain-text-output
	'''

	# Create our SED-ML file from the template with the given step size
	#open the file
	filein = open( self.template )
	#read it
	src = Template( filein.read() )
	#document data
	d={ 'MAX_STEP_SIZE':stepSize, 'INTEGRATION_METHOD':methodId }
	#do the substitution
	result = src.substitute(d)
	tmpFile = "/tmp/andre-tmp-sedml.xml"
	fileout = open( tmpFile, "w" )
	fileout.write(result)
	fileout.flush()
	
	# execute the simulation experiment
	resultsFile = "/tmp/andre-sed-ml-results.csv"
	exeFile = "/home/abi/projects/simulation-data/bin/get-sed-ml-client"
	call_args = "['%s','%s','%s']" % (exeFile, tmpFile, resultsFile)
	timeTaken = timeit(stmt="returnCode = subprocess.call(%s)" % call_args, setup="import subprocess", number=1)
	# FIXME: get return code back?
	#if returnCode != 0:
	#	return None
	data = np.genfromtxt(resultsFile, dtype=float, delimiter=',', names=True)
	r = {'time': timeTaken, 'data': data}
	return r 
