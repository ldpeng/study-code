const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
    //入口
    entry: {
        //输出多个js文件，指定不同的输入
        app: path.resolve(__dirname, 'src/entry.js'),
        print: path.resolve(__dirname, 'src/print.js'),
        //配置第三方包单独输出一个文件，如react
        // vendor: []
    },
    // 编译之后的输出路径
    output: {
        path: path.resolve(__dirname, 'out'),
        chunkFilename: '[name].bundle.js',
        filename: '[name].bundle.js',
    },
    //模块依赖
    module: {
        rules: [
            {
                test: /\.html$/,
                use: [{
                    loader: 'html-loader',
                    options: {
                        minimize: true
                    }
                }]
            },
            {
                test: /\.js$/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            ["env", {
                                targets: {
                                    chrome: "60"
                                }
                            }]
                        ],
                        //支持import() 函数
                        plugins: ["syntax-dynamic-import"]
                    }
                }
            },
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader'
                ]
            },
            {
                test: /\.(png|svg|jpg|gif)$/,
                use: [{
                    loader: 'file-loader',
                    options: {
                        name: '[name].[ext]',
                        outputPath: 'images/'
                    }
                }]
            }
        ]
    },
    plugins: [
        //每次构建前先清理输出目录
        new CleanWebpackPlugin(['out']),
        //自动创建index.html，注入的相关引用
        new HtmlWebpackPlugin({
            title: 'html file title'
        }),
        //第三方包分离文件配置，放在所有CommonsChunkPlugin的前面
        // new webpack.optimize.CommonsChunkPlugin({
        //     name: 'vendor'
        // }),
        //代码分离工具，防止多个输出文件同时打包了一样的代码
        new webpack.optimize.CommonsChunkPlugin({
            name: 'common' // 指定公共 bundle 的名称。
        })
    ]
}