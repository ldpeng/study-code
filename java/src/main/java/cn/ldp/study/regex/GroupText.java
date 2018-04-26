package cn.ldp.study.regex;

import org.junit.Test;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author ldp
 * @date 2018/4/26
 */
public class GroupText {

    @Test
    public void test1() {
        Pattern p = Pattern.compile("\\{(\\w+)\\}");
        Matcher m = p.matcher("{year}年{mouth}月");
        while (m.find()) {
            System.out.println("m.group():" + m.group());
            System.out.println("m.group(1):" + m.group(1));
        }
    }

    @Test
    public void test2() {
        Pattern p = Pattern.compile("\\{(\\w+)\\}");
        Matcher m = p.matcher("{year}年{mouth}月");

        Map<String, Object> map = new HashMap<>();
        map.put("year", 2018);
        map.put("mouth", 4);

        StringBuffer sb = new StringBuffer();
        while (m.find()) {
            // 将匹配到的字符串进行替换
            m.appendReplacement(sb, map.get(m.group(1)).toString());
        }
        m.appendTail(sb);
        System.out.println(sb.toString());
    }
}
