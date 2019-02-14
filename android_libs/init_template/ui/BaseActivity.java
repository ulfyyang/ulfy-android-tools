package {{ package_name }}.ui.base;

import android.content.pm.ActivityInfo;
import android.os.Bundle;

import com.ulfy.android.extra.base.UlfyBaseActivity;

public abstract class BaseActivity extends UlfyBaseActivity {

    @Override protected void onCreate(Bundle savedInstanceState) {
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        super.onCreate(savedInstanceState);
    }

}

