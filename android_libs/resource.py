# -*- coding: UTF-8 -*-

import os, shutil
from android_libs import template, initializer


drawable_type = (
    'shape-circle', 'shape-rectangl', 'selector-normal'
)
drawable_picture_dir = (
    'drawable-hdpi', 'drawable-mdpi', 'drawable-xhdpi', 'drawable-xxhdpi', 'drawable-xxxhdpi',
    'mipmap-hdpi', 'mipmap-mdpi', 'mipmap-xhdpi', 'mipmap-xxhdpi', 'mipmap-xxxhdpi',
)


def generate_layout_file(layout_file_name):
    """生成layout文件"""
    template.copy_file(
        template.PathConfig.runtime_layout_normal,
        initializer.AndroidConfig.generate_config_by_default_config().res_layout_path + '/' + layout_file_name + '.xml'
    )


def generate_drawable_file(drawable_type, drawable_name):
    """生成drawable文件"""
    if drawable_type == 'shape-circle':
        template.copy_file(
            template.PathConfig.runtime_shape_circle,
            initializer.AndroidConfig.generate_config_by_default_config().res_drawable_path + '/' + drawable_name + '.xml'
        )
    if drawable_type == 'shape-rectangl':
        template.copy_file(
            template.PathConfig.runtime_shape_rectangle,
            initializer.AndroidConfig.generate_config_by_default_config().res_drawable_path + '/' + drawable_name + '.xml'
        )
    if drawable_type == 'selector-normal':
        template.copy_file(
            template.PathConfig.runtime_selector,
            initializer.AndroidConfig.generate_config_by_default_config().res_drawable_path + '/' + drawable_name + '.xml'
        )


######################################## 资源图片的编辑操作 #############################################


def find_resource_image_paths_by_name(search_root, search_name):
    """
    根据图片的名字查找出资源文件的路径数组
        1) 层级寻找安卓的资源目录
        2) 然后在这些目录中找到被搜索的文件并放置到一个列表中
    :param search_root: 搜索的根路径
    :param search_name: 搜索的文件名 需要包含后缀
    :return: 资源文件的路径数组
    """
    target_file_paths = []
    for root, dirs, files in os.walk(search_root):
        if os.path.split(root)[1] in drawable_picture_dir:
            for file in files:
                if file.decode('utf-8') == search_name:
                    target_file_paths.append(os.path.join(root, file))
    return target_file_paths


def rename_resource_image(search_root, search_name, replace_name):
    """
    重命名资源图片文件
    :param search_root: 搜索的根路径
    :param search_name: 搜索的文件名 需要包含后缀
    :param replace_name: 被替换的名字
    """
    for target_file_path in find_resource_image_paths_by_name(search_root, search_name):
        os.rename(target_file_path, os.path.join(os.path.split(target_file_path)[0], replace_name))


def delete_resource_image(search_root, search_name):
    """
    删除资源图片文件
    :param search_root: 搜索的根路径
    :param search_name: 搜索的文件名 需要包含后缀
    """
    for target_file_path in find_resource_image_paths_by_name(search_root, search_name):
        os.remove(target_file_path)