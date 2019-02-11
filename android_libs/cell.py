# -*- coding: UTF-8 -*-
from android_libs import layout, initializer, template


def generate_cell_file(layout_file_name, cell_name):
    """生成cell代码"""
    view_by_ids_code = "\n    ".join(layout.Layout(layout_file_name).get_view_by_ids().split("\n"))
    template.generate_code_then_write(
        template.PathConfig.runtime_cell,
        initializer.AndroidConfig.generate_config_by_default_config().ui_cell_path + '/' + cell_name + 'Cell.java',
        package_name=initializer.AndroidConfig.get_package_name(), layout_id=layout_file_name.split('.')[0],
        model_name=cell_name, view_by_ids=view_by_ids_code
    )


def generate_cm_file(cm_name):
    """生成cm代码"""
    template.generate_code_then_write(
        template.PathConfig.runtime_cm,
        initializer.AndroidConfig.generate_config_by_default_config().application_cm_path + '/' + cm_name + 'CM.java',
        package_name=initializer.AndroidConfig.get_package_name(), model_name=cm_name
    )
