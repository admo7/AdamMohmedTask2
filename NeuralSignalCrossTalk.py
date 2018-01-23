#import SciPy as DontUseThis
import time
import random
random.seed(1) #Setting random number generator seed for repeatability

NUM_NEURONS = 5000 #Start with a small no for testing, use original 10000 later
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

neuron_positions = [[gen_coord(), gen_coord()] for i in xrange(NUM_NEURONS)] #This gives the coords of each neuron in a 2D list

#print neuron_positions

start = time.time() #set start time of code

k = 1 #need a second counter to shift the comparison neurons start point across by 1 to avoid overlap with the base neuron when restarting the loop
	  #see later in the code for how it is used

conflict = [] #list of which elements in neuron_positions are causing a conflict

for i in neuron_positions: #iterate over neuron_positions to set the base neuron from which to calculate radius to other neurons

	for j in range(k, NUM_NEURONS): #selects neurons from 1 after the base neuron to the end of the neuron_positions list to compare with the base neuron
								    #using 'k' as explained above
								
		base_neuron_x = i[0] #the base neuron (x-coord),which starts from the 1st neuron and then moves to the next neuron each loop
		
		compare_neuron_x = neuron_positions[j][0] #the comparison neuron (x-coord), which starts from after the base neuron until the last neuron
		
		base_neuron_y = i[1] 
		compare_neuron_y = neuron_positions[j][1]
		
		x = abs(compare_neuron_x - base_neuron_x) #calculate difference in x values between the two selected neurons
												  #need abs() to use the absolute value when calculating the radius
												  
		y = abs(compare_neuron_y - base_neuron_y) #calculate difference in y values between the two selected neurons
		
		radius = ((x ** 2) + (y ** 2)) ** 0.5 #calculate the radius between the base neuron and the comparison neuron
		
		if radius < 500: 
		
			conflict.append(k-1) #appends the base neuron's position in the neuron_positions list to the conflict list
			
			conflict.append(k) #appends the comparison neuron's position in the neuron_positions list to the conflict list
			
	k += 1
	
#print conflict 

#print len(conflict) #gives the total number of neurons which are in a conflicted state

conflict = set(conflict) #removes any repeated neurons, as we already know they are in a conflicted state if they already appear in the list

#print conflict

print len(conflict)

print time.time()-start #shows time taken for code to run
