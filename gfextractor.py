from PIL import Image
import unitypack, os, sys
'''
extract android bundle files
'''
def extractimg(abpath, extractpath):
	for root,dirs,files in os.walk(abpath):
		for filename in files:
			if filename[:10] == 'character_':
				bundle = unitypack.load(open(abpath+"/"+filename,"rb"))
				for asset in bundle.assets:
					filenamearray = filename.split(".")[0].split("_")
					if filenamearray[-1]=='jpvoice':
						continue
					charactername = "_".join(filenamearray[1:])
					if not os.path.exists(extractpath+"/"+charactername):
						os.makedirs(extractpath+"/"+charactername)
					for id, object in asset.objects.items():
						if object.type=="Texture2D":
							data=object.read()
							image = data.image.transpose(Image.FLIP_TOP_BOTTOM)
							image.save(extractpath+"/"+charactername+"/"+data.name+".png","PNG")
'''
make RGBA image file with two image file.
one has RGB info, and the other has A info
'''
def patchimg(extractpath, patchpath):
	for root,dirs,files in os.walk(extractpath):
		for dirname in dirs:
			for root,dirs,files in os.walk(extractpath+"/"+dirname):
				for i in range(len(files)):
					if i+1<len(files) and files[i].split('.')[0]+'_Alpha.png' == files[i+1]:
						image = Image.open(extractpath+"/"+dirname+"/"+files[i]).convert("RGBA")
						width,height = image.size
						image_alpha = Image.open(extractpath+"/"+dirname+"/"+files[i+1]).convert("RGBA").resize(image.size,Image.ANTIALIAS)
						for x in range(width):
							for y in range(height):
								r,g,b,a=image_alpha.getpixel((x,y))
								if r==0 and g==0 and b==0 and a==0:
									image.putpixel((x,y),(0,0,0,0))
								else:
									r,g,b,temp = image.getpixel((x,y))
									image.putpixel((x,y),(r,g,b,a))
						if not os.path.exists(patchpath+"/"+dirname):
							os.makedirs(patchpath+"/"+dirname)
						image.save(patchpath+"/"+dirname+"/"+files[i],"PNG")
						i+=1
if __name__ == "__main__":
	if len(sys.argv) != 4:
		print('Usage : python3 gfextractor.py <Assetbundle path> <Extracted images path> <Patched images path>')
		sys.exit()
	extractimg(sys.argv[1],sys.argv[2])
	patchimg(sys.argv[2],sys.argv[3])
