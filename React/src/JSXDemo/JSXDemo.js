import React from 'react';

function formatName(user) {
    return user.firstName + ' ' + user.lastName;
}

const user = {
    firstName: 'Harper',
    lastName: 'Perez'
};

// 小括号中的代码已html方式解析，大括号中的代码以js方式解析
// 推荐在最外层添加小括号，防止分号自动插入的bug
const element = (
    <h1>
        Hello, {formatName(user)}!
    </h1>
);

export default element;