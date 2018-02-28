package cn.ldp.study.redis;

import org.junit.Test;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

/**
 * @author ldp
 * @date 2018/2/28
 */
public class JedisTest {

    @Test
    //获得单一的jedis对象操作数据库
    public void test1() {

        //获得连接对象
        Jedis jedis = new Jedis("127.0.0.1", 6379);

        //存储
        jedis.set("addr", "中山");

        //取数据
        System.out.println(jedis.get("addr"));

        //删除
        System.out.println(jedis.del("addr"));
    }


    //通过jedis的pool获得jedis连接对象
    @Test
    public void test2() {
        //创建池子的配置对象
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        poolConfig.setMaxIdle(30);//最大闲置个数
        poolConfig.setMinIdle(10);//最小闲置个数
        poolConfig.setMaxTotal(50);//最大连接数

        //创建一个redis的连接池
        JedisPool pool = new JedisPool(poolConfig, "127.0.0.1", 6379);

        //从池子中获取redis的连接资源
        Jedis jedis = pool.getResource();

        //操作数据库
        jedis.set("xxx", "yyyy");
        System.out.println(jedis.get("xxx"));

        //删除
        System.out.println(jedis.del("xxx"));

        //关闭资源
        jedis.close();
        pool.close();
    }
}
