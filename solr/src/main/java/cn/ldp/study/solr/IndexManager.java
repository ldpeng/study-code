package cn.ldp.study.solr;

import org.apache.solr.client.solrj.SolrClient;
import org.apache.solr.client.solrj.SolrQuery;
import org.apache.solr.client.solrj.impl.HttpSolrClient;
import org.apache.solr.client.solrj.response.QueryResponse;
import org.apache.solr.common.SolrDocument;
import org.apache.solr.common.SolrDocumentList;
import org.apache.solr.common.SolrInputDocument;
import org.junit.Test;

import java.util.List;
import java.util.Map;

/**
 * 使用solrj前，需要将solr环境先跑起来
 *
 * @author ldp
 * @date 2018/2/27
 */
public class IndexManager {
    @Test
    public void insertAndUpdateIndex() throws Exception {
        // 单节点
        String url = "http://localhost:8080/solr/core1";
        SolrClient solr = new HttpSolrClient.Builder(url).build();

        // 集群
        //String zkHostString = "zkServerA:2181,zkServerB:2181,zkServerC:2181/solr";
        //SolrClient solr = new CloudSolrClient.Builder().withZkHost(zkHostString).build();

        // 创建Document对象
        SolrInputDocument doc = new SolrInputDocument();
        doc.addField("id", "1");
        doc.addField("name", "孙悟空");
        doc.addField("zz_sik", "赛亚人");
        doc.addField("xt_sik", "超1、超2、超3、超4、超蓝、红蓝、自在极意功");
        doc.addField("jj_sik", "龟派气功、界王拳、龙拳、太阳拳");
        // 将Document对象添加到索引库
        solr.add(doc);

        SolrInputDocument doc1 = new SolrInputDocument();
        doc1.addField("id", "2");
        doc1.addField("name", "贝吉塔");
        doc1.addField("zz_sik", "赛亚人");
        doc1.addField("xt_sik", "超1、超2、超3、超4、超蓝、深蓝");
        doc1.addField("jj_sik", "终极闪光、自爆");
        solr.add(doc1);

        SolrInputDocument doc2 = new SolrInputDocument();
        doc2.addField("id", "3");
        doc2.addField("name", "孙悟饭");
        doc2.addField("zz_sik", "地球人");
        doc2.addField("xt_sik", "超1、超2、神秘");
        doc2.addField("jj_sik", "龟派气功、魔闪光");
        solr.add(doc2);

        solr.commit();
    }

    @Test
    public void search01() throws Exception {
        // 单节点
        String url = "http://localhost:8080/solr/core1";
        SolrClient solr = new HttpSolrClient.Builder(url).build();

        // 创建SolrQuery对象
        SolrQuery query = new SolrQuery();
        // 输入查询条件
        query.setQuery("name:孙");
        // 执行查询并返回结果
        QueryResponse response = solr.query(query);
        // 获取匹配的所有结果
        SolrDocumentList list = response.getResults();
        // 匹配结果总数
        long count = list.getNumFound();
        System.out.println("匹配结果总数:" + count);
        for (SolrDocument doc : list) {
            System.out.println(doc.get("id"));
            System.out.println(doc.get("name"));
            System.out.println(doc.get("zz_sik"));
            System.out.println(doc.get("xt_sik"));
            System.out.println(doc.get("jj_sik"));
            System.out.println("=====================");
        }
    }

    @Test
    public void search02() throws Exception {
        // 单节点
        String url = "http://localhost:8080/solr/core1";
        SolrClient solr = new HttpSolrClient.Builder(url).build();

        // 创建SolrQuery对象
        SolrQuery query = new SolrQuery();

        // 输入查询条件
        // query.setQuery("name:孙");
        query.set("q", "name:孙 AND xt_sik:蓝");

        // 设置过滤条件
        // 如果设置多个过滤条件的话，需要使用query.addFilterQuery(fq)
        //query.setFilterQueries("xt_sik:蓝");

        // 设置排序
        query.setSort("id", SolrQuery.ORDER.desc);
        // 设置分页信息（使用默认的）
        query.setStart(0);
        query.setRows(10);

        // 设置显示的Field的域集合
        query.setFields("id,name,xt_sik");

        // 设置默认域
        query.set("df", "name");

        // 设置高亮信息
        query.setHighlight(true);
        query.addHighlightField("name");
        query.addHighlightField("xt_sik");
        query.setHighlightSimplePre("<em>");
        query.setHighlightSimplePost("</em>");

        // 执行查询并返回结果
        QueryResponse response = solr.query(query);
        // 获取匹配的所有结果
        SolrDocumentList list = response.getResults();
        // 匹配结果总数
        long count = list.getNumFound();
        System.out.println("匹配结果总数:" + count);

        // 获取高亮显示信息
        Map<String, Map<String, List<String>>> highlighting = response.getHighlighting();
        for (SolrDocument doc : list) {
            System.out.println(doc.get("id"));

            List<String> list2 = highlighting.get(doc.get("id")).get("name");
            if (list2 != null)
                System.out.println("名称高亮：" + list2.get(0));
            else {
                System.out.println(doc.get("name"));
            }

            List<String> list3 = highlighting.get(doc.get("id")).get("xt_sik");
            if (list3 != null)
                System.out.println("形态高亮：" + list3.get(0));
            else {
                System.out.println(doc.get("xt_sik"));
            }
            System.out.println("=====================");
        }
    }

    @Test
    public void deleteIndex() throws Exception {
        // 单节点
        String url = "http://localhost:8080/solr/core1";
        SolrClient solr = new HttpSolrClient.Builder(url).build();

        // 根据指定的ID删除索引
        //solr.deleteById("c001");

        // 根据条件删除
        //solr.deleteByQuery("id:c001");

        // 删除全部（慎用）
        solr.deleteByQuery("*:*");

        // 提交
        solr.commit();
    }
}
