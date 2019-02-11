package {{ package_name }};

import android.support.multidex.MultiDexApplication;

import com.ulfy.android.U;
import {{ package_name }}.ui.activity.MainActivity;

public class MainApplication extends MultiDexApplication {

    @Override public void onCreate() {
        super.onCreate();
        U.init(this, MainActivity.class);
    }

}
