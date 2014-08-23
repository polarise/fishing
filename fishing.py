#!/usr/bin/env python
from __future__ import division
import sys
import scipy
import scipy.stats

class Boat( object ):
	def __init__( self, name ):
		self.name = name
		self.caught_fish = None
		
class Fish( object ):
	def __init__( self, length ):
		self.length = length

class Sea( object ):
	def __init__( self, name ):
		self.name = name
		self.mean_length = None
		self.var_length = None
		self.N = None
	
	def set_population_stats( self, mean_length=5, var_length=25, N=1000 ):
		self.mean_length = mean_length
		self.var_length = var_length
		self.N = N
	
	def yield_fish( self, net ):
		# generate fish lengths according to a normal distribution
		# all lengths must be positive ergo abs( . )
		net_size = net.size
		
		fish_lengths = abs( scipy.stats.norm.rvs( loc=self.mean_length, scale=scipy.sqrt( self.var_length ), size=net_size ))

		fishes = dict()
		fish_index = 1 # use 1-based indexing
		for l in fish_lengths:
			fishes[ "Fish_%s" % fish_index ] = Fish( l )
			fish_index += 1
		
		# decrement the number of fish in the sea
		self.N -= net_size
		
		net.caught_fish = fishes	
		
		return net	

class Net( object ):
	def __init__( self, size ):
		self.size = size
		self.caught_fish = None
	
	def empty_net( self, boat ):
		boat.caught_fish = self.caught_fish
		self.caught_fish = None
		
		return boat

class FisherMan( object ):
	def __init__( self, name, net, boat, sea ):
		self.name = name
		self.net = net
		self.boat = boat
		self.sea = sea
	 
	def catch_fish( self ):
		self.net = sea.yield_fish( self.net )
		
	def empty_net( self ):
		# empty the net into the boat
		self.boat = self.net.empty_net( self.boat )
	
	def count_fish( self ):
		print "The '%s' belonging to Mr. %s has %d fishes." % ( self.boat.name, self.name, len( self.boat.caught_fish ) )
				
if __name__ == "__main__":
	# instantiate all vars
	boat = Boat( "MV Mvita" )
	sea = Sea( "Indian Ocean" )
	sea.set_population_stats() # use default parameters
	net = Net( 10 )
	fisherman = FisherMan( "Salim Bakari", net, boat, sea )
	
	# now for some actions...
	fisherman.catch_fish()
	fisherman.empty_net()
	fisherman.count_fish()
	
	# basic stats
	
