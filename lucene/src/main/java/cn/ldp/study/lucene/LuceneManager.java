package cn.ldp.study.lucene;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.SortedNumericDocValuesField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.*;
import org.apache.lucene.queryparser.classic.MultiFieldQueryParser;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.*;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.junit.Test;
import org.wltea.analyzer.lucene.IKAnalyzer;

import java.nio.file.Paths;

/**
 * @author ldp
 * @date 2018/2/24
 */
public class LuceneManager {

    public IndexWriter getIndexWriter() throws Exception {
        Directory directory = FSDirectory.open(Paths.get("/Users/ldp/study/study-code/lucene/index"));
        Analyzer analyzer = new IKAnalyzer();
        IndexWriterConfig config = new IndexWriterConfig(analyzer);
        return new IndexWriter(directory, config);
    }

    //全删除
    @Test
    public void testAllDelete() throws Exception {
        IndexWriter indexWriter = getIndexWriter();
        indexWriter.deleteAll();
        indexWriter.close();
    }

    //根据条件删除
    @Test
    public void testDelete() throws Exception {
        IndexWriter indexWriter = getIndexWriter();
        Query query = new TermQuery(new Term("fileName", "apache"));
        indexWriter.deleteDocuments(query);
        indexWriter.close();
    }

    //修改
    @Test
    public void testUpdate() throws Exception {
        IndexWriter indexWriter = getIndexWriter();
        Document doc = new Document();
        doc.add(new TextField("fileN", "测试文件名", Field.Store.YES));
        doc.add(new TextField("fileC", "测试文件内容", Field.Store.YES));
        indexWriter.updateDocument(new Term("fileName", "lucene"), doc);
        indexWriter.close();
    }

    //IndexReader  IndexSearcher
    public IndexSearcher getIndexSearcher() throws Exception {
        Directory directory = FSDirectory.open(Paths.get("/Users/ldp/study/study-code/lucene/index"));// 磁盘
        IndexReader indexReader = DirectoryReader.open(directory);
        return new IndexSearcher(indexReader);
    }

    //执行查询的结果
    public void printResult(IndexSearcher indexSearcher, Query query) throws Exception {
        TopDocs topDocs = indexSearcher.search(query, 10);
        ScoreDoc[] scoreDocs = topDocs.scoreDocs;
        for (ScoreDoc scoreDoc : scoreDocs) {
            int doc = scoreDoc.doc;
            Document document = indexSearcher.doc(doc);
            String fileName = document.get("fileName");
            System.out.println(fileName);
//            String fileContent = document.get("fileContent");
//            System.out.println(fileContent);
            String fileSize = document.get("fileSize");
            System.out.println(fileSize);
            String filePath = document.get("filePath");
            System.out.println(filePath);
            System.out.println("------------");
        }
    }

    //查询所有
    @Test
    public void testMatchAllDocsQuery() throws Exception {
        IndexSearcher indexSearcher = getIndexSearcher();
        Query query = new MatchAllDocsQuery();
        System.out.println(query);
        printResult(indexSearcher, query);
        //关闭资源
        indexSearcher.getIndexReader().close();
    }

    //根据数值范围查询
    @Test
    public void testNumericRangeQuery() throws Exception {
        IndexSearcher indexSearcher = getIndexSearcher();

        Query query = SortedNumericDocValuesField.newSlowRangeQuery("fileSize", 47L, 200L);
        System.out.println(query);
        printResult(indexSearcher, query);
        //关闭资源
        indexSearcher.getIndexReader().close();
    }

    /**
     * “多条件查询”搜索—BooleanQuery
     * BooleanQuery也是实际开发过程中经常使用的一种Query。
     * 它其实是一个组合的Query，在使用时可以把各种Query对象添加进去并标明它们之间的逻辑关系。
     */
    @Test
    public void testBooleanQuery() throws Exception {
        IndexSearcher indexSearcher = getIndexSearcher();

        BooleanQuery.Builder builder = new BooleanQuery.Builder();

        Query query1 = new TermQuery(new Term("fileName", "apache"));
        Query query2 = new TermQuery(new Term("fileName", "lucene"));
        //  select * from user where id =1 or name = 'safdsa'
        // 1．MUST和MUST：取得连个查询子句的交集。
        // 2．MUST和MUST_NOT：表示查询结果中不能包含MUST_NOT所对应得查询子句的检索结果。
        // 3．SHOULD与MUST_NOT：连用时，功能同MUST和MUST_NOT。
        // 4．SHOULD与MUST连用时，结果为MUST子句的检索结果,但是SHOULD可影响排序。
        // 5．SHOULD与SHOULD：表示“或”关系，最终检索结果为所有检索子句的并集。
        // 6．MUST_NOT和MUST_NOT：无意义，检索无结果。
        builder.add(query1, BooleanClause.Occur.MUST);
        builder.add(query2, BooleanClause.Occur.SHOULD);
        printResult(indexSearcher, builder.build());
        //关闭资源
        indexSearcher.getIndexReader().close();
    }

    //条件解释的对象查询
    @Test
    public void testQueryParser() throws Exception {
        IndexSearcher indexSearcher = getIndexSearcher();
        //参数1： 默认查询的域
        //参数2：采用的分析器
        QueryParser queryParser = new QueryParser("fileName", new IKAnalyzer());
        // *:*   域：值
        Query query = queryParser.parse("fileName:lucene is apache OR fileContent:lucene is apache");

        printResult(indexSearcher, query);
        //关闭资源
        indexSearcher.getIndexReader().close();
    }

    //条件解析的对象查询   多个默念域
    @Test
    public void testMultiFieldQueryParser() throws Exception {
        IndexSearcher indexSearcher = getIndexSearcher();

        String[] fields = {"fileName", "fileContent"};
        //参数1： 默认查询的域
        //参数2：采用的分析器
        MultiFieldQueryParser queryParser = new MultiFieldQueryParser(fields, new IKAnalyzer());
        // *:*   域：值
        Query query = queryParser.parse("lucene is apache");

        printResult(indexSearcher, query);
        //关闭资源
        indexSearcher.getIndexReader().close();
    }
}
