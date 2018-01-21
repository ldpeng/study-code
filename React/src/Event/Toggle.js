import React from 'react';

export default class Toggle extends React.Component {
    constructor(props) {
        super(props);
        this.state = {isToggleOn: true};

        //类的方法默认是不会绑定 this 的。如果这里不bind， 当事件触发调用这个函数的时 this 的值会是 undefined。
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {

        //这里需要使用函数的方式重新指定state中的值，因为state类似于Java类的成员变量，在多线程环境下会产生资源竞争
        //这里函数第一个参数是先前的状态（prevState），还有第二个参数是此次更新被应用时的（props）
        this.setState(prevState => ({
            isToggleOn: !prevState.isToggleOn
        }));
    }

    render() {
        return (
            <button onClick={this.handleClick}>
                {this.state.isToggleOn ? 'ON' : 'OFF'}
            </button>
        );
    }
}