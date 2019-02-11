# -*- coding: UTF-8 -*-

from android_libs import template, initializer


drawable_type = (
    'shape-circle', 'shape-rectangl', 'selector-normal'
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