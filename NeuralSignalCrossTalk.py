#import SciPy as DontUseThis
import random
random.seed(1) #Setting random number generator seed for repeatability

NUM_NEURONS = 3 #Start with a small no for testing, use original 10000 later
NERVE_SIZE = 128000 #nanometers 
CONFLICT_RADIUS = 500 #nanometers
 
def check_for_conflicts(nerves, conflict_radius):
	raise NotImplementedError()

def gen_coord():
	return int(random.random() * NERVE_SIZE)
	
'''
if __name__ == '__main__':
	neuron_positions = [[gen_coord(), gen_coord()] for i in range(NUM_NEURONS)]
	n_conflicts = check_for_conflicts(neuron_positions, CONFLICT_RADIUS)
	print " Neurons in conflict :{}".format (n_conflicts)
'''

neuron_positions = [[gen_coord(), gen_coord()] for i in range(NUM_NEURONS)] #This gives the coords of each neuron in a 2D list

print neuron_positions

for i in neuron_positions: #This should just print the coords of each neuron one at a time
	print i 
	
	print i[0] #The x-coord of the current neuron
	print i[1] #The y-coord of the current neuron