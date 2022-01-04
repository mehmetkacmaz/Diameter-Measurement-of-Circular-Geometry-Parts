# all functions and constants to be used. organize hierarchicaly
from modules import *

############# CONSTANTS AND PARAMETERS #################################
SMALL = np.finfo(float).eps
rho_air = 1.2 # [kg/m3]
ni = 14.88*10**-6 # [m2/s] kinematic viscosity air
kappa = 0.4 # von Karman constant for atmospheric flows

############# PLOTTING CUSTOMIZATIONS ##################################
plt.rcParams["figure.figsize"] = np.array(plt.rcParams["figure.figsize"])*1
fsize = min(plt.rcParams['figure.figsize'])
#plt.rcParams["image.cmap"] = 'Spectral'
plt.rcParams["image.cmap"] = 'gray' # for images
plt.rcParams["font.size"] = 18
plt.rcParams["axes.grid"] = False
plt.rcParams["figure.dpi"] = 200 # 100
markerlist = [ k for k in Line2D.markers.keys() ]
lineslist = [ k for k in Line2D.lineStyles.keys() ]
plt.rcParams['lines.markersize'] = 10
plt.rcParams["legend.frameon"] = True
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["legend.fancybox"] = False
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
ploting = True # disable if you don't want to see plots


############# TIER 1 ###################################################
def zero_to_small(A):
	"""
	take array A and values whose abs is smalleer than SMALL
	are converted to SMALL
	"""
	A[(A<SMALL) & (A>=0)] = SMALL
	A[(A>-SMALL) & (A<0)] = -SMALL
	return A

def poly_2d(x,y,K):
	return (K[0]+K[1]*x+K[2]*y + K[3]*x**2+K[4]*x*y+K[5]*y**2 + 
		K[6]*x**3+K[7]*x**2*y+K[8]*x*y**2+K[9]*y**3)

def fname_dir(fname):
	"""
	returns the directory in which fname is located
	"""
	return os.path.abspath(os.path.join(fname,os.pardir))

def df_add(df,index,column,value):
	"""
	Add a new value at column and index. If either column or index
	do not exist they are created.
	Works for pandas dataframes.
	"""
	try:
		df[column]
	except:
		df[column]=np.nan
	try:
		df.loc[index]
	except:
		df.loc[index]=np.nan
	df.loc[index,column]=value
	return df

def gaussian(x,mu,sigma,A):
	return A/(sigma*np.sqrt(2*np.pi))*np.exp(
		-(x-mu)**2/(2*sigma**2))

def read_external_data(fname,sep='	',coma=False,bn=False,header=0):
	"""
	read a data file located in fname structured in lines and columns 
	where each column is separated by sep. If the data uses comas 
	instead of dots put replace=True to sort compatibility. In case \n
	shows up at the end of each line but bn=True. Header is
	the number of lines to be skipped at the start of the file.
	returns a matrix
	"""
	f = open(fname,"r")
	Lines = f.readlines()[header:]
	N = len(Lines)
	nVal = len(Lines[N-1].split(sep)) # using last line as reference for number of cloumns
	A = np.zeros((N,nVal))
	for line in range(N):
		if coma:
			Lines[line] = Lines[line].replace(',' , '.')
		if bn:
			Lines[line] = Lines[line].replace('\n' , '')
		A[line] = np.array(Lines[line].split(sep))
	f.close()
	return A.transpose()

def detect_circles(img,resolution=1,delta=10,canny=30,akku=15,rmin=10,rmax=-1):
	"""
	circles: x,y vecotor
	resolution: when multiplied by image size
	delta: min space between circles in px
	canny: threshold for canny edge. The higher the stricter.
	akku: threshold for hough circles accumulator. The higher the stricter.
	rmin: minimum radius of circles
	"""
	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,resolution,delta,
              param1=canny,param2=akku,minRadius=rmin,maxRadius=rmax)[0,:,:-1]
	return circles

