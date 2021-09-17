import os
import img2pdf
import natsort

directory = './'

with open('out.pdf', 'wb') as f:
    pdf_list = []
    files = natsort.natsorted(os.listdir(directory))
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            pdf_list.append(file)

    pdf = img2pdf.convert(pdf_list)
    f.write(pdf)
    
#if you see the TypeError: blah blah 'str', you must check the directory first!
#you can get the information about 'encode' or 'byte' etc, but it will be probably not the answer.