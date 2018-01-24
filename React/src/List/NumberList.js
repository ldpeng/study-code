import React from 'react';
import ListItem from './ListItem'

export default class NumberList extends React.Component {
    render() {
        return (
            <ul>
                {this.props.numbers.map((number) =>
                    //列表项需要有一个唯一的key值，用来判断增删改查
                    //key 应该设置在实际被循环的元素上
                    //key ListItem 中不能通过 props.key 获取 key 中的值，key只作为列表的唯一标识，如果要获取key的值，这里需要再定义一个属性，用相同的值传过去
                    <ListItem key={number.toString()} id={number.toString()} value={number}/>
                )}
            </ul>);
    }
}