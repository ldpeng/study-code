import React from 'react';

export default class Toggle extends React.Component {
    constructor(props) {
        super(props);
        this.state = {isToggleOn: true};

        //类的方法默认是不会绑定 this 的。如果这里不bind， 当事件触发调用这个函数的时 this 的值会是 undefined。
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {

        //如果需要使用到state 或者 props 的属性来计算出新的值，需要使用函数的方式，不然直接取这两个属性可能不准确
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