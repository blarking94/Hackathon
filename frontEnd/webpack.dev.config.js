const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: [
    'babel-polyfill',
    'react-hot-loader/patch',
    'webpack-hot-middleware/client',
    './app/index.jsx'
  ],
  devtool: 'inline-source-map',
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin()
  ],
  resolve: {
    extensions: ['.js', '.jsx']
  },
  module: {
    loaders: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.json?$/, loader: 'json'},
      { test: /\.css$/,use: [ 'style-loader', 'css-loader' ]},
      { test: /\.scss$/, loader: 'style!css!sass?modules&localIdentName=[name]---[local]---[hash:base64:5]'},
      { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "url-loader?limit=10000&minetype=application/font-woff" },
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
