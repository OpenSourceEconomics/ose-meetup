import matplotlib.pyplot as plt
import numpy as np

def barplot(first_order, tot_order):

	assert len(first_order)==len(tot_order), "inputs must have equal length"

	width = 0.8

	fig, ax = plt.subplots(figsize=(12,9))

	indices = np.arange(len(tot_order))
	plt.bar(indices, tot_order, width=width, 
	        color='#4169E1', label='Total Order', alpha=1, edgecolor = "black")
	plt.bar(indices, first_order, 
	        width=0.7*width, color='#3CB371', alpha=1, label='First Order', edgecolor = "black")

	plt.xticks(indices, 
	           ['q0', 'q1', 'q2'] )


	handles, labels = ax.get_legend_handles_labels()
	ax.legend(handles[::-1], labels[::-1], loc='upper right', edgecolor="white")
	plt.show()