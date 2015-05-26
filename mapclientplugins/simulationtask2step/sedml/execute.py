from string import Template
from subprocess import call
import numpy as np

class ExecuteSedml():
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
	
	self.simulationDataRoot = u"/home/abi/projects/simulation-data"
	self.template = self.simulationDataRoot + u"/sed-ml-templates/euler-with-sine-model.xml"

    def execute(self, stepSize):
	'''
	http://stackoverflow.com/questions/6385686/python-technique-or-simple-templating-system-for-plain-text-output
	'''

	# Create our SED-ML file from the template with the given step size
	#open the file
	filein = open( self.template )
	#read it
	src = Template( filein.read() )
	#document data
	d={ 'MAX_STEP_SIZE':stepSize }
	#do the substitution
	result = src.substitute(d)
	tmpFile = "/tmp/andre-tmp-sedml.xml"
	fileout = open( tmpFile, "w" )
	fileout.write(result)
	fileout.flush()
	
	# execute the simulation experiment
	resultsFile = "/tmp/andre-sed-ml-results.csv"
	returnCode = call(["/home/abi/projects/simulation-data/bin/get-sed-ml-client", tmpFile, resultsFile])
	if returnCode != 0:
		return None
	data = np.genfromtxt(resultsFile, dtype=float, delimiter=',', names=True)
	return data 