def nan_interp(A):
	"""
	Interpolate nans in a matrix
	"""
	ni,nj = np.shape(A)
	# extend edges of A by one
	A = np.concatenate((np.array([A[:,0]]).transpose(),A,np.array([A[:,-1]]).transpose()),axis=1)
	A = np.concatenate((np.array([A[0,:]]),A,np.array([A[-1,:]])),axis=0)
	
	#nit = 0
	#while np.sum(np.isnan(A)) != 0:
	#nit+=1
	nanp = np.isnan(A)
	for i in range(1,ni+1):
		for j in range(1,nj+1):
			if nanp[i,j]:
				#	# edges
				#	if (i==0) & (j!=0)& (j!=nj-1):
				#		b = np.array([A[i+1,j],A[i,j-1],A[i,j+1]])
				#	if (i==ni-1) & (j!=0)& (j!=nj-1):
				#		b = np.array([A[i-1,j],A[i,j-1],A[i,j+1]])
				#	if (j==0) & (i!=0)& (i!=ni-1):
				#		b = np.array([A[i-1,j],A[i+1,j],A[i,j+1]])
				#	if (j==nj-1) & (i!=0)& (i!=ni-1):
				#		b = np.array([A[i-1,j],A[i+1,j],A[i,j-1]])
				#	# corners
				#	if (i==0) & (j==0):
				#		b = np.array([A[i+1,j],A[i,j+1]])
				#	if (i==ni-1) & (j==0):
				#		b = np.array([A[i-1,j],A[i,j+1]])
				#	if (i==0) & (j==nj-1):
				#		b = np.array([A[i+1,j],A[i,j-1]])
				#	if (i==ni-1) & (j==nj-1):
				#		b = np.array([A[i-1,j],A[i,j-1]])
				#	# core
				#	else:
				b = np.array([A[i-1,j],A[i,j-1],A[i+1,j],A[i,j+1]])
				snan = np.sum(np.isnan(b))
				sb = np.nansum(b)
				A[i,j] = sb/(len(b)-snan)
				#print(i,j)
	# only the core matters
	A = A[1:ni+1,1:nj+1]
	return A

def new_directory(name):
	if not os.path.isdir(name):
		os.mkdir(name)
	return name
	
def read_image(fname):
	"""
	Return the loaded image as is (with alpha channel)
	As a numpy array
	"""
	img = cv2.imread(fname,cv2.IMREAD_GRAYSCALE)
	return img

def dir_ftype(directory,extension):
	"""
	find all files with given extension in directory
	order them alphabetically in a list and return them
	"""
	extension = extension.replace(".","") # make sure theres no "."
	fnames = directory+os.sep+"*"+"."+extension
	fnames = glob.glob(fnames)
	fnames = np.sort(fnames) # order files from 0 to last
	return fnames

def dir_fname(directory,nametype):
	"""
	find all files with given extension and string in directory
	order them alphabetically in a list and return them
	"""
	fnames = directory+os.sep+nametype
	fnames = glob.glob(fnames)
	fnames = np.sort(fnames) # order files from 0 to last
	return fnames

def crop_image(img,roi):
	"""
	roi: region of interest, numpy slice, 4 elements, 
	[y_min:y_max,x_min:x_max]
	"""
	img = img[roi]
	return img
	
def canny_edge(img,threshold=15,hysteresis=5):
	img = cv2.Canny(img, threshold-hysteresis,threshold+hysteresis)
	return img

def blur_image(img,Ks,strength=1):
	"""
	Gaussian blur. Currently using the cv2 package.
	Ks is the kernel size and strength is the sigma 
	"""
	Ks = int(Ks)
	if Ks%2 != 1:
		print("blur_image: Ks must be odd! Continuing with Ks = Ks-1")
		Ks = Ks-1
	img = cv2.GaussianBlur(img,(Ks,Ks),strength)#sigmaX=
	return img

