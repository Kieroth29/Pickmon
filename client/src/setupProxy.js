const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'https://kieroth29.xyz:5051',
      changeOrigin: true,
    })
  );
};