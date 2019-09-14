from bs4 import BeautifulSoup
import requests,sys
class downloader():
	def __init__(self):
		self.server="https://www.biqukan.com"
		self.book=self.server+"/1_1094/"
		self.path='/Users/Administrator/Downloads/a/'
		self.urls=[]
		self.names=[]
		self.nums=0
	def get_chap(self):
		req=requests.get(url=self.book)
		req.encoding='gbk'
		html=req.text
		L=BeautifulSoup(html)
		a_br=L.find_all('div',class_='listmain')
		a=BeautifulSoup(str(a_br[0]))
		
		chap=a.find_all('a')
		chap=chap[16:]
		self.nums=len(chap)
		
		for each in chap:
			self.names.append(each.string)
			self.urls.append(self.server+each.get('href'))
	
	def save_to_local(self,name,chap):
		
		with open(self.path+name+'.txt','a',encoding='utf-8')as f:
			f.write(self.get_content(chap))
	
	def get_content(self,chapurl):
		r=requests.get(url=chapurl)
		r.encoding='gbk'
		html=r.text
		div=BeautifulSoup(html)
		content=div.find_all('div',class_='showtxt')
		content=content[0].text.replace("\xa0"*7,"\n\n")
		return content


dl=downloader()
dl.get_chap()
print('开始下载...')
for i in range(dl.nums):
	dl.save_to_local(dl.names[i],dl.urls[i])
	sys.stdout.write("已下载%.3f%%"%float(i/dl.nums)+'\r')
	sys.stdout.flush()
print("已完成")