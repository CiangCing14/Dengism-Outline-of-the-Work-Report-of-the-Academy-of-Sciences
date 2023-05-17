from PIL import Image
import os
ims=[]
for a in os.walk('images'):
    a[2].sort()
    for b in a[2]:
        ims.append(Image.open('%s/%s'%(a[0],b)))

ims=[a.convert('RGB')for a in ims]

image_list = ims[1:]
ims[0].save(r'Dengism-Outline-of-the-Work-Report-of-the-Academy-of-Sciences.pdf', save_all=True, append_images=image_list)
