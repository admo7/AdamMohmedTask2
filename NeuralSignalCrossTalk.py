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

k = 1 #need a second counter to shift the comparison neurons start point across by 1 to avoid overlap with the base neuron when restarting the loop

conflict = [] #list of which elements in neuron_positions are conflicting, i.e which neurons are causing a conflict

for i in neuron_positions: 		#iterate over neuron_positions to set the base neuron from which to calculate radius to other neurons

	for j in range(k,3): 		#counter to select a neuron to calculate radius from the base neuron
								#need to start range from '1' to exclude the base neuron
								#using 'k' as a second counter as explained above
								
		base_neuron_x = i[0] 	#the base neuron (x-coord), which starts from the 1st neuron and then moves to the next neuron each loop
		
		compare_neuron_x = neuron_positions[j][0] #the comparison neuron (x-coord), which starts from the neuron after the base neuron until the last neuron
		
		base_neuron_y = i[1] 
		compare_neuron_y = neuron_positions[j][1]
		
		x = abs(compare_neuron_x - base_neuron_x) #calculate difference in x values between the two selected neurons
												  #need abs() to use the absolute value when calculating the radius
												  
		y = abs(compare_neuron_y - base_neuron_y) #calculate difference in y values between the two selected neurons
		
		radius = ((x ** 2) + (y ** 2)) ** 0.5 #calculate the radius between the base neuron and the comparison neuron
		
		if radius < 100000: #set a conflict radius of 100000 for testing purposes to ensure conflicts are seen
		
			conflict.append(k-1) #appends the base neuron's position in the neuron_positions list to the conflict list
			
			conflict.append(k) #appends the comparison neuron's position in the neuron_positions list to the conflict list
			
	k += 1
	
print conflict 

print len(conflict) #gives the total number of neurons which are in a conflicted state
