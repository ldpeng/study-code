import React from 'react';
import jsx_demo from './JSXDemo/JSXDemo';
import Hello from './Hello/Hello';
import Clock from './Clock/Clock';
import Toggle from './Event/Toggle';
import Popper from './Event/Popper';
import LoginControl from './Condition/LoginControl';
import Page from './Condition/Page';
import NumberList from './List/NumberList';
import FormText from './Form/FormText'

export default class React_Demo extends React.Component {
    render() {
        //在jsx前后添加小括号，防止js自动给换行添加分号的bug
        return (
            <div>
                <h1>简单jsx demo</h1>
                {jsx_demo}
                <hr/>

                <h1>父子组件通信</h1>
                <Hello name="Eagle"/>
                <hr/>

                <h1>生命周期</h1>
                <Clock/>
                <hr/>

                <h1>事件触发</h1>
                <Toggle/>
                <Popper/>
                <hr/>

                <h1>条件渲染</h1>
                <LoginControl/>
                <Page/>
                <hr/>

                <h1>列表</h1>
                <NumberList numbers={[1, 2, 3, 4, 5]}/>
                <hr/>

                <h1>表单</h1>
                <FormText/>
                <hr/>
            </div>
        );
    }
}