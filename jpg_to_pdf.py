#problem :
#1. the order of images were ignored in the convert progress although thar images have each of their numbers
import os
from img2pdf import convert

with open('out.pdf', 'wb') as f:
    pdf_list=[]
    pdf_list1=[]

    for root, dirs, files in os.walk('./'):
        for idx, file in enumerate(files):
            fname, ext = os.path.splitext(file)
            if file.endswith('.png'):
                pdf_list.append(file)
                pdf_list1 = sorted(pdf_list)
                for i in range(len(pdf_list)):
                    if i == int(fname[3:]):
                #        pdf_list1.append(pdf_list[i])
            #print(fname[3:])
                

#    pdf = convert(pdf_list)
#    f.write(pdf)
#new = sorted(pdf_list)
#new1 = list(map(int,new))
#print(pdf_list)
print(pdf_list1)
#print(new1)