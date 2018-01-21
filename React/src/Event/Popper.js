import React from 'react';

export default class Popper extends React.Component {
    constructor() {
        super();
        this.state = {name: 'Hello world!'};
    }

    //bind方式调用，最后一个参数是事件对象
    preventPop(name, e) {
        e.preventDefault();
        alert(name);
    }

    render() {
        return (
            <div>
                <p>hello</p>
                {/* 用bind方式调用，先传this，再传递其他参数 */}
                <a href="https://reactjs.org" onClick={this.preventPop.bind(this, this.state.name)}>Click</a>
            </div>
        );
    }
}