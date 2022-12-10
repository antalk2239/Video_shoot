import os
import cv2


def get_video_shoot(video_name, video_time):
    time = int(video_time)
    video_capture = cv2.VideoCapture(video_name)
    # 跳到指定时间戳
    video_capture.set(cv2.CAP_PROP_POS_MSEC, time)
    # 读取当前帧
    ret, frame = video_capture.read()
    name = video_name.split(".")
    img_name = str(video_time) + '_' + name[0] + '.png'
    # 保存截图
    cv2.imwrite(img_name, frame)
    return img_name


def get_img_arr(img_name, X1, Y1, X2, Y2):
    img = cv2.imread(img_name)
    x1 = int(X1)
    y1 = int(Y1)
    x2 = int(X2)
    y2 = int(Y2)
    # 获取图片的高度和宽度
    height, width = img.shape[:2]
    # 指定截取区域，左上角坐标 (x1, y1) 和右下角坐标 (x2, y2)
    # 截取图片特定区域
    cropped_img = img[y1:y2, x1:x2]
    # 保存截图
    cv2.imwrite('done_' + img_name, cropped_img)
    return 0


if __name__ == '__main__':
    while True:
        os.system("cls")
        tag = input('1.获取视频指定时戳截图 \n2.获取图片指定区域截图 \n3.获取视频指定时戳指定区域截图\n4.退出 \n请输入序号:')
        tag = int(tag)
        if tag == 1:
            video_name = input('请输入视频名称(带后缀):')
            video_time = input('请输入截图时间（毫秒值）:')
            get_video_shoot(video_name, video_time)
        if tag == 2:
            img_name = input('请输入图片名称(带后缀):')
            x1 = input('左上x坐标:')
            y1 = input('左上y坐标:')
            x2 = input('右下x坐标:')
            y2 = input('右下y坐标:')
            get_img_arr(img_name, x1, y1, x2, y2)
        if tag == 3:
            video_name = input('请输入视频名称(带后缀):')
            video_time = input('请输入截图时间（毫秒值）:')
            x1 = input('左上x坐标:')
            y1 = input('左上y坐标:')
            x2 = input('右下x坐标:')
            y2 = input('右下y坐标:')
            img_name = get_video_shoot(video_name, video_time)
            print(img_name)
            get_img_arr(img_name, x1, y1, x2, y2)
        if tag == 4:
            break
