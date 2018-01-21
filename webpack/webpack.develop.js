const path = require('path');
const merge = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
    //开发环境使用，脚本出错时，控制台可以明确报错原始文件的错误
    devtool: 'inline-source-map',
    //开发环境使用，用于指定webpack-dev-server，的属性
    devServer: {
        //指定从哪个目录读取资源
        contentBase: path.join(__dirname, "out"),
        compress: true,
        port: 9000
    }
});