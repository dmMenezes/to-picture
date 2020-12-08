from PIL import Image

#source later to be turned into argument or default
im = Image.open("C:/Users/DmM67/Documents/projects/python/to-pic/source/source.jpg")

k=0
iwidth,iheight = im.size
#print(iwidth,iheight)

#size of crop
w=200
h=200

#ow,oh -> original width and height
ow,oh = iwidth,iheight
col = int(iwidth/w)
col_last = iwidth - col * w
#print(col,col_last)
row = int(iheight/h)
row_last = iheight - row * h
#print(row,row_last)

for i in range(1,row+2):
    for j in range(1,col+2):
        #print(i,j)
        left = w * (j - 1)
        upper = h * (i - 1)
        right = w * j
        lower = h * i
        if (i == row + 1):
            if (row_last != 0):
                lower=oh
            else:
                continue
        if (j == col + 1):
            if (col_last != 0):
                right=ow
            else:
                continue
        box = (left, upper, right, lower)
        #print(box)
        im_crop = im.crop(box)
        #save path. later to be turned into argumrnt or default
        #i and j represent loacation of image. i represents row and j represents columns.
        #i,j start feom (1,1) at left top corner
        
        im_crop.save("C:/Users/DmM67/Documents/projects/python/to-pic/result/result-i" + str(i) + "j" + str(j) + ".jpg")
        k = k + 1

if(col_last):
    col = col + 1
if(row_last):
    row= row + 1
total_parts = col * row

print("DONE!",total_parts)
#im_crop = im.crop((left, upper, right, lower))
#im_crop = im.crop((0, 0, 500, 500))
#im_crop.save("C:/Users/DmM67/Documents/projects/python/to-pic/result/result.jpg")