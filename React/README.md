# 环境构建

## 构建webpack环境

安装webpack本地依赖

```
npm install webpack webpack-dev-server webpack-merge --save-dev
```

安装样式、图片处理loader、babel相关loader、优化插件。具体参考webpack学习项目

```
npm install css-loader style-loader file-loader  --save-dev
npm install babel-loader babel-core babel-preset-env babel-plugin-syntax-dynamic-import --save-dev
npm install html-webpack-plugin clean-webpack-plugin uglifyjs-webpack-plugin --save-dev
```

创建webpack配置文件

- webpack.common.js
- webpack.develop.js
- webpack.publish.js

## 添加react依赖

```
npm install --save react react-dom
```

添加babel对react的支持

```
npm install --save-dev babel-preset-react
```

# 路由

## react-router

```
npm install --save react-router-dom
```