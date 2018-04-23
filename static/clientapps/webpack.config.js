var webpack = require('webpack');
var path = require('path');

var DIST_DIR = path.normalize(__dirname +"/dist");
var SRC_DIR = path.resolve(__dirname, "src");

var config = {
    entry: {
        'testapp': SRC_DIR + "/testapp.js",
        'base': SRC_DIR + "/base.js",
        'casems': SRC_DIR + "/casems.js",
    },
    output: {
        path: DIST_DIR + "/apps",
        filename: "[name].bundle.js"
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                include: SRC_DIR,
                loader: "babel-loader",
                query: {
                  presets: ["react", "es2015", "stage-2"]
                }
            }
        ]
    }
}

module.exports = config;
