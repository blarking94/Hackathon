const express = require('express')
var favicon = require('serve-favicon')
var path = require('path')
var request = require('request')
var postDetails = require('./serverApis/postDetails');

const port = (process.env.PORT || 8087)

const app = express();

app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')))

app.post('/submitDetails', function(req, response) {
      var result = postDetails.postDetails(req.query, function callback(request, res){
        response.send(request)
      });
});

// If we are running in dev mode, use hot reloading
if (process.env.NODE_ENV !== 'production') {
  const webpack = require('webpack');
  const webpackDevMiddleware = require('webpack-dev-middleware');
  const config = require('./webpack.dev.config.js');
  const compiler = webpack(config);

  app.use(webpackDevMiddleware(compiler, {
    publicPath: config.output.publicPath
  }));

  app.use(require("webpack-hot-middleware")(compiler));

  app.get('*', function(req, res) {
    res.sendFile(path.resolve(__dirname, 'public/index.html'));
  });
}

// If we are running in production, use static index.html
if (process.env.NODE_ENV === 'production') {
  app.use(express.static(__dirname + '/public'));
  app.get('*', function(req, res) {
    res.sendFile(path.resolve(__dirname, '/index.html'));
  });
}

app.listen(port, function () { console.log(`Listening at ${port}` );});
