import React from 'react';
import ReactDOM from 'react-dom';
import jsx_demo from './JSXDemo/JSXDemo';
import Hello from './Hello/Hello';
import Clock from './Clock/Clock';
import Toggle from './Event/Toggle';
import Popper from './Event/Popper';

ReactDOM.render(
    <div>
        {jsx_demo}
        <Hello name="Eagle"/>
        <Clock/>
        <Toggle/>
        <Popper/>
    </div>,
    document.getElementById('root')
);