# -*- coding: UTF-8 -*-
import initializer
from xml.etree import ElementTree


class ViewType:
    """记录布局文件中的View信息"""

    def __init__(self, id, type):
        self.id = id
        self.type = type


class Layout:
    """表示一个布局文件"""

    find_id_flag = './/*[@{http://schemas.android.com/apk/res/android}id]'
    attr_id_flag = '{http://schemas.android.com/apk/res/android}id'

    def __init__(self, layout_file_name):
        self.layout_file_name = layout_file_name
        self.layout_file_path = initializer.AndroidConfig.generate_config_by_default_config().res_layout_path + '/' + layout_file_name

    def get_view_id_map(self):
        """获取一个布局文件的所有@+id组件，不包括根组件"""
        return [
            ViewType(node.attrib[Layout.attr_id_flag].split('/')[1], node.tag.split('.')[-1])
            for node in filter(lambda x: x.attrib[Layout.attr_id_flag].startswith('@+id/'),
                               ElementTree.parse(self.layout_file_path).findall(Layout.find_id_flag))]

    def get_view_by_ids(self):
        """生成ViewById声明代码"""
        view_by_id_list = [
            '@ViewById(id = R.id.%s) private %s %s;' %
            (view_type.id, view_type.type, view_type.id) for view_type in self.get_view_id_map()
        ]
        return '\n'.join(view_by_id_list)

    def get_single_clicks(self, ids):
        """生成单个单机事件代码"""
        click_template = """
        /**
         * click: %s
         * 
         */
        @ViewClick(ids = {R.id.%s}) private void %s(View v) {
            // Todo
        }
        """
        three_ids = [tuple([id] * 3) for id in ids]
        return '\n'.join([click_template % three_id for three_id in three_ids])

    def get_group_clicks(self, group_name, ids):
        """生成多个view的组单击事件代码"""
        click_template = """
        /**
         * click: %s
         *
         */
        @ViewClick(ids = {%s})
        private void %s(View v) {
            switch (v.getId()) {
%s
                default:
                    break;
            }
        }
        """
        case_template = """                case R.id.%s:
                    break;"""
        ids_top = ', '.join(ids)
        ids_middle = ', '.join(["R.id." + id for id in ids])
        ids_bottom = "\n".join([case_template % id for id in ids])
        return click_template % (ids_top, ids_middle, group_name, ids_bottom)