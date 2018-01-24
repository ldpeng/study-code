import React from 'react';
import ReactDOM from 'react-dom';
//这里可以用 BrowserRouter 或者 HashRouter， 使用 BrowserRouter 浏览器地址栏没有#，但刷新会有问题
import {HashRouter as Router, Link, Route, Switch} from 'react-router-dom';

import Main from './Main';


const Home = () => (
    <div>
        <h2>Home</h2>
    </div>
)

const Always = () => (
    <div>
        <h2>Always</h2>
    </div>
)

const About = () => (
    <div>
        <h2>About</h2>
    </div>
)

const Topic = ({ match }) => (
    <div>
        <h3>{match.params.topicId}</h3>
    </div>
)

const Topics = ({ match }) => (
    <div>
        <h2>Topics</h2>
        <ul>
            <li>
                <Link to={`${match.url}/rendering`}>
                    Rendering with React
                </Link>
            </li>
            <li>
                <Link to={`${match.url}/components`}>
                    Components
                </Link>
            </li>
            <li>
                <Link to={`${match.url}/props-v-state`}>
                    Props v. State
                </Link>
            </li>
        </ul>

        <Route path={`${match.path}/:topicId`} component={Topic}/>
        <Route exact path={match.path} render={() => (
            <h3>Please select a topic.</h3>
        )}/>
    </div>
)

ReactDOM.render(
    (<Router>
        <div>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/about">About</Link></li>
                <li><Link to="/topics">Topics</Link></li>
                <li><Link to="/main">Main</Link></li>
            </ul>

            <hr/>

            {/* Route 中不写path，永远都会显示 */}
            {/*<Route component={Always}/>*/}
            {/*<Route exact path="/" component={Home}/>*/}
            {/*<Route path="/about" component={About}/>*/}
            {/*<Route path="/topics" component={Topics}/>*/}

            <Switch>
                <Route exact path='/' component={Home}/>
                <Route path='/about' component={About}/>
                <Route path="/topics" component={Topics}/>
                <Route path="/main" component={Main}/>
                {/* 在 Switch 中，如果 Route 没有写 path 则在匹配不到其他路劲时显示 */}
                <Route component={Always}/>
            </Switch>
        </div>
    </Router>),
    document.getElementById('root')
);