def blurd_image(img,order=5,direction='horizontal',strength=0.25,speed='slow'):
	"""
	blur in a given direction with a 
	slow: low pass butterworth filter
	fast: directional averaging convolution
	"""
	ny,nx = np.shape(img)
	if speed == 'slow':
		b, a = scig.butter(order, strength)
		if direction == 'horizontal':
			for i in range(ny):
				img[i,:] = scig.filtfilt(b, a, img[i,:])
		elif direction == 'vertical':
			for i in range(nx):
				img[:,i] = scig.filtfilt(b, a, img[:,i])
		return img
	elif speed=='fast':
		K = np.ones((int(strength),1))
		K = K/np.sum(K)
		if direction=='vertical':
			img=scig.convolve2d(img,K,mode='same')
		elif direction=='horizontal':
			img=scig.convolve2d(img,K.transpose(),mode='same')
		return img
			
			

def zernike_Vnm(rho,theta,n,m):
	"""
	from [2] a function necessary for the calculation of any Anm
	"""
	Rnm = 0
	fact = lambda x: np.math.factorial(x)
	am = abs(m)
	for s in range(0,(n-am)/2):
		Rnm+= (-1)**s*fact(n-s)*rho**(n-2*s)/(
			fact(s)*fact((n+am)/2-s)*fact((n-am)/2-s))
	Vnm = Rnm*np.exp(1j*m*theta)


def ddx(a):
	"""
	The first derivative of a vector assuming a constant spacing of
	1 unit between poitns. Avoid edge effects
	"""
	# avoid corner effects
	thick = 2
	a = np.concatenate((a[(thick-1)::-1],a,a[:-(thick+1):-1]))
	mode="same"
	mode = "valid"
	
	K = np.array([-0.5,0,0.5])
	da = scig.convolve(a,K,mode=mode)
	return da

