package {{ package_name }}.application.cm;

import com.ulfy.android.mvvm.IView;
import com.ulfy.android.task.LoadDataUiTask;
import com.ulfy.android.utils.LogUtils;
import {{ package_name }}.application.base.BaseCM;
import {{ package_name }}.ui.cell.{{ model_name }}Cell;

public class {{ model_name }}CM extends BaseCM {

    @Override public Class<? extends IView> getViewClass() {
        return {{ model_name }}Cell.class;
    }
}
