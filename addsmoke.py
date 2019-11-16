import cv2
import os
import sys


def get_images_data(src_path = 'src',smoke_path = './/smoke'):
    data = []
    for root, dirs, files in os.walk(src_path, topdown=False):
        for name in files:
            src = os.path.join(root, name)
            print(src)
            smoke = os.path.join(smoke_path,name)
            print(smoke)
            value = {"src": src, 'smoke':smoke}
            data.append(value)
    return data


def together(src = '1.jpg',smoke = '2.jpg',fname = 'test.jpg'):
    try:
        src = cv2.imread(src)#//读取资源文件
        smoke = cv2.imread(smoke)#//读取相应的烟
        rows, cols = src.shape[:2]#//资源图像大小
        smoke_dst = cv2.resize(smoke, (cols, rows), interpolation=cv2.INTER_CUBIC)  # 调整到和资源一样大小
        add_img = cv2.addWeighted(smoke_dst, 0.5, src, 0.5, 0)
        cv2.imwrite(fname,add_img);
    except BaseException as e:
        print(e)
    return

if __name__ == "__main__":
    #//设置新保存的文件名
    new_path = './new_img'
    if(not os.path.exists(new_path)):
        os.mkdir(new_path)
    #//含烟目录
    smoke_path = 'smoke'
    #//无烟目录
    src_path = 'src'
    #//将烟文件夹和无烟文件夹中图片配对；返回list
    data = get_images_data(src_path,smoke_path)
#//开始合成
    for i ,value in enumerate(data):
        src ,smoke = value['src'],value['smoke']
        fname = new_path + '//' + ''.join(src.split('\\')[-1])
        together(src,smoke,fname)

    pass
