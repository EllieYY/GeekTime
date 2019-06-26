import org.apache.catalina.Lifecycle;
import org.apache.catalina.LifecycleEvent;
import org.apache.catalina.LifecycleListener;
import org.apache.catalina.Server;

/**
 * @Description :
 * @Author : Ellie
 * @Date : 2019/6/26
 */
public class TestListener implements LifecycleListener {

    @Override
    public void lifecycleEvent(LifecycleEvent event) {

        if (event != null && event.getLifecycle() != null) {
            System.out.println(event.getLifecycle().getStateName() + "ellie");
        }

        if (!(event.getLifecycle() instanceof Server)) {
            return;
        }

        if (!Lifecycle.AFTER_START_EVENT.equals(event.getType())) {
            return;
        }

        Server server = (Server) event.getLifecycle();
    }
}
