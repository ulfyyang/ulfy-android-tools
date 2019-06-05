package {{ package_name }}.application.cm;

import {{ package_name }}.application.base.BaseCM;
import {{ package_name }}.ui.cell.{{ model_name }}Cell;
import com.ulfy.android.model.IView;
import com.ulfy.android.task.task_extension.LoadDataUiTask;

public class {{ model_name }}CM extends BaseCM {

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
        return {{ model_name }}Cell.class;
    }
}
