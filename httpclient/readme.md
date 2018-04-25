# 与Spring整合

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:context="http://www.springframework.org/schema/context" xmlns:p="http://www.springframework.org/schema/p"
	xmlns:aop="http://www.springframework.org/schema/aop" xmlns:tx="http://www.springframework.org/schema/tx"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.0.xsd
	http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.0.xsd
	http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-4.0.xsd http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx-4.0.xsd
	http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util-4.0.xsd">

	<!-- 定义连接管理器 -->
	<bean id="httpClientConnectionManager" class="org.apache.http.impl.conn.PoolingHttpClientConnectionManager" destroy-method="close">
		<!-- 设置最大连接数 -->
		<property name="maxTotal" value="${http.maxTotal}" />
		<!-- 设置每个主机地址的并发数 -->
		<property name="defaultMaxPerRoute" value="${http.defaultMaxPerRoute}" />
	</bean>

	<!-- Httpclient构建器 -->
	<bean id="httpClientBuilder" class="org.apache.http.impl.client.HttpClientBuilder">
		<property name="connectionManager" ref="httpClientConnectionManager" />
	</bean>

	<!-- 定义HttpClient对象 -->
	<!-- 
	 class 表示所创建bean的类型
	 factory-bean bean工厂，即具体创建bean逻辑的实例对象
	 factory-method factory-bean对象中，创建bean的方法
	 scope=prototype 表示多例，不配置默认为单利
	 -->
	<bean class="org.apache.http.impl.client.CloseableHttpClient" factory-bean="httpClientBuilder" factory-method="build" scope="prototype" />

    <!--构建请求配置-->
	<bean id="requestConfigBuilder" class="org.apache.http.client.config.RequestConfig.Builder">
		<!-- 创建连接的最长时间 -->
		<property name="connectTimeout" value="${http.connectTimeout}" />
		<!-- 从连接池中获取到连接的最长时间 -->
		<property name="connectionRequestTimeout" value="${http.connectionRequestTimeout}" />
		<!-- 数据传输的最长时间 -->
		<property name="socketTimeout" value="${http.socketTimeout}" />
	</bean>

	<!-- 请求参数对象 -->
	<bean class="org.apache.http.client.config.RequestConfig" factory-bean="requestConfigBuilder" factory-method="build"></bean>
	
	<!-- 定期清理无效连接  -->
	<bean class="com.taotao.common.httpclient.IdleConnectionEvictor" destroy-method="shutdown">
		<constructor-arg index="0" ref="httpClientConnectionManager"/>
	</bean>
</beans>
```

IdleConnectionEvictor代码如下：

```java
public class IdleConnectionEvictor extends Thread {

    private final HttpClientConnectionManager connMgr;

    private volatile boolean shutdown;

    public IdleConnectionEvictor(HttpClientConnectionManager connMgr) {
        this.connMgr = connMgr;
        this.start();//启动当前线程
    }

    @Override
    public void run() {
        try {
            while (!shutdown) {
                synchronized (this) {
                    wait(5000);
                    // 关闭失效的连接
                    connMgr.closeExpiredConnections();
                }
            }
        } catch (InterruptedException ex) {
            // 结束
        }
    }

    public void shutdown() {
        shutdown = true;
        synchronized (this) {
            notifyAll();
        }
    }
}
```
