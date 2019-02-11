package {{ package_name }}.ui.base;

import android.content.Context;
import android.util.AttributeSet;
import android.widget.FrameLayout;

import {{ package_name }}.R;
import com.ulfy.android.extra.base.UlfyBaseView;
import com.ulfy.android.utils.ui_inject.Layout;
import com.ulfy.android.utils.ui_inject.ViewById;

@Layout(id = R.layout.view_content)
public abstract class ContentView extends UlfyBaseView {

    public ContentView(Context context) {
        super(context);
    }

    public ContentView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    /*
    声明为protected类型，便于子类直接访问
     */
    @ViewById(id = R.id.contentFL) protected FrameLayout contentFL;
}