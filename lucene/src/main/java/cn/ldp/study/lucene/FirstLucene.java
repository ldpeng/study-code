package cn.ldp.study.lucene;

import org.apache.commons.io.FileUtils;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.document.*;
import org.apache.lucene.index.*;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.junit.Test;
import org.wltea.analyzer.lucene.IKAnalyzer;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.Arrays;

/**
 * Lucene 入门 创建索引 查询索引
 *
 * @author ldp
 * @date 2018/2/24
 */
public class FirstLucene {
    // 创建索引
    @Test
    public void testIndex() throws Exception {

        // 指定索引库的存放位置Directory对象
        Directory directory = FSDirectory.open(Paths.get("/Users/ldp/study/study-code/lucene/index"));
        // Directory directory = new RAMDirectory();//保存索引到内存中 （内存索引库）

//        Analyzer analyzer = new StandardAnalyzer();// 官方推荐

        // 第三方中文分析器
        // 需要 IKAnalyzer.cfg.xml 配置文件 进行扩展
        Analyzer analyzer = new IKAnalyzer();

        // 指定一个分析器，对文档内容进行分析。
        IndexWriterConfig config = new IndexWriterConfig(analyzer);

        //创建一个indexwriter对象。
        IndexWriter indexWriter = new IndexWriter(directory, config);

        File f = new File("/Users/ldp/study/study-code/lucene/searchsource");
        File[] listFiles = f.listFiles();
        for (File file : listFiles) {
            // 创建document对象。
            Document document = new Document();
            // 创建field对象，将field添加到document对象中。
            // 文件名称
            String file_name = file.getName();
            Field fileNameField = new TextField("fileName", file_name, Field.Store.YES);
            // 文件大小
            long file_size = FileUtils.sizeOf(file);
            Field fileSizeField = new SortedNumericDocValuesField("fileSize", file_size);
            // 文件路径
            String file_path = file.getPath();
            Field filePathField = new StoredField("filePath", file_path);
            // 文件内容
            String file_content = FileUtils.readFileToString(file, "utf-8");
            Field fileContentField = new TextField("fileContent", file_content, Field.Store.YES);

            document.add(fileNameField);
            document.add(fileSizeField);
            document.add(filePathField);
            document.add(fileContentField);
            // 使用indexwriter对象将document对象写入索引库，此过程进行索引创建。并将索引和document对象写入索引库。
            indexWriter.addDocument(document);
        }

        // 关闭IndexWriter对象。
        indexWriter.close();
    }

    // 搜索索引
    @Test
    public void testSearch() throws Exception {
        // 创建一个Directory对象，也就是索引库存放的位置。
        Directory directory = FSDirectory.open(Paths.get("/Users/ldp/study/study-code/lucene/index"));// 磁盘

        // 创建一个indexReader对象，需要指定Directory对象。
        IndexReader indexReader = DirectoryReader.open(directory);

        // 创建一个indexsearcher对象，需要指定IndexReader对象
        IndexSearcher indexSearcher = new IndexSearcher(indexReader);

        // 对特定项搜索
        // 按词条搜索—TermQuery
        // TermQuery是最简单、也是最常用的Query。TermQuery可以理解成为“词条搜索”，
        // 在搜索引擎中最基本的搜索就是在索引中搜索某一词条，而TermQuery就是用来完成这项工作的。
        // 在Lucene中词条是最基本的搜索单位，从本质上来讲一个词条其实就是一个名/值对。
        // 只不过这个“名”是字段名，而“值”则表示字段中所包含的某个关键字。

        // 创建一个TermQuery对象，指定查询的域和查询的关键词。
        Query query = new TermQuery(new Term("fileName", "lucene"));//精准匹配

        // 执行查询。
        TopDocs topDocs = indexSearcher.search(query, 10);

        // 返回查询结果。遍历查询结果并输出。
        Arrays.stream(topDocs.scoreDocs).forEach(scoreDoc -> {
            try {
                int doc = scoreDoc.doc;
                Document document = indexSearcher.doc(doc);
                // 文件名称
                String fileName = document.get("fileName");
                System.out.println(fileName);
                // 文件内容
//                String fileContent = document.get("fileContent");
//                System.out.println(fileContent);
                // 文件大小
                String fileSize = document.get("fileSize");
                System.out.println(fileSize);
                // 文件路径
                String filePath = document.get("filePath");
                System.out.println(filePath);
                System.out.println("------------");
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        // 关闭IndexReader对象
        indexReader.close();
    }
}
