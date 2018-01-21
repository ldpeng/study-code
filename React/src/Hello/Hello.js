import React from 'react';

export default class Hello extends React.Component {
    render(){
        // 通过 props 获取属性传过来的值
        // props 只用于读取，规范上不建议内部去修改它
        return <h1>Hello, {this.props.name}</h1>;
    }
}