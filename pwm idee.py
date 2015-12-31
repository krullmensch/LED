col = [255,128,64]
pin = [18,23,24]
ord = []
tln = {}

min = 0

for i in range(3):
	tmp = 255
	tmp2 = 0
	for j in range(3):
		if col[j] <= tmp and col[j] >= min and j not in ord:
			tmp = col[j]
			tmp2 = j
	ord.append(tmp2)
	min = tmp
	
last = 0
for k in ord:
	tln[k] = col[k]/10-last
	last = col[k]/10
	
while True:
	for i in pin:
		G.output(i,True)
	
	for i in range(3);
		sleep(tln[i]/1000)
		G.output(ord[i],False)