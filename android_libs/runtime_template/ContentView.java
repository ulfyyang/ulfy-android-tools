package {{ package_name }}.ui.view;

import android.content.Context;
import android.os.Bundle;
import android.view.View;

import {{ package_name }}.application.vm.ShouyePageVM;
import {{ package_name }}.domain.entity.MovieCategory;
import {{ package_name }}.ui.base.ContentView;
import com.ulfy.android.task.task_extension.transponder.ContentDataLoader;
import com.ulfy.android.task.task_extension.transponder.OnReloadListener;
import com.ulfy.android.utils.TaskUtils;

public class {{ model_name }}ContentView extends ContentView {
    private {{ model_name }}VM vm;
    private {{ model_name }}View view;

    public {{ model_name }}ContentView(Context context) {
        super(context);
        initModel(null);
        initContent(null);
    }

    /**
     * 初始化模型和界面
     */
    private void initModel(Bundle savedInstanceState) {
        vm = new {{ model_name }}VM();
    }

    /**
     * 初始化界面的数据
     */
    private void initContent(final Bundle savedInstanceState) {
        TaskUtils.loadData(getContext(), vm.loadDataOnExe(), new ContentDataLoader(contentFL, vm, false) {
                    @Override protected void onCreatView(ContentDataLoader loader, View createdView) {
                        view = ({{ model_name }}View) createdView;
                    }
                }.setOnReloadListener(new OnReloadListener() {
                    @Override public void onReload() {
                        initContent(savedInstanceState);
                    }
                })
        );
    }
}