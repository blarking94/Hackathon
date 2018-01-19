const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: [
    'babel-polyfill',
    './app/index.jsx'
  ],
  devtool: 'source-map',
  resolve: {
    extensions: ['.js', '.jsx']
  },
  module: {
    loaders: [
      { test: /\.js$/, loader: 'babel-loader', options: { presets: ['env'] }, exclude: /node_modules/ },
      { test: /\.jsx$/, loader: 'babel-loader', options: { presets: ['env'] }, exclude: /node_modules/ },
      { test: /\.json?$/, loader: 'json'},
      { test: /\.css$/,use: [ 'style-loader', 'css-loader' ]},
      { test: /\.scss$/, loader: 'style!css!sass'},
      { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader" },
      { test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader" },
      { test: /\.png$/, loader: "url-loader?mimetype=image/png" }
    ]
  },
  output: {
    filename:'bundle.js',
    path: path.resolve(__dirname, 'public'),
    publicPath: '/'
  },

};
