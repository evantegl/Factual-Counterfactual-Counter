#!/usr/bin/python

from numpy import *
from pylab import *
from matplotlib import rc, rcParams

rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Droid Sans']})

# Read in data from an ASCII data table
data = genfromtxt('plotting_data')

#'data' is a matrix containing the columns and rows from the file
mass   = data[:,0]  # Python indices are (row,col) as in linalg
radius = data[:,1]  # Creates arrays for first two columns

print mass
print radius

# Create a loglog plot of data
loglog(mass,radius)
xlabel(r'Mass ($M_{\odot}$)')
ylabel(r'Radius ($R_{\odot}$)')

# Turn on a grid
grid(True)

# Save the figure in a separate file
savefig('read_and_plot_data.png')

# Draw the plot to the screen
show()