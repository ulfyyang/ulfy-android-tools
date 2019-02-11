# -*- coding: UTF-8 -*-
from android_libs import layout, initializer, template


def generate_view_file(layout_file_name, view_name):
    """生成View代码"""
    view_by_ids_code = "\n    ".join(layout.Layout(layout_file_name).get_view_by_ids().split('\n'))
    template.generate_code_then_write(
        template.PathConfig.runtime_view,
        initializer.AndroidConfig.generate_config_by_default_config().ui_view_path + '/' + view_name + 'View.java',
        package_name=initializer.AndroidConfig.get_package_name(), layout_id=layout_file_name.split('.')[0],
        model_name=view_name, view_by_ids=view_by_ids_code
    )


def generate_vm_file(vm_name):
    """生成VM代码"""
    template.generate_code_then_write(
        template.PathConfig.runtime_vm,
        initializer.AndroidConfig.generate_config_by_default_config().application_vm_path + '/' + vm_name + 'VM.java',
        package_name=initializer.AndroidConfig.get_package_name(), model_name=vm_name
    )