import React from 'react';
import {Link, Route, Switch} from 'react-router-dom';

import React_Demo from './React_Demo';
import Hello from './Hello/Hello';
import Clock from './Clock/Clock';
import Toggle from './Event/Toggle';
import Popper from './Event/Popper';
import LoginControl from './Condition/LoginControl';
import Page from './Condition/Page';
import NumberList from './List/NumberList';
import FormText from './Form/FormText'

export default class Main extends React.Component {
    constructor(props) {
        super(props);
        console.log(props);
    }

    render() {
        return (

            <div>
                <h1>React Demo</h1>
                <ul>
                    <li><Link to={`${this.props.match.url}/hello`}>父子组件通信</Link></li>
                    <li><Link to={`${this.props.match.url}/clock`}>生命周期</Link></li>
                    <li><Link to={`${this.props.match.url}/event`}>事件触发</Link></li>
                    <li><Link to={`${this.props.match.url}/condition`}>条件渲染</Link></li>
                    <li><Link to={`${this.props.match.url}/list`}>列表</Link></li>
                    <li><Link to={`${this.props.match.url}/form`}>表单</Link></li>
                    <li><Link to={`${this.props.match.url}/demo`}>非路由方式集成</Link></li>
                </ul>

                <hr/>

                <Switch>
                    <Route exact path={this.props.match.path} render={() => (
                        <h3>选择一个例子</h3>
                    )}/>
                    <Route path={`${this.props.match.url}/hello`} render={(props) => (
                        <Hello name="Eagle"/>
                    )}/>
                    <Route path={`${this.props.match.url}/clock`} component={Clock}/>
                    <Route path={`${this.props.match.url}/event`} render={() => (
                        <div>
                            <Toggle/>
                            <Popper/>
                        </div>
                    )}/>
                    <Route path={`${this.props.match.url}/condition`} render={() => (
                        <div>
                            <LoginControl/>
                            <Page/>
                        </div>
                    )}/>
                    {/* render 可以接受 props 作为参数 */}
                    <Route path={`${this.props.match.url}/list`} render={(props) => (
                        <NumberList numbers={[1, 2, 3, 4, 5]}/>
                    )}/>
                    <Route path={`${this.props.match.url}/form`} component={FormText}/>
                    <Route path={`${this.props.match.url}/demo`} component={React_Demo}/>
                </Switch>
            </div>
        );
    }
}