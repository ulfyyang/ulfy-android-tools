package {{ package_name }}.ui.cell;

import android.content.Context;
import android.util.AttributeSet;

import com.ulfy.android.mvvm.IViewModel;
import com.ulfy.android.ui_injection.Layout;
import com.ulfy.android.ui_injection.ViewById;
import {{ package_name }}.R;
import {{ package_name }}.application.cm.{{ model_name }}CM;
import {{ package_name }}.ui.base.BaseCell;

@Layout(id = R.layout.{{ layout_id }})
public class {{ model_name }}Cell extends BaseCell {
    {{ view_by_ids }}
    private {{ model_name }}CM cm;

    public {{ model_name }}Cell(Context context) {
        super(context);
        init(context, null);
    }

    public {{ model_name }}Cell(Context context, AttributeSet attrs) {
        super(context, attrs);
        init(context, attrs);
    }

    private void init(Context context, AttributeSet attrs) {

    }

    @Override public void bind(IViewModel model) {
        cm = ({{ model_name }}CM) model;

    }
}
