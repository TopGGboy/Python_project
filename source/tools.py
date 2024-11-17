import os
import pygame
import json


def load_graphics(path, accept=('.png', '.jpg', '.bmp', '.gif')):
    """
    函数功能：
    用于加载指定路径下特定格式的图像文件，并将它们以易于访问的字典形式进行存储，方便后续在游戏开发等场景中使用这些图像资源。

    参数说明：
    - path：字符串类型，表示图像文件所在的文件夹路径。该函数会遍历此路径下的所有文件，从中筛选出符合要求的图像文件进行加载。
    - accept：元组类型，默认值为('.png', '.jpg', '.bmp', '.gif')，用于指定可接受的图像文件扩展名。只有扩展名在这个元组中的图像文件才会被加载。

    返回值：
    返回一个字典（graphics），字典的键（key）是图像文件去除扩展名后的文件名，值（value）是对应的加载并经过适当转换后的Pygame图像对象，这样可以通过文件名方便地获取相应的图像资源。
    """
    # 创建一个空字典，用于存储加载后的图像资源，字典的键是文件名（不含扩展名），值是对应的Pygame图像对象
    graphics = {}
    # 遍历指定路径下的所有文件和文件夹（通过os.listdir函数获取文件名列表）
    for pic in os.listdir(path):
        # 将文件名和扩展名分离，os.path.splitext函数返回一个包含文件名（不含扩展名）和扩展名的元组
        name, ext = os.path.splitext(pic)
        # 判断文件的扩展名（转换为小写形式）是否在可接受的扩展名列表（accept）中
        if ext.lower() in accept:
            # 使用os.path.join函数将路径和文件名组合成完整的文件路径，然后通过pygame.image.load函数加载图像文件，得到一个Pygame图像对象
            img = pygame.image.load(os.path.join(path, pic))
            # 判断图像是否有透明通道（通过img.get_alpha方法获取），如果有透明通道，则调用img.convert_alpha方法进行转换，
            # 这样可以正确处理图像的透明效果，并且在后续绘制等操作中能有更好的性能表现
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                # 如果图像没有透明通道，则调用img.convert方法进行普通的图像格式转换，将图像转换为适合在Pygame中快速绘制的格式
                img = img.convert()
            # 将文件名（不含扩展名）作为键，对应的Pygame图像对象作为值，存入graphics字典中，以便后续通过文件名来获取图像
            graphics[name] = img
    # 返回存储了所有加载并转换好的图像资源的字典
    return graphics


def get_image(sheet, x, y, width, height, colorkey, scale):
    """
    函数功能：
    从给定的图像（sheet）中提取指定区域的子图像，并进行颜色键处理和缩放操作，最后返回处理后的图像。

    参数说明：
    - sheet：一个Pygame的Surface对象，表示包含多个子图像的源图像。
    - x, y：整数，指定要提取的子图像在源图像中的左上角坐标。
    - width, height：整数，指定要提取的子图像的宽度和高度。
    - colorkey：一个颜色值（通常是一个三元组 (R, G, B)），用于设置透明颜色。如果图像中的某个像素颜色与colorkey相同，那么该像素将被设置为透明。
    - scale：浮点数，表示缩放倍数，用于放大或缩小提取的子图像。

    返回值：
    返回一个经过处理（提取、颜色键处理、缩放）后的Pygame Surface对象，即所需的子图像。
    """
    # 创建一个新的Surface对象，大小为指定的宽度和高度
    image = pygame.Surface((width, height))
    # 将源图像（sheet）的指定区域（由 (x, y, width, height) 指定）绘制到新创建的Surface对象（image）上
    image.blit(sheet, (0, 0), (x, y, width, height))
    # 设置颜色键（colorkey），使图像中与colorkey颜色相同的像素变为透明
    image.set_colorkey(colorkey)
    # 对图像进行缩放操作，将图像的宽度和高度分别乘以缩放倍数scale，并将结果转换为整数
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    # 返回处理后的图像
    return image


# 处理地图json文件
def read_map(file_name, LEVEL_NUMBER):
    # 将文件名与地图数据文件夹路径拼接
    file_path = os.path.join('source/data/maps', file_name)
    # 打开文件并读取数据
    with open(file_path) as f:
        data = json.load(f)

    for level_ in data:
        if data[level_]['number'] == LEVEL_NUMBER:
            MAP = data[level_]['map']
            PLAYER_BUFF = data[level_]['buff']
            # tools.modify_json('source/data/maps/memory.json', "level_number", constans.LEVEL_NUMBER)

    return MAP, PLAYER_BUFF
