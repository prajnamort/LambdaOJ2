var path = require('path');
var webpack = require('webpack');

module.exports = {
    devtool: 'inline-source-map',
    entry: [
        'webpack-dev-server/client?http://127.0.0.1:8080/', 'webpack/hot/only-dev-server', './src'
    ],
    output: {
        path: path.resolve(__dirname, 'public'),
        filename: 'bundle.js'
        // , publicPath: path.resolve(__dirname, 'public')
    },
    resolve: {
        modules: [
            'node_modules', 'src', 'src/components', 'styles'
        ],
        extensions: ['.js', '.jsx']
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                use: ['react-hot-loader', 'babel-loader?presets[]=babel-preset-react,presets[]=babel-preset-es2015,presets[]=babel-preset-stage-0']
            }, {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }, {
                test: /\.scss$/,
                use: ['style-loader', 'css-loader', 'sass-loader']
            }, {
                test: /\.less$/,
                use: ['style-loader', 'css-loader', 'less-loader']
            }
        ]
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.ProvidePlugin({$: 'jquery', jQuery: 'jquery'})
    ],
    devServer: {
        hot: true,
        contentBase: path.resolve(__dirname, 'public'),
        publicPath: '/'
    }
};
