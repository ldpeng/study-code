package cn.ldp.study.java8;

public class SubClass /*extends MyClass*/ implements MyFun, MyInterface{

	@Override
	public Integer getValue(Integer num) {
		return null;
	}

	@Override
	public String getName() {
		return MyInterface.super.getName();
	}

}
