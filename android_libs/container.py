# -*- coding: UTF-8 -*-
from android_libs import template, initializer


container_type = (
    'activity-title-content', 'activity-content',
    'view-content'
)


def generate_container_file(container_type, container_name):
    """ 生成容器类文件 """
    if container_type == 'activity-title-content':
        template.generate_code_then_write(
            template.PathConfig.runtime_title_content_activity,
            initializer.AndroidConfig.generate_config_by_default_config().ui_activity_path + '/' + container_name + 'Activity.java',
            package_name=initializer.AndroidConfig.get_package_name(), model_name=container_name
        )
    if container_type == 'activity-content':
        template.generate_code_then_write(
            template.PathConfig.runtime_content_activity,
            initializer.AndroidConfig.generate_config_by_default_config().ui_activity_path + '/' + container_name + 'Activity.java',
            package_name=initializer.AndroidConfig.get_package_name(), model_name=container_name
        )
    if container_type == 'view-content':
        template.generate_code_then_write(
            template.PathConfig.runtime_content_view,
            initializer.AndroidConfig.generate_config_by_default_config().ui_view_path + '/' + container_name + 'ContentView.java',
            package_name=initializer.AndroidConfig.get_package_name(), model_name=container_name
        )
