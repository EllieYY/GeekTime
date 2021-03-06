import org.apache.catalina.WebResourceRoot;
import org.apache.catalina.Wrapper;
import org.apache.catalina.connector.Connector;
import org.apache.catalina.core.StandardContext;
import org.apache.catalina.startup.Tomcat;
import org.apache.catalina.webresources.DirResourceSet;
import org.apache.catalina.webresources.EmptyResourceSet;
import org.apache.catalina.webresources.StandardRoot;
import org.apache.tomcat.util.descriptor.web.FilterDef;
import org.apache.tomcat.util.descriptor.web.FilterMap;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * @Description :
 * @Author : Ellie
 * @Date : 2019/6/24
 */
public class MyTomcat {
    public static void main(String[] args) throws Exception {

        // 创建临时目录作为tomcat的基础目录
        Path tempBaseDir = Files.createTempDirectory("tomcat-temp-base-dir");
        // 创建临时目录作为应用文档资源的目录
        Path tempDocDir = Files.createTempDirectory("tomcat-temp-doc-dir");

        Tomcat tomcat = new Tomcat();
        Connector connector = new Connector();
        // 设置绑定端口
        connector.setPort(8080);
        tomcat.getService().addConnector(connector);
        tomcat.setConnector(connector);
        tomcat.getHost().setAutoDeploy(false);
        tomcat.setBaseDir(tempBaseDir.toFile().getAbsolutePath());

        // 创建应用上下文
        String contextPath = "/ellie";
        StandardContext context = (StandardContext) tomcat.addWebapp(
                contextPath, tempDocDir.toFile().getAbsolutePath());
        context.setParentClassLoader(MyTomcat.class.getClassLoader());
        context.setUseRelativeRedirects(false);

        // 添加servlet
        configureServlets(contextPath, tomcat, context);
        configureResources(context);


        //tomcat 启动jar扫描设置为跳过所有，避免与框架结合出现 jar file not found exception
        System.setProperty("tomcat.util.scan.StandardJarScanFilter.jarsToSkip", "\\,*");

        tomcat.start();
        tomcat.getServer().await();
    }

    private static void configureContextParameters(StandardContext context) {
        context.addParameter("param1", "1");
        context.addParameter("param2", "2");
    }

    private static void configureResources(StandardContext context) {
        String WORK_HOME = System.getProperty("user.dir");
        File classesDir = new File(WORK_HOME, "target/classes");
        File jarDir = new File(WORK_HOME, "lib");
        WebResourceRoot resources = new StandardRoot(context);
        if (classesDir.exists()) {
            resources.addPreResources(new DirResourceSet(resources, "/WEB-INF/classes", classesDir.getAbsolutePath(), "/"));
            System.out.println("Resources added: [classes]");
        } else if (jarDir.exists()) {
            resources.addJarResources(new DirResourceSet(resources, "/WEB-INF/lib", jarDir.getAbsolutePath(), "/"));
            System.out.println("Resources added: [jar]");
        } else {
            resources.addPreResources(new EmptyResourceSet(resources));
            System.out.println("Resources added: [empty]");
        }
        context.setResources(resources);
    }

    private static void configureServlets(String contextPath, Tomcat tomcat, StandardContext context) {
        {
            tomcat.addServlet(contextPath, "test1Name", TestServlet.class.getName());
            //注意不要忘记设置Servlet路径映射
            context.addServletMappingDecoded("/test1Path/*", "test1Name");
        }
        {
            Wrapper wrapper = context.createWrapper();
            wrapper.setName("test2Name");
            wrapper.setServletClass(TestServlet2.class.getName());
            context.addChild(wrapper);
            context.addServletMappingDecoded("/test2Path/*", "test2Name");
        }
    }

    private static void configureFilters(StandardContext context) {
        //Filter定义
        FilterDef filterDef = new FilterDef();
        filterDef.setFilterName("test-filter");
        filterDef.setFilterClass(TestFilter.class.getName());
        filterDef.addInitParameter("name", "test-filter");
        context.addFilterDef(filterDef);
        //Filter路径映射
        FilterMap filterMap = new FilterMap();
        filterMap.setFilterName("test-filter");
        filterMap.addURLPattern("/*");
        context.addFilterMap(filterMap);
    }

    private static void configureListeners(StandardContext context) {
        context.addApplicationEventListener(new TestListener());
    }
}
