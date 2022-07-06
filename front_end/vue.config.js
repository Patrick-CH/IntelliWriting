const proxyObj = {}
proxyObj['/api'] = {
    target: 'http://124.223.80.199:9000',
    changeOrigin: true,
    ws: true, //是否代理 websockets
    pathRewrite: {
        '^/api': ''
    }
}
module.exports = {
    devServer: {
        host: '0.0.0.0',
        port: 8080,
        proxy: proxyObj
    }
}