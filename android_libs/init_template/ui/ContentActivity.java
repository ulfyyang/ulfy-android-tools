package {{ package_name }}.ui.base;

import android.os.Bundle;
import android.view.View;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import com.ulfy.android.utils.ui_inject.Layout;
import com.ulfy.android.utils.ui_inject.ViewById;
import com.ulfy.android.utils.ui_inject.ViewClick;
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
