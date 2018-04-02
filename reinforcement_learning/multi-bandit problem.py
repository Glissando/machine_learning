import math
import numpy as np
import scipy as sp
import random

NUM_OF_SLOTS = 3
values = np.array()

#Value function(s)
#i: the element to add the reward to
#r: the reward for performing the action
def sum(i,r):
	values[i] = values[i] + r

#alpha: learning rate
#r: the reward for performing the action
#v[i]: the current estimate reward for performing that action
def nudge(i,r,alpha):
	values[i] = values[i] + alpha*(r-values[i])

#Exploitation/Search function(s)
def prob():
	values = values/np.linalg.norm(values)
	index = np.random.ranf();
	v = 0
	
	for i in range(values):
		if index > v and index <= v + values[i]:
			return i
	
		v = v + values[i]
	
	return -1

def uncertainty():
	for i in range(values):
		values[i] = float("inf")
	
	return best(values)

def noise():
	#TODO: Calculate noise with linear regression?
	pass

def best(a):
	var best = float("-inf")
	index = 0
	
	for i in range(a):
		if a[i] > best:
			best = a[i]
			index = i
	
	return index