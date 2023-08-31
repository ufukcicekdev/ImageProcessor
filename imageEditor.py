from PIL import Image,ImageChops,ImageColor


def image_diff(file_img_1,file_img_2):

    img1 = Image.open(file_img_1).convert('RGB')
    img2 = Image.open(file_img_2).convert('RGB')
    diff = ImageChops.difference(img1, img2)

    RED = ('red')
    RL = Image.new('RGB', diff.size, RED) # Make a red layer the same size
    RedDiff = ImageChops.multiply(RL, diff)
    Result = ImageChops.blend(RedDiff, img1, alpha=0.07)

    datas = Result.getdata()
    newData = []
    for items in datas:
        if items[0] == 255 and items[1] == 255 and items[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(items)
    Result.putdata(newData)
    Result.putalpha(128)
    img1.paste(Result,mask=Result)
    img1.save("dif.png",quality=95)

image_diff('img1.PNG','img2.PNG')
