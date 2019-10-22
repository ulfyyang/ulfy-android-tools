package {{ package_name }}.ui.fragment;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.view.View;

import com.ulfy.android.ui_injection.Layout;
import com.ulfy.android.ui_injection.ViewById;
import {{ package_name }}.R;
import {{ package_name }}.ui.base.BaseFragment;

@Layout(id = R.layout.{{ layout_id }})
public class {{ model_name }}Fragment extends BaseFragment {
    {{ ids }}

    @Override public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        initContent(savedInstanceState);
    }

    private void initContent(final Bundle savedInstanceState) {

    }
}
