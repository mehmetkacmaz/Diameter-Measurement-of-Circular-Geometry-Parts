# v3 started on Mar 24
# General edge detection

################ IMPORTS ###############################################
from modules import *
from functions import *

################ MAIN ##################################################

### Read Settings Files
# the test matrix contains the names of images to be processed 
# and information on how to process each one
img_info = pd.read_csv(
	os.path.join("Settings","imageinfo.csv"),sep=",")
idx_cases = np.where(img_info.process == "x")
img_info = img_info.iloc[idx_cases[0]] # remove images wo/ x
ncases = len(img_info)
# the folder where the results are to be saved
save = pd.read_csv(
	os.path.join("Settings","saveTo.csv"),sep="	").iloc[0].directory
if not os.path.isdir(save):
	os.mkdir(save)
# new folder with timestamp
savedirect = os.path.join(save,str(datt.now())[:-7])
if not os.path.isdir(savedirect):
	os.mkdir(savedirect)
# the folder containing all the images
datafolder = pd.read_csv(
	os.path.join("Settings","dataFolder.csv")).iloc[0].directory

### cycle cases of img_info
pbarc = tqdm(total=ncases) # progress bar
for c in range(ncases):
	# files, files..
	direct = os.path.join(datafolder,img_info.iloc[c].Name)
	# read the output file of tune_ghosal to get the parameters for edge
	# detection, edge thresholding and blurring
	pars = read_external_data(
		os.path.join("Settings",str(img_info.iloc[c].GPars)))[0]
	K_s, k_min, k_max, l_max, phi_min, outlier_sigma, blur = \
		int(pars[0]),pars[1],pars[2],pars[3],pars[4],pars[5],pars[6]

	## detection and saving	
	# open original image
	img_o = read_image(direct)
	h, w = img_o.shape
	# blur (i.e filter) image
	img_f = blur_image(img_o,blur)
	# detect edges: Ghosal
	edg_full, org = ghosal_edge_v2(img_f,K_s,kmax=k_max,
		kmin=k_min,lmax=l_max,phimin=phi_min,mirror=True)
	# save to savedirect with same name as img
	savename = os.path.splitext(os.path.basename(direct))[0]+".txt"
	savename = os.path.join(savedirect,savename)
	np.savetxt(savename,edg_full,delimiter="	")
	
	if ploting == True:
		# plotting
		vectors = edg_full-org # show the vectors also
		plt.imshow(img_f)
		plt.quiver(org[:,1],org[:,0],vectors[:,1],vectors[:,0],angles='xy',
			scale_units='xy', scale=1, color = 'orange')
		plt.scatter(edg_full[:,1],edg_full[:,0],c='blue',marker='.')
		plt.title("detected points")
		plt.show()
	# progress bar
	pbarc.update(1)
pbarc.close()

# for convenience
input('Press ENTER to exit')
	
