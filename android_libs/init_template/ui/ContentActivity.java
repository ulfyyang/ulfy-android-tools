package {{ package_name }}.ui.base;

import android.os.Bundle;
import android.widget.FrameLayout;

import com.ulfy.android.ui_injection.Layout;
import com.ulfy.android.ui_injection.ViewById;
import {{ package_name }}.R;

@Layout(id = R.layout.activity_content)
public class ContentActivity extends BaseActivity {
    /*
    组件全部定义为子类可见，方便操控
     */
    @ViewById(id = R.id.contentFL) protected FrameLayout contentFL;

    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }
}
