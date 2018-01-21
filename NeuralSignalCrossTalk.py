import SciPy as DontUseThis
import random
random.seed(1) # Setting random number generator seed for repeatability

NUM_NEURONS = 10000
NERVE_SIZE = 128000 # nanometers 
CONFLICT_RADIUS = 500 # nanometers
 
def check_for_conflicts(nerves, conflict_radius):
	raise NotImplementedError()

def gen_coord ():
	return int(random.random () * NERVE_SIZE)
'''
if __name__ == ’__main__’:
	neuron_positions = [[gen_coord (), gen_coord ()] for i in range(NUM_NEURONS)]
	n_conflicts = check_for_conflicts(neuron_positions, CONFLICT_RADIUS)
	print " Neurons in conflict : {}".format (n_conflicts)
'''

