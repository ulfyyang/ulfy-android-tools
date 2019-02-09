package {{ package_name }}.ui.base;

import android.content.Context;
import android.util.AttributeSet;

import com.ulfy.android.extra.base.UlfyBaseView;

public abstract class BaseView extends UlfyBaseView {

    public BaseView(Context context) {
        super(context);
    }

    public BaseView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

}
