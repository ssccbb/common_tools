import os
import sys


def apktool_apk(apk, dirs):
    print("开始反编译原apk...")
    cmd = f'java -jar ./jar/apktool.jar d {apk} -o {dirs}'
    if os.system(cmd) == 0:
        print(f'输出路径 >>> {dirs}')
        print("成功反编译原apk")
    else:
        raise Exception("反编译原apk失败")
    pass


if __name__ == '__main__':
    """apktool解包工具"""
    print(sys.argv)
    len_argv = len(sys.argv)
    if len_argv >= 2:
        apk_file_name = sys.argv[1]
        output_dir = apk_file_name.replace(".apk", "")
    if len_argv == 3:
        output_dir = sys.argv[2]
    if len_argv > 3:
        print(f'不支持的参数, 命令格式为： python [apktool.py路径] [apk路径] [输出文件夹(如果有)]')
        sys.exit(0)
    if not os.path.exists(output_dir):
        apktool_apk(apk_file_name, output_dir)
    else:
        output_dir = f'{output_dir}_new'
        apktool_apk(apk_file_name, output_dir)
    pass