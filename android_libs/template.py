# -*- coding: UTF-8 -*-
from jinja2 import Environment, FileSystemLoader
import os, codecs, shutil, sys


def generate_code_then_write(template, file_path, **kwargs):
    """根据模板生成代码，并写到文件中"""
    code = generate_code_from_template(template, **kwargs)
    write_code_to_file(code, file_path)


def generate_code_from_template(template, **kwargs):
    """根据模板生成代码"""
    return Environment(loader=FileSystemLoader(get_template_absolute_path())).get_template(template).render(kwargs)


def write_code_to_file(code, file_path):
    """把代码写到文件中"""
    if os.path.exists(file_path):
        print('file exist, skip %s' % file_path)
    else:
        with codecs.open(file_path, 'w', 'utf-8') as code_file:
            code_file.write(code)


def copy_file(source_file, destination_file):
    """ 问价复制 """
    if os.path.exists(destination_file):
        print('file exist, skip %s' % destination_file)
    else:
        shutil.copyfile(source_file, destination_file)


def get_template_absolute_path():
    """获取正在执行的脚本的路径"""
    return sys.path[0] + '/android_libs'


class PathConfig:
    """路径配置类"""

    # 初始化模板配置
    init_template_path = 'init_template'

    init_application_path = init_template_path + '/application'
    init_base_cm = init_application_path + '/BaseCM.java'
    init_base_vm = init_application_path + '/BaseVM.java'

    init_drawable_path = get_template_absolute_path() + '/' + init_template_path + '/drawable'
    init_arrow = init_drawable_path + '/icon_back_arrow_white.png'

    init_layout_path = get_template_absolute_path() + '/' + init_template_path + '/layout'
    init_activity_content = init_layout_path + '/activity_content.xml'
    init_activity_title_content = init_layout_path + '/activity_title_content.xml'
    init_fragment_content = init_layout_path + '/fragment_content.xml'
    init_view_content = init_layout_path + '/view_content.xml'
    init_view_title_normal = init_layout_path + '/view_title_normal.xml'

    init_ui_path = init_template_path + '/ui'
    init_base_activity = init_ui_path + '/BaseActivity.java'
    init_base_cell = init_ui_path + '/BaseCell.java'
    init_base_fragment = init_ui_path + '/BaseFragment.java'
    init_base_view = init_ui_path + '/BaseView.java'
    init_content_activity = init_ui_path + '/ContentActivity.java'
    init_content_fragment = init_ui_path + '/ContentFragment.java'
    init_content_view = init_ui_path + '/ContentView.java'
    init_title_content_activity = init_ui_path + '/TitleContentActivity.java'
    init_web_activity = init_ui_path + '/WebActivity.java'
    init_web_fragment = init_ui_path + '/WebFragment.java'

    init_main_application = init_template_path + '/MainApplication.java'

    # 运行时模板配置
    runtime_template_path = '/runtime_template'

    runtime_base_activity = runtime_template_path + '/BaseActivity.java'
    runtime_base_fragment = runtime_template_path + '/BaseFragment.java'
    runtime_cell = runtime_template_path + '/Cell.java'
    runtime_cm = runtime_template_path + '/Cm.java'
    runtime_content_activity = runtime_template_path + '/ContentActivity.java'
    runtime_content_fragment = runtime_template_path + '/ContentFragment.java'
    runtime_content_view = runtime_template_path + '/ContentView.java'
    runtime_layout_normal = get_template_absolute_path() + '/' + runtime_template_path + '/layout_normal.xml'
    runtime_selector = get_template_absolute_path() + '/' + runtime_template_path + '/selector.xml'
    runtime_shape_circle = get_template_absolute_path() + '/' + runtime_template_path + '/shape_circle.xml'
    runtime_shape_rectangle = get_template_absolute_path() + '/' + runtime_template_path + '/shape_rectangle.xml'
    runtime_title_content_activity = runtime_template_path + '/TitleContentActivity.java'
    runtime_view = runtime_template_path + '/View.java'
    runtime_vm = runtime_template_path + '/Vm.java'

    def __init__(self):
        pass