def ghosal_edge(img,Ks,thr=1,thrmax=0.995,lmin = 0.5,phimin=1.4,thresholding=True, debug=False):
	"""
	implementation of the subpixel edge detection method of [2]. The
	pixels are projected into a new orthogonal domain where a parameter
	k defines the intesity of the edge. By filtering out edges of small
	k the relevant ones remain. The extracted parameters are enough to 
	define a straight edge.
	img: the image to be treated.
	Ks: kernel size
	thr: threshold paramter limiting the minimum of k
	thrmax: threshold limiting the maximum of k. This is usefull to
		remove reflections which have excessively sharp edges
	lmin: is the minimum distance between the pixel center and the
		detected edge. This avoids that big kernels do errors, when 
		close to multiple edges. It also avoids values of l which are
		nonesense, since they only make sense for real edges.
	phimin: allows the user to define a minimum angle in redians 
		measured between the y-axis and the edge.
	"""
	totaltime = time.time()
	kerneltime = time.time()
	# Ks must be odd
	if Ks%2 != 1:
		print("Ks must be odd! Continuing with Ks = Ks-1")
		Ks = Ks-1
	# define the rectangular kernels
	#Vc00 = np.zeros((Ks,Ks),dtype=complex)
	Vc11 = np.zeros((Ks,Ks),dtype=complex)
	Vc20 = np.zeros((Ks,Ks),dtype=complex)
	ofs = 1 *(1-1/Ks) # offset for centering kernel around 0,0
	for i in range(Ks):
		for j in range(Ks):
			Kx = 2*j/Ks-ofs # limits of integration between -1 and 1
			Ky = 2*i/Ks-ofs
			if Kx**2+Ky**2 <= 1: # only a circle
				#Vc00[i,j] = 1 # the conjugate of V00
				Vc11[i,j] = Kx-Ky*1j # ...
				Vc20[i,j] = 2*Kx**2+2*Ky**2-1
	kerneltime = time.time() - kerneltime
	
	# Kernel Plots
	#	VCplot = Vc00
	#	plt.pcolormesh(np.real(VCplot))
	#	plt.title("real w K Vc00")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot))
	#	plt.title("imag w K Vc00")
	#	plt.colorbar()
	#	plt.show()
	#	VCplot = Vc11
	#	plt.pcolormesh(np.real(VCplot))
	#	plt.title("real w K Vc11")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot))
	#	plt.title("imag w K Vc11")
	#	plt.colorbar()
	#	plt.show()
	#	VCplot = Vc20
	#	plt.pcolormesh(np.real(VCplot))
	#	plt.title("real w K Vc20")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot))
	#	plt.title("imag w K Vc20")
	#	plt.colorbar()
	#	plt.show()
	
	# do the convolution with the images to get the zernike moments
	Anorm = lambda n : (n+1)/np.pi	# a normalization value
	convolvetime = time.time()
	#A00 = scig.convolve2d(img,Vc00,mode='same')
	#	A11 = Anorm(1)*scig.convolve2d(img,Vc11,mode='same')
	#	A20 = Anorm(2)*scig.convolve2d(img,Vc20,mode='same')
	A11 = Anorm(1)*scig.oaconvolve(img,Vc11,mode='same')
	A20 = Anorm(2)*scig.oaconvolve(img,Vc20,mode='same')
	convolvetime = time.time() - convolvetime
	# Plot Zernike moments
	#	VCplot = A00
	#	plt.pcolormesh(np.real(VCplot))
	#	plt.title("real A00")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot))
	#	plt.title("imag A00")
	#	plt.colorbar()
	#	plt.show()
	#	VCplot = A11
	#	plt.pcolormesh(np.real(VCplot))
	#	plt.title("real A11")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot))
	#	plt.title("imag A11")
	#	plt.colorbar()
	#	plt.show()
	#	VCplot = A20
	#	plt.pcolormesh(np.real(VCplot))
	#	plt.title("real A20")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot))
	#	plt.title("imag A20")
	#	plt.colorbar()
	#	plt.show()
	
	paramstime = time.time()
	# calculate the edge paramters
	#	tanphi = np.imag(A11)/np.real(A11)
	#	phi = np.arctan(tanphi)
	#	cosphi = np.cos(phi)
	#	sinphi = cosphi*tanphi
	#	Al11 = np.real(A11)*cosphi+np.imag(A11)*sinphi
	
	phi = np.arctan(np.imag(A11)/np.real(A11))
	Al11 = np.real(A11)*np.cos(phi)+np.imag(A11)*np.sin(phi)
	
	#	Al11 = A11*np.exp(-phi*1j)
	l = A20/Al11 # A20 has no imaginary component so A20 = A'20

	k = 3*Al11/(2*(1-l**2)**(3/2))
	paramstime = time.time() - paramstime
	
	# Plot edge paramters
	#	VCplot = phi
	#	plt.pcolormesh(np.real(VCplot))
	#	plt.title("real phi")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot))
	#	plt.title("imag phi")
	#	plt.colorbar()
	#	plt.show()
	#	VCplot = Al11
	#	plt.pcolormesh(np.real(VCplot))
	#	plt.title("real A\'11")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot))
	#	plt.title("imag A\'11")
	#	plt.colorbar()
	#	plt.show()
	#	VCplot = l
	#	plt.pcolormesh(np.real(VCplot))#,vmin=-5,vmax=5
	#	plt.title("real l")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot)) # ,vmin=-5,vmax=5
	#	plt.title("imag l")
	#	plt.colorbar()
	#	plt.show()
	#	VCplot = k
	#	plt.pcolormesh(np.real(VCplot))
	#	plt.title("real k")
	#	plt.colorbar()
	#	plt.show()
	#	plt.pcolormesh(np.imag(VCplot))
	#	plt.title("imag k")
	#	plt.colorbar()
	#	plt.show()
	
	
	treattime = time.time()
	if thresholding==True:
		# do the thresholding
		if (thrmax<0)&(thr>0):
			knorm = np.sort(k.flatten())[[int(thr*np.size(k)),int(thrmax*np.size(k))]]
			idx = (abs(l)<lmin)&(abs(phi)>phimin)&(abs(k)>knorm[0])
		elif thrmax>0:
			knorm = np.sort(k.flatten())[[int(thr*np.size(k)),int(thrmax*np.size(k))]]
			idx = (abs(l)<lmin)&(abs(phi)>phimin)&(abs(k)>knorm[0])&(abs(k)<knorm[1])
		elif thr<0:
			idx = (abs(l)<lmin)&(abs(phi)>phimin)
			knorm = np.sort(k[idx].flatten())[int(thr)]
			idx = idx&(abs(k)>abs(knorm))
		ne = np.sum(idx)
	elif thresholding==False:
		raise ValueError("this option is not still uncer development")
		# no thresholding
		idx = np.ones(np.shape(l),dtype=bool)
		ne =np.sum(idx)
	else:
		raise ValueError("thresholding should be boolean")
	
	# put all detected points in a vector of (x,y) values
	edg = np.zeros((ne,2))
	org = np.zeros((ne,2))
	nx,ny = np.shape(img)
	e = 0
	for i in range(nx):
		for j in range(ny):
			if idx[i,j]:
				edg[e]=np.array([i,j]) + l[i,j]*Ks/2*np.array(
					[np.sin(phi[i,j]),-np.cos(phi[i,j])])
				org[e]=np.array([i,j])
				e +=1
	treattime = time.time() - treattime
	totaltime = time.time() - totaltime
	print("total %0.5f	convolution %0.5f	thresholding %0.5f	paramters %0.5f	kernel %0.5f"%(totaltime,convolvetime,treattime,paramstime,kerneltime))
	
	if debug==True:
		return edg, org, k, l, phi
	else:
		return edg, org
		
def ghosal_edge_v2(img,Ks,kmin=0,kmax=1000,lmax=0.5,phimin=1,thresholding=True,debug=False,mirror=False):
	"""
	implementation of the subpixel edge detection method of [2]. The
	pixels are projected into a new orthogonal domain where a parameter
	k defines the intesity of the edge. By filtering out edges of small
	k the relevant ones remain. The extracted parameters are enough to 
	define a straight edge.
	img: the image to be treated.
	Ks: kernel size
	thr: threshold paramter limiting the minimum of k
	kmax/min: threshold limiting k. This is usefull to define the edge
		intensity range that we are looking for. Neither too strong nor
		too weak
	lmax: is the maximum distance between the pixel center and the
		detected edge. This avoids that big kernels do errors, when 
		close to multiple edges. It also avoids values of l which are
		nonesense, since they only make sense for real edges.
	phimin: allows the user to define a minimum angle in radians 
		measured between the y-axis and the edge.
	thresholding: in case no thresholding is desired, might make sense
		for debugging or for post-processing raw data of edges
	debug: will output k, l and phi matrices
	mirror: mirror the limits of the image during convolution 
		so that no aliasing happens during the convolution. 
		Convolution time is doubled for some cases if this is activated. 
	"""
	# gather image properties before its altered
	ni,nj = np.shape(img)
	# Ks must be odd
	if Ks%2 != 1:
		print("Ks must be odd! Continuing with Ks = Ks-1")
		Ks = Ks-1
	# define the rectangular kernels
	#Vc00 = np.zeros((Ks,Ks),dtype=complex) # not needed
	Vc11 = np.zeros((Ks,Ks),dtype=complex)
	Vc20 = np.zeros((Ks,Ks),dtype=complex)
	ofs = 1 *(1-1/Ks) # offset for centering kernel around 0,0
	for i in range(Ks):
		for j in range(Ks):
			Kx = 2*j/Ks-ofs # limits of integration between -1 and 1
			Ky = 2*i/Ks-ofs
			if Kx**2+Ky**2 <= 1: # only a circle
				#Vc00[i,j] = 1 # the conjugate of V00 # not needed
				Vc11[i,j] = Kx-Ky*1j # ...
				Vc20[i,j] = 2*Kx**2+2*Ky**2-1
	# mirror the edges to avoid edge effects from convolution
	if mirror:
		thick = int((Ks-1)/2)
		img = np.concatenate((img[:,(thick-1)::-1],img,img[:,:-(thick+1):-1]),1)
		img = np.concatenate((img[(thick-1)::-1,:],img,img[:-(thick+1):-1,:]),0)
		mode = "valid"
	else:
		mode = "same"
	
	# do the convolution with the images to get the zernike moments
	Anorm = lambda n : (n+1)/np.pi	# a normalization value
	#A00 = scig.convolve2d(img,Vc00,mode='same') # not needed
	A11 = Anorm(1)*scig.oaconvolve(img,Vc11,mode=mode)
	A20 = Anorm(2)*scig.oaconvolve(img,Vc20,mode=mode)

	phi = np.arctan(np.imag(A11)/zero_to_small(np.real(A11)))
	Al11 = np.real(A11)*np.cos(phi)+np.imag(A11)*np.sin(phi)
	l = np.real(A20)/Al11 # A20 has no imaginary component so A20 = A'20
	l = np.minimum(l,1-SMALL) # chop off those that go beyond the kernel boundaries
	l = np.maximum(l,-1+SMALL)
	k = abs(3*Al11/(2*(1-l**2)**(3/2))) 
	
	if thresholding==True:
		# conditions
		phi_c = abs(phi)>phimin
		l_c = abs(l)<lmax
		k_c = (k<kmax) & (k>kmin)
		valid = phi_c & (k_c & l_c)
	elif thresholding==False:
		valid = np.ones_like(k)
	# define a grid of pixel positions
	i,j = np.meshgrid(np.arange(nj),np.arange(ni))
	
	# get a list of the valid relevant parameters 
	i = i[valid]
	j = j[valid]
	#	k = k[valid] # not necessary
	l = l[valid]
	phi = phi[valid]
	
	# convert to the subpixel position
	i_s = i+l*Ks/2*np.cos(phi)
	j_s = j+l*Ks/2*np.sin(phi)
	
	# put all detected points in a vector of (x,y) values
	edg = np.squeeze((j_s,i_s)).transpose()
	org = np.squeeze((j,i)).transpose()
	if debug==True:
		return edg, org, k, l, phi
	else:
		return edg, org

