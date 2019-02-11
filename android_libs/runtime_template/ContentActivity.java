package {{ package_name }}.ui.activity;

import android.os.Bundle;
import android.view.View;

import com.ulfy.android.task.task_extension.transponder.ContentDataLoader;
import com.ulfy.android.task.task_extension.transponder.OnReloadListener;
import com.ulfy.android.utils.TaskUtils;
import {{ package_name }}.application.vm.{{ model_name }}VM;
import {{ package_name }}.ui.base.ContentActivity;
import {{ package_name }}.ui.view.{{ model_name }}View;


public class {{ model_name }}Activity extends ContentActivity {
    private {{ model_name }}VM vm;
    private {{ model_name }}View view;

    /**
     * 初始化方法
     */
    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        initModel(savedInstanceState);
        initContent(savedInstanceState);
        initActivity(savedInstanceState);
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
                    protected void onCreatView(ContentDataLoader loader, View createdView) {
                        view = ({{ model_name }}View) createdView;
                    }
                }.setOnReloadListener(new OnReloadListener() {
                    public void onReload() {
                        initContent(savedInstanceState);
                    }
                })
        );
    }

    /**
     * 初始化Activity的数据
     */
    private void initActivity(Bundle savedInstanceState) {

    }

}