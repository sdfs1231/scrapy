from bs4 import BeautifulSoup
import sys,requests
from contextlib import closing
class imgdownload():
	def __init__(self):
		self.server='https://unsplash.com/'
		self.validphotos=[]
		self.path='/Users/Administrator/Downloads/a/'
		self.nums=0
	
	def get_img(self):
		req=requests.get(url=self.server,verify=False)
		html=req.text
		a=BeautifulSoup(html)
		imgs=a.find_all('img')
		for j in imgs:
			if j.get('src'):
				validurl=j.get('src')
				if 'photo' in validurl:
					self.validphotos.append(validurl)
			else:
				pass
		self.nums=len(self.validphotos)
	
	def write_to_local(self):
		for i in range(len(self.validphotos)):
			req=requests.get(url=self.validphotos[i],verify=False)
			with closing(req) as r:
				sys.stdout.write('正在下载第%i照片'%(i+1))
				sys.stdout.flush()
				with open(self.path+"%d.jpg"%(i+1),'ab+') as f:
					for chunk in r.iter_content(chunk_size=1024):
						if chunk:
							f.write(chunk)
							f.flush()
					sys.stdout.write('已完成第%d张照片'%(i+1))
					sys.stdout.flush()
dl=imgdownload()
dl.get_img()

print('正在下载')
dl.write_to_local()

print('下载完成')