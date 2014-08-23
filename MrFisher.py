#!/usr/bin/env python
from __future__ import division
import sys
import cmd

class MrFisher( cmd.Cmd ):
	def do_version( self, e ):
		print "Mr.Fisher version 0.01"
		
	def do_run( self, e ):
		print "This runs the HPC vector frame ..."
		
	def help_version( self ):
		print "Shows version information"
		
	def do_quit( self, e ):
		sys.exit( 0 )


def notice():
	print """\
--------------------------------------------------------------------------------
Mr. Fisher is an innovative software application to help you learn statistics.
It is provided under the terms of the General Public License version 3 (GPLv3)
Copyright 2013 Paul K. Korir

Mr. Fisher

If you use Mr. Fisher please cite:
Korir, P.K. (2013) "Mr. Fisher: Learning Statistics Intuitively"
Journal of Statistical Education, pages. 
--------------------------------------------------------------------------------	
"""

if __name__ == '__main__':
		mrfisher = MrFisher()
		
		# set interpreter parameters
		mrfisher.prompt = "fish> "
		mrfisher.intro = notice()
		
		mrfisher.cmdloop()
