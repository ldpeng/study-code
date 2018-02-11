package cn.ldp.study.java8;

public interface MyFun {

	Integer getValue(Integer num);
	
	default String getName(){
		return "哈哈哈";
	}

}