def line_fit(x,y):
	"""
	Returns a straight line (two points) that is the best fit to a cloud
	of x,y values
	"""
	# clean
	x = np.squeeze(x)
	y = np.squeeze(y)
	# concatenate
	xy = np.concatenate((x[:,np.newaxis],y[:,np.newaxis]),1)
	# sort by x values
	xy = xy[xy[:,0].argsort()]
	#print(xy)
	f = lambda x,m,b : m*x+b
	pars,_ = opt.curve_fit(f,xy[:,0],xy[:,1])
	m = pars[0]
	b = pars[1]
	pts = np.zeros((2,2))
	pts[0,0] = xy[0,0]
	pts[1,0] = xy[-1,0]
	pts[:,1] = pts[:,0]*m+b
	sig = np.std((xy[:,1]-f(xy[:,0],m,b)))
	return pts, sig


def remove_dbledge(img):
	"""
	The image has to be binary. Get only the points closest to the 
	bottom of the image.
	"""
	(ny,nx) = np.shape(img)
	for i in range(nx):
		idx = np.array(np.nonzero(img[:,i]))
		if np.size(idx) == 0:
			continue
		idx = idx[0][-1]
		img[idx-1::-1,i] = 0
	return img

def solve_L(centers_i,centers_r):
	"""
	From [1] as an intermediary step to obtain the reorientation of the 
	calibration plate.
	L is a matrix which when multiplied with the rotation and 
	translation parameters r'1, r'2, r'4, r'5 and T'x returns the vector
	of the x_r values at each calibration point. Solving it results in
	the	vector of rotation parameters. T'x and T'y require special 
	treatment later on.
	"""
	# The first term is a column vector of size N. Each of its rows
	# multiplies with the respective row on the x_r with 2 columns and 
	# N rows.
	Ly = centers_i[:,1][np.newaxis,:].transpose() * centers_r
	Lx = - centers_i[:,0][np.newaxis,:].transpose() * centers_r
	L = np.concatenate((Ly,centers_i[:,1][np.newaxis,:].transpose(),Lx),
		axis=1)
	b = centers_i[:,0]
	print("solving for the rotation and translation coefficients...")
	rl,resids,rank,svals = np.linalg.lstsq(L,b)
	print("residue:%0.4f	rank:%0.4f"%(np.sum(resids),rank))
	return rl

