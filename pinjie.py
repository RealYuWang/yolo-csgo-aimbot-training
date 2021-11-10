from PIL import Image

def join(png1, png2, flag='vertical'):
    """
    :param png1: path
    :param png2: path
    :param flag: horizontal or vertical
    :return:
    """
    img1, img2 = Image.open(png1), Image.open(png2)
    # 统一图片尺寸，可以自定义设置（宽，高）
    img1 = img1.resize((1500, 1000), Image.ANTIALIAS)
    img2 = img2.resize((1500, 1000), Image.ANTIALIAS)
    size1, size2 = img1.size, img2.size
    if flag == 'horizontal':
        joint = Image.new('RGB', (size1[0] + size2[0], size1[1]))
        loc1, loc2 = (0, 0), (size1[0], 0)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('horizontal2.png')
    elif flag == 'vertical':
        joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))
        loc1, loc2 = (0, 0), (0, size1[1])
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('vertical.png')

if __name__ == '__main__':
    # 两张图片地址：
    png1 = r"horizontal.png"
    png2 = r"horizontal1.png"
    # 横向拼接
    join(png1, png2, flag='vertical')

    # 纵向拼接
    # join(png1, png2, flag='vertical')