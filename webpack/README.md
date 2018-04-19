# 环境搭建

>当前代码使用的是node v8.9.4版本，webpack3

- 全局安装webpack

```
npm install webpack -g
```

- 安装项目依赖

```
npm install webpack --save-dev
```

- 安装 webpack-dev-server 插件

    用于修改文件时，自动编译并刷新浏览器 

```
npm install webpack-dev-server --save-dev
```

# loader

Loader 可以理解为是模块和资源的转换器，它本身是一个函数，接受源文件作为参数，返回转换的结果。这样，我们就可以通过 require 来加载任何类型的模块或文件，比如 CoffeeScript、 JSX、 LESS 或图片。

按照惯例，而非必须，loader 一般以 xxx-loader 的方式命名，xxx 代表了这个 loader 要做的转换功能，比如 json-loader。

在引用 loader 的时候可以使用全名 json-loader，或者使用短名 json。这个命名规则和搜索优先级顺序在 webpack 的 resolveLoader.moduleTemplates api 中定义。

```javascript
Default: ["*-webpack-loader", "*-web-loader", "*-loader", "*"]
```

## css loader

- css相关loader

```
npm install css-loader style-loader --save-dev
```

- 图片处理loader

```
npm install file-loader --save-dev
```

- babel

```
npm install babel-loader babel-core babel-preset-env babel-plugin-syntax-dynamic-import --save-dev  
```

# 插件

插件的执行顺序是依次执行的

- HtmlWebpackPlugin

```
npm install --save-dev html-webpack-plugin
```

- 输出目录清理

```
npm install clean-webpack-plugin --save-dev
```

- 压缩

```
npm install --save-dev uglifyjs-webpack-plugin
```

# 编译

## 使用配置文件

默认情况下，会搜索当前目录的 webpack.develop.js 文件，这个文件是一个 node.js 模块，返回一个 json 格式的配置信息对象，或者通过 --config 选项来指定配置文件。

如果存在 webpack.develop.js 文件，直接在命令行输入 `webpack` 即可完成编译。否则需要指定配置文件如：`webpack --config webpack.publish.config`

## 拆分配置

生产环境与开发环境的配置存在不一致，可以分成两个文件，并将公共配置单独抽出来。通过 `webpack-merge` 合并

```
npm install --save-dev webpack-merge
```

三个文件分别为：

- webpack.common.js
- webpack.develop.js
- webpack.publish.js

## 开发环境

使用 webpack-dev-server 。它将在 localhost:8080 启动一个 express 静态资源 web 服务器，并且会以监听模式自动运行 webpack，在浏览器打开 http://localhost:8080/ 或 http://localhost:8080/webpack-dev-server/ 可以浏览项目中的页面和编译后的资源输出，并且通过一个 socket.io 服务实时监听它们的变化并自动刷新页面。

```
webpack-dev-server --config webpack.develop
```

webpack-dev-server 是对webpack的包装，可以替代webpack命令

## 发布

发布时可在命令中添加 -p 属性，指定压缩输出文件

```
webpack --config webpack.publish.config -p
```

也可以通过配置文件中配置`UglifyJSPlugin`和`webpack.DefinePlugin`。

建议使用配置的方式，可以更灵活

# 注意

Webpack 中涉及路径配置最好使用绝对路径，建议通过 path.resolve(__dirname, "app/folder") 或 path.join(__dirname, "app", "folder") 的方式来配置，以兼容 Windows 环境。