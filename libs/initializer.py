# -*- coding: UTF-8 -*-
import os, ConfigParser
from template import template


class AndroidConfig:
    """初始化配置，一个Model一个份配置"""

    @staticmethod
    def generate_config_by_default_config():
        if not os.path.exists(AndroidConfig.get_config_file_path()):
            raise Exception('config file does not exist')
        else:
            return AndroidConfig()

    @staticmethod
    def get_layout_file_names_if_config_exist():
        """如果存在配置文件则返回布局文件名列表"""
        if os.path.exists(AndroidConfig.get_config_file_path()):
            return AndroidConfig().get_layout_file_names()
        else:
            return []

    @staticmethod
    def get_model_path():
        """获取当前模块的路径，因为命令会在当前模块下运行"""
        return os.getcwdu()

    @staticmethod
    def get_config_file_path():
        """获取当前模块下的配置文件路径"""
        return os.getcwdu() + '/' + '.android.cfg'

    @staticmethod
    def get_package_name():
        if not os.path.exists(AndroidConfig.get_config_file_path()):
            raise Exception('config file does not exist')
        else:
            config_parser = ConfigParser.RawConfigParser()
            config_parser.read(AndroidConfig.get_config_file_path())
            return config_parser.get('base', 'package_name')

    @staticmethod
    def init_android_config(package_name):
        config_parser = ConfigParser.RawConfigParser()
        config_parser.add_section('base')
        config_parser.set('base', 'package_name', package_name)
        with open(AndroidConfig.get_config_file_path(), 'wb') as config_file:
            config_parser.write(config_file)

    def __init__(self):
        # 基础路径
        self.model_path = AndroidConfig.get_model_path()
        self.package_name = AndroidConfig.get_package_name()
        self.code_path = self.model_path + '/src/main' + '/java/' + '/'.join(self.package_name.split('.'))
        self.res_path = self.model_path + '/src/main' + '/res'
        # ui路径
        self.ui_base_path = self.code_path + '/ui/base'
        self.ui_activity_path = self.code_path + '/ui/activity'
        self.ui_fragment_path = self.code_path + '/ui/fragment'
        self.ui_view_path = self.code_path + '/ui/view'
        self.ui_cell_path = self.code_path + '/ui/cell'
        self.ui_globle_path = self.code_path + '/ui/globle_event'
        # application路径
        self.application_base_path = self.code_path + '/application/base'
        self.application_vm_path = self.code_path + '/application/vm'
        self.application_cm_path = self.code_path + '/application/cm'
        # domain路径
        self.domain_entities_path = self.code_path + '/domain/entity'
        self.domain_repository_path = self.code_path + '/domain/repository'
        # infrastructure路径
        self.infrastructure_path = self.code_path + '/infrastructure'
        # res路径
        self.res_color = self.res_path + '/color'
        self.res_drawable_path = self.res_path + '/drawable'
        self.res_drawable_lpath = self.res_path + '/drawable-ldpi'
        self.res_drawable_mpath = self.res_path + '/drawable-mdpi'
        self.res_drawable_hpath = self.res_path + '/drawable-hdpi'
        self.res_drawable_xpath = self.res_path + '/drawable-xhdpi'
        self.res_drawable_xxpath = self.res_path + '/drawable-xxhdpi'
        self.res_drawable_xxxpath = self.res_path + '/drawable-xxxhdpi'
        self.res_layout_path = self.res_path + '/layout'
        self.res_values_path = self.res_path + '/values'

    def init_standard_directory(self):
        """
        根据配置文件生成标准目录结构
        """
        directory_paths = (
            # ui 层
            self.ui_base_path, self.ui_activity_path, self.ui_fragment_path,
            self.ui_view_path, self.ui_cell_path, self.ui_globle_path,
            #  application 层
            self.application_base_path, self.application_vm_path, self.application_cm_path,
            # domain 层
            self.domain_entities_path, self.domain_repository_path,
            # infrastructure 层
            self.infrastructure_path,
            # res
            self.res_color, self.res_drawable_path, self.res_drawable_lpath, self.res_drawable_mpath,
            self.res_drawable_hpath, self.res_drawable_xpath, self.res_drawable_xxpath,
            self.res_drawable_xxxpath, self.res_layout_path, self.res_values_path
        )
        for directory_path in directory_paths:
            if os.path.exists(directory_path):
                print("directory exist, skip: %s" % directory_path)
            else:
                os.makedirs(directory_path)

    def init_standard_file(self):
        """
        根据配置文件初始化基本文件
        """
        # application
        application_files = {
            template.PathConfig.init_base_cm: 'BaseCM.java',
            template.PathConfig.init_base_vm: 'BaseVM.java'
        }
        for application_template, application_file_name in application_files.items():
            template.generate_code_then_write(
                application_template, self.application_base_path + '/' + application_file_name,
                package_name=AndroidConfig.get_package_name()
            )
        # drawable
        drawable_files = {
            template.PathConfig.init_arrow: 'white_back_arrow.png'
        }
        for drawable_file_template, drawable_file_name in drawable_files.items():
            template.copy_file(drawable_file_template, self.res_drawable_xpath + '/' + drawable_file_name)
        # layout
        layout_files = {
            template.PathConfig.init_activity_content: 'activity_content.xml',
            template.PathConfig.init_activity_title_content: 'activity_title_content.xml',
            template.PathConfig.init_fragment_content: 'fragment_content.xml',
            template.PathConfig.init_view_content: 'view_content.xml',
            template.PathConfig.init_view_title_normal: 'view_title_normal.xml'
        }
        for layout_file_template, layout_file_name in layout_files.items():
            template.copy_file(layout_file_template, self.res_layout_path + '/' + layout_file_name)
        # ui
        ui_files = {
            template.PathConfig.init_base_activity: 'BaseActivity.java',
            template.PathConfig.init_base_cell: 'BaseCell.java',
            template.PathConfig.init_base_fragment: 'BaseFragment.java',
            template.PathConfig.init_base_view: 'BaseView.java',
            template.PathConfig.init_content_activity: 'ContentActivity.java',
            template.PathConfig.init_content_fragment: 'ContentFragment.java',
            template.PathConfig.init_content_view: 'ContentView.java',
            template.PathConfig.init_title_content_activity: 'TitleContentActivity.java',
            template.PathConfig.init_web_activity: 'WebActivity.java',
            template.PathConfig.init_web_fragment: 'WebFragment.java'
        }
        for ui_file_template, ui_file_name in ui_files.items():
            template.generate_code_then_write(
                ui_file_template, self.ui_base_path + '/' + ui_file_name,
                package_name=AndroidConfig.get_package_name()
            )
        # MainApplication
        template.generate_code_then_write(
            template.PathConfig.init_main_application, self.code_path + '/' + 'MainApplication.java', package_name=AndroidConfig.get_package_name()
        )

    def get_layout_file_names(self):
        """获取布局文件列表"""
        return os.listdir(self.res_layout_path)