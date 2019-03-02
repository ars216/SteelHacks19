def drawBox(vertices):

	import matplotlib.pyplot as pyplot
	import matplotlib.patches as patches
	import numpy as np
	from PIL import Image

	w = 450
	h = 100
	x = vertices[0]
	y = vertices[1]

	def boxDraw(imageFile):

		img = np.array(Image.open(imageFile),dtype=np.uint8)

		fig,ax = pyplot.subplots(1)

		ax.imshow(img)

		rectangle = patches.Rectangle((x + w, y + h),150,h,linewidth=1,edgecolor='r',facecolor='none')

		ax.add_patch(rectangle)

		pyplot.show()

	boxDraw('powerPlant.jpeg')
