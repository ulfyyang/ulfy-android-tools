# -*- coding: UTF-8 -*-
from android_libs import layout, initializer, template


def generate_fragment_file(layout_file_name, fragment_name):
    """生成Fragment代码"""
    view_by_ids_code= '\n    '.join(layout.Layout(layout_file_name).get_view_by_ids().split("\n"))
    template.generate_code_then_write(
        template.PathConfig.runtime_base_fragment,
        initializer.AndroidConfig.generate_config_by_default_config().ui_fragment_path + '/' + fragment_name + 'Fragment.java',
        package_name=initializer.AndroidConfig.get_package_name(), model_name=fragment_name,
        layout_id=layout_file_name.split('.')[0], view_by_ids=view_by_ids_code
    )