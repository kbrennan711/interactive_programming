"""
Kelly Brennan and Celine Ta
Software Design Spring 2015
Interactive Visualization Project

We aim to create an interactive map that displays each countries' happiness rating and GDP
"""
import bokeh.plotting as bk
import numpy as np
from bokeh.models import HoverTool as hov
import pandas as pd

class Display_Map():
	"""
	Takes in map image, array of defining coordinates for each country, and list of countries. Upon a mouse action, Display_Map will
	look up location of mouse action in relation to map and update display accordingly.
	"""
	#def __init__(self,image, borders, list_countries):
	def __init__(self):
		"""
		Initializes map image, borders, countries
		"""
		#for now, data is not related to geography
		stats = pd.read_csv('data/juvie_breakdown.csv')
		self.gender = stats['Sex'].Series.toList() #you can also use df['column_name']
		print type(self.gender)
		self.year = stats['Year'].Series.toList
		#self.juvRate=[]
		#for rate in stats['Rate per 100,000']:
		#	if not np.isnan(rate):
		#		self.juvRate.extend(int(rate))


		df = pd.read_csv('GDP_per_state.csv', names = ['State', 'GDP'])
		state_GDP = dict(zip(df.State, df.GDP))


	def lookup_country(self,hover_pos):
		"""Given position, finds Country object
			returns: country (Country object)
		"""
		pass
	def update(self,hover_pos):
		"""
		Updates map display upon mouse action
		"""
		pass
	def run_display(self):
		"""
		Maintains display/ interaction experience
		"""
		bk.output_file("Map_bk.html", title="Hello World!")  # save plot as html
		xs = [0,1,2,3,4,5]
		ys = [x**2 for x in xs]
		fig = bk.figure(plot_width = 600, plot_height= 600, title = "Map") #creates new Bokeh plot
		fig.circle(#self.gender, self.year,
         #size=(self.juvRate), # px
         xs, ys,
         size =2,
         fill_alpha=0.5,
         fill_color="steelblue",
         line_alpha=0.8,
         line_color="crimson")
		#fig.circle(xs,ys)


		#fig.line(xs, ys, line_width=2)
		bk.save(obj=fig)
		bk.show(fig)

class Country():
	def __init__(self,name, borders, happiness, GDP):
		"""
		Creates Country object with name, borders, mean happiness level, and GDP of a certain year
		"""
		pass
	def get_happiness(self):
		"""
		returns country's mean happiness level
		"""
		pass
	def get_GDP(self):
		"""
		returns country's GDP
		"""
		pass

class Interactive():
	def __init__(self):
		"""
		Initializes monitoring of user input
		"""
		pass
	def get_mouse_position(self):
		"""
		returns mouse position in relation to map image (translate from screen position)
		"""
		pass
if __name__ == '__main__':
	vis = Display_Map() # pass in arguments
	#mouse = Interactive() 
	vis.run_display()