package {{ package_name }}.ui.base;

import android.content.Context;
import android.util.AttributeSet;

import com.ulfy.android.extra.base.UlfyBaseCell;

public abstract class BaseCell extends UlfyBaseCell {

    public BaseCell(Context context) {
        super(context);
    }

    public BaseCell(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

}