############# TIER 2 ###################################################
def select_points(fname,n=-1,prompt=""):
	"""
	Open an image and allow for the selection of points to be diplayed
	as an array later
	"""
	#def onclose(event):
	#	raise ValueError("Figure Closed by user. No input. Exiting.")
	if type(fname) is type(plt.figure()):
		fig = fname
		ax1 = fig.axes[0]
	else:
		fig,ax1 = plt.subplots(1)
	
	if type(fname) is str:
		img = read_image(fname)
	elif type(fname) is np.ndarray:
		img = fname
	#if n == 1:
	#	mouse = {"mouse_add":2, "mouse_pop":1,"mouse_stop":3}
	#	plt.xlabel("middle click: add point",fontsize="xx-small")
	#else:
	mouse = {"mouse_add":2, "mouse_pop":1,"mouse_stop":3}
	try:
		ax1.imshow(img)
	except:
		1 == 2
	fig.suptitle(prompt)
	ax1.set_xlabel("L click: remove previous - middle click: add point - R click: exit",fontsize="xx-small")
	#fig = plt.gcf() # get current figure
	#fig.canvas.mpl_connect('close_event', onclose) # raise value error if figure is closed
	pts = fig.ginput(n=n,timeout=0,**mouse)
	plt.close()
	return pts

def gradient_edge(img):
	def error(y,mu,sigma,A):
		return y-gaussian(np.arange(0,len(y)),mu,sigma,A)
	#	optimum,residu = opt.leastsq(\
	#		error, guess, args=(x,y))
	nx,ny = np.shape(img)
	
	for i in range(nx):
		I = img[:,i]
		dI = ddx(I)
		maxx = np.where(dI == max(dI))
		minx = np.where(dI == min(dI))
		plt.plot(I)
		plt.plot(dI)
		plt.show()
		#if i == 0:

def polyfit_2d(Xu,X):
	"""
	Xu is a vector of the positions of the points in pixels
	X is the vector of the positions of the points in meters
	The result is a set of coefficients k which allow the mapping of a
	point in the reference of Xu to the reference of X using poly_2d
	"""
	xu = Xu[:,0]
	yu = Xu[:,1]
	X = np.squeeze(X) # an mx1 vector
	M = np.squeeze((np.ones(xu.size),xu,yu,xu**2,xu*yu,yu**2,
		xu**3,xu**2*yu,xu*yu**2,yu**3)) # a mxn matrix
	M = M.transpose()
	print("solving for the polynomial fitting coefficients...")
	K,resid,rnk,svs = np.linalg.lstsq(M,X,rcond=-1) # k has size n
	print("residue:%0.8f	rank:%0.8f"%(np.sum(resid),rnk))
	return K
	
	
def beads(img,yps=None,thr=6,skip=5,nbead=0):
	ny,nx = np.shape(img)
	
	def search_peaks(yps):
		dI = ddx(img[yps,:])
		peaks = np.zeros(len(dI))
		i = 0
		while i < len(dI):
				if dI[i]>thr:
					peaks[i] = 1
					i+=skip
				i+=1
		return peaks, dI # a vector with 1 at positions where a peak was detected		
	if yps == None: # scan the image vertically until a good result is found
		yps=0
		peaks = 0
		while np.sum(peaks)!=nbead:
			yps+=1
			peaks, dI = search_peaks(yps)
	else:
		peaks, dI = search_peaks(yps)
	#	plt.plot(peaks)
	#	plt.plot(dI)
	#	plt.show()
	return peaks, dI, yps


############# TIER 3 ###################################################

def tune_ghosal(fimg,K_s=5,k_m=None,N_k=5000,l_max=0.5,phi_min=1.45,outlier_sigma=2,blur=10):
	"""
	help make the selection of parameters for the function faster
	Machine learning on v2 of this code
	"""
	# open
	img = read_image(fimg)
	camera = fimg[-10]
	
	# ensure N_k is even
	if N_k%2!=0:
		N_k+=1
		print("N_k=%0.5f"%N_k)
	
	# blur image
	img = blurd_image(img,order=1,strength=blur,speed='fast')
	
	# calculate k,l and phi for the whole image
	_,_,k,l,phi = ghosal_edge_v2(img,Ks=K_s,debug=True)
	
	# find mean k
	if k_m == None:
		ij_m = select_points(img,n=1,prompt="choose a characteristic edge location")
		ij_m = np.array(ij_m[0],dtype=int)
		k_m = k[ij_m[1],ij_m[0]]
		print("k_m=",k_m)
	
	# find k limits
	k_sort = np.sort(k.flatten())
	k_sort[np.isnan(k_sort)]=0 # get rid of nans for argmin
	#print(np.shape(k_sort))
	#i_km = np.where(k_sort==k_m)[0][0]
	i_km = (np.abs(k_sort - k_m)).argmin()
	i_kmin = int(i_km-N_k/2)
	i_kmax = int(i_km+N_k/2)
	k_min = k_sort[i_kmin]
	k_max = k_sort[i_kmax]
	edg,org = ghosal_edge_v2(img,K_s,kmax=k_max,kmin=k_min,lmax=l_max,phimin=phi_min)
	
	# outlier removal
	pts,sig = line_fit(edg[:,1],edg[:,0])
	ptsy = np.mean(pts[:,1])
	accepted = ((edg[:,0]<(ptsy+outlier_sigma*sig)) & (edg[:,0]>(ptsy-outlier_sigma*sig)))
	edga = edg[accepted,:]
	
	# plotting
	vectors = edg-org # show the vectors also
	plt.imshow(img)
	plt.quiver(org[:,1],org[:,0],vectors[:,1],vectors[:,0],angles='xy',
		scale_units='xy', scale=1, color = 'orange')
	plt.scatter(edga[:,1],edga[:,0],c='blue',marker='.')
	plt.title("Validated Points")
	plt.show()
	
	# save
	print("Paramters:\n Camera %s:	K_s=%0.5f	k_min=%0.5f	k_max=%0.5f	l_max=%0.5f	phi_min=%0.5f outlier_sigma=%0.5f	blur=%0.5f"
		%(camera,K_s,k_min,k_max,l_max,phi_min,outlier_sigma, blur))
	save = input("save current parameters?(y/n)	")
	if save=="y":
		savename = fname_dir(fimg)
		savename = savename+os.sep+camera+"_ghosal_edge_parameters.txt"
		savematrix = np.squeeze([K_s,k_min, k_max, l_max, phi_min, outlier_sigma, blur])
		np.savetxt(savename,savematrix,delimiter="	")
		print("saved\n",savematrix)
	

############# EXTERNAL #################################################

def animate(directory,gifname,n_t,step=2,duration=0.2):
	"""
	n_t is the nuber of images you want
	step is how many images int the directory to skip each timestep
	duration is the duration of each frame in the final gif
	Based on the gif code of the SP classes of M Mendez 2019
	"""
	# create list of filenames
	fnames = dir_fname(directory,"*")
	# create list of plots
	images=[]    
	for k in range(0,n_t):
		k = k*step
		print('Mounting Im '+ str(k))
		FIG_NAME=fnames[k]
		images.append(imageio.imread(FIG_NAME)) # read
	# Now we can assemble the video
	imageio.mimsave(gifname, images,duration=duration) # create gif
	print('Animation'+gifname+'Ready')
	return True
