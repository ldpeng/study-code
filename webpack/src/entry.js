import './style.css';
import printMe from './print.js';

document.write('It works.')

//Webpack 会给每个模块分配一个唯一的 id 并通过这个 id 索引和访问模块。在页面启动时，会先执行 entry.js 中的代码，其它模块会在运行 require 的时候再执行。
document.write(require('./module.js')) // 添加模块

let btn = document.createElement('button');
btn.innerHTML = 'Click me and check the console!';

btn.onclick = printMe;
document.body.appendChild(btn);

let big = document.createElement('img');
big.setAttribute("id", "big");
document.body.appendChild(big);

let small = document.createElement('img');
small.setAttribute("id", "small");
document.body.appendChild(small);

var br = document.createElement('br');
document.body.appendChild(br);

let btn_lazy = document.createElement('button');
btn_lazy.innerHTML = 'btn_lazy';
document.body.appendChild(btn_lazy);

//懒加载
btn_lazy.onclick = e => import(/* webpackChunkName: "lazy" */ './lazyload').then(module => {
    var f = module.default;
    f();
});