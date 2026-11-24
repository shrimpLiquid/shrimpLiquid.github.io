a = []
b = []
c = []

ind = []
for i in range(7):
	b = []
	for j in range(6):
		c = []
		for k in range(6):
			c.append(())
		b.append(c)
	a.append(b)
	ind.append(b)
	
from os import walk
from PIL import Image
from colorutils import rgb_to_hex as rth , rgb_to_hsv

filenames = next(walk("cols"), (None, None, []))[2]
for h in range(7):
	for s in range(6):
		for v in range(6):
			im = Image.open("cols/" + filenames[h])
			cole = im.getpixel((s, 5-v))
			cole = (cole[0], cole[1], cole[2])
			a[h][s][v] = cole 
			#print("cols/" + filenames[h] + "   " + str(cole) + "	" + str((h, s, v)) + "	  " + str(a[h][s][v]))
#print(a)
hsv = rgb_to_hsv((91, 66, 110))
#print(a[int((hsv[0]/360)*7)][int(hsv[1]*5)][int(hsv[2]*5)])
cl = []
numb = 0
for h in range(7):
	for s in range(6):
		for v in range(6):
			cl.append(rth(a[h][s][v]).replace("#","0x"))
			ind[h][s][v] = numb
			numb+=1

#print(cl)




#ksjfcbdsyxjbytvweiudtv8idyvti baugdiufvȳi iguiv̄cibubcuh̄iohihiǵugÚGuḡUIgdbcukfus


colors2 = {}
def rgb_to_hsv(rgb):
	"""
	Convert an RGB color representation to an HSV color representation.

	(r, g, b) :: r -> [0, 255]
				 g -> [0, 255]
				 b -> [0, 255]

	:param rgb: A tuple of three numeric values corresponding to the red, green, and blue value.
	:return: HSV representation of the input RGB value.
	:rtype: tuple
	"""
	r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255
	_min = min(r, g, b)
	_max = max(r, g, b)
	v = _max
	delta = _max - _min

	if _max == 0:
		return 0, 0, v

	s = delta / _max

	if delta == 0:
		delta = 1

	if r == _max:
		h = 60 * (((g - b) / delta) % 6)

	elif g == _max:
		h = 60 * (((b - r) / delta) + 2)

	else:
		h = 60 * (((r - g) / delta) + 4)

	return round(h, 3), round(s, 3), round(v, 3)



colors = (((0, 1, 2, 3, 4, 5), (6, 7, 8, 9, 10, 11), (12, 13, 14, 15, 16, 17), (18, 19, 20, 21, 22, 23), (24, 25, 26, 27, 28, 29), (30, 31, 32, 33, 34, 35)), ((36, 37, 38, 39, 40, 41), (42, 43, 44, 45, 46, 47), (48, 49, 50, 51, 52, 53), (54, 55, 56, 57, 58, 59), (60, 61, 62, 63, 64, 65), (66, 67, 68, 69, 70, 71)), ((72, 73, 74, 75, 76, 77), (78, 79, 80, 81, 82, 83), (84, 85, 86, 87, 88, 89), (90, 91, 92, 93, 94, 95), (96, 97, 98, 99, 100, 101), (102, 103, 104, 105, 106, 107)), ((108, 109, 110, 111, 112, 113), (114, 115, 116, 117, 118, 119), (120, 121, 122, 123, 124, 125), (126, 127, 128, 129, 130, 131), (132, 133, 134, 135, 136, 137), (138, 139, 140, 141, 142, 143)), ((144, 145, 146, 147, 148, 149), (150, 151, 152, 153, 154, 155), (156, 157, 158, 159, 160, 161), (162, 163, 164, 165, 166, 167), (168, 169, 170, 171, 172, 173), (174, 175, 176, 177, 178, 179)), ((180, 181, 182, 183, 184, 185), (186, 187, 188, 189, 190, 191), (192, 193, 194, 195, 196, 197), (198, 199, 200, 201, 202, 203), (204, 205, 206, 207, 208, 209), (210, 211, 212, 213, 214, 215)), ((216, 217, 218, 219, 220, 221), (222, 223, 224, 225, 226, 227), (228, 229, 230, 231, 232, 233), (234, 235, 236, 237, 238, 239), (240, 241, 242, 243, 244, 245), (246, 247, 248, 249, 250, 251)))
for r in range(64):
	txt = open("txt.txt","a")
	txt.write("\n")
	for g in range(64):
		for b in range(64):
			(r,g,b) = (r,g,b)
			hsv = rgb_to_hsv((r,g,b))
			#colors2[(r,g,b)] = colors[int((hsv[0]/360)*7)][int(hsv[1]*5)][int(hsv[2]*5)]
			print((r,g,b))
			
			txt.write(str((r,g,b))+":"+str(colors[int((hsv[0]/360)*7)][int(hsv[1]*5)][int(hsv[2]*5)])+",")
	txt.close()

