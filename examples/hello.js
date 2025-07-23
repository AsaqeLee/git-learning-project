/**
 * Git学习项目 - JavaScript示例文件
 * 这个文件用于演示Git的基本操作
 */

/**
 * 问候函数
 * @param {string} name - 要问候的名字，默认为"World"
 * @returns {string} 问候语
 */
function greet(name = "World") {
    return `Hello, ${name}!`;
}

/**
 * 主函数
 */
function main() {
    console.log(greet());
    console.log(greet("Git学习者"));
    console.log("欢迎来到Git学习项目！");
}

// 如果是在Node.js环境中运行
if (typeof require !== 'undefined' && require.main === module) {
    main();
}

// 导出函数供其他模块使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { greet, main };
}
