import sys
sys.path.append('/home/dishan/anaconda3/inkml2img')
import glob, os
import pandas as pd
from inkml2img import *
import xml.etree.ElementTree as et
import cv2 as cv
path='/home/dishan/Documents/ocr/sample'
di={'latex':[],'image':[]}
doc_namespace = "{http://www.w3.org/2003/InkML}"
for i in os.listdir(path) : 
    if i.endswith('.inkml'):
        print(i)
        tree=et.parse(path+'/'+i)
        root=tree.getroot()
        for r in root:
            if (r.tag==doc_namespace+'annotation'): 
                if (r.attrib['type']=='truth') & (len(r.attrib)==1):
                    di['latex'].append(r.text)
        path1='/home/dishan/Documents/ocr/sample/test/{}'.format(i.replace('.inkml','.png')) 
        inkml2img(path+'/'+i,path1)
        di['image'].append(cv.imread(path1))
        
df=pd.DataFrame(di)   
