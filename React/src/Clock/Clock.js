import React from 'react';

export default class Clock extends React.Component {

    constructor(props) {
        super(props);
        // 构造函数是唯一初始化 state 的地方
        this.state = {date: new Date()};
    }

    /**
     * React 每次渲染组件的时候都会调用这个方法
     */
    render() {
        console.log("render");
        return (
            <div>
                <h1>Clock</h1>
                <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
                {/*父节点可将 state 中的值，传入子节点的 props 中*/}
                <FormattedDate date={this.state.date}/>
            </div>
        );
    }

    /**
     * 生命周期方法
     * 当节点即将挂载到实际DOM时执行
     * 只执行一次
     */
    componentWillMount(){
        console.log("componentWillMount");
    }

    /**
     * 生命周期方法
     * 当节点挂载到实际DOM时执行
     * 只执行一次
     */
    componentDidMount() {
        console.log("componentDidMount");

        //当组件渲染到页面时，启动一个定时器
        this.timerID = setInterval(
            () => {
                //这样写不会报错，但是不会触发页面重新渲染（再次调用render方法）
                //this.state.date = new Date();

                this.setState({
                    date: new Date()
                });
            },
            1000
        );
    }

    /**
     * 当 props 或 state 修改时，React会调用组件这个方法，判断是否需要重新渲染组件
     * 此方法默认返回true，如果重写了这个方法，记得返回true，不然组件永远都不会刷新
     */
    shouldComponentUpdate(){
        console.log("shouldComponentUpdate");
        return true;
    }

    /**
     * 生命周期方法
     * 当节点即将卸载是执行
     * 只执行一次
     */
    componentWillUnmount() {
        console.log("componentWillUnmount");

        //当组件卸载时，取消定时器
        clearInterval(this.timerID);

        //不仅是定时器，这里应该把在组件中注册的事件也取消掉
    }
}

class FormattedDate extends React.Component{

    constructor(props)  {
        super(props);
    }

    render() {
        return <h2>Format date: {this.props.date.toLocaleTimeString()}.</h2>;
    }
}