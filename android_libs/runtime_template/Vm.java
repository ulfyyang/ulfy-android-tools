package {{ package_name }}.application.vm;

import {{ package_name }}.application.base.BaseVM;
import {{ package_name }}.ui.view.{{ model_name }}View;
import com.ulfy.android.model.IView;
import com.ulfy.android.task.task_extension.LoadDataUiTask;

public class {{ model_name }}VM extends BaseVM {

    public LoadDataUiTask.OnExecute loadDataOnExe() {
        return new LoadDataUiTask.OnExecute() {
            public void onExecute(LoadDataUiTask task) {
                try {
                    task.notifyStart("正在加载...");

                    task.notifySuccess("加载完成");
                } catch (Exception e) {
                    e.printStackTrace();
                    task.notifyFail(e);
                }
            }
        };
    }

    @Override public Class<? extends IView> getViewClass() {
        return {{ model_name }}View.class;
    }
}
