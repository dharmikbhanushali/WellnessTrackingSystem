const {merge} = require('webpack-merge');
const commonConfig = require('./common.config');
const staticUrl = '/static/';

module.exports = merge(commonConfig, {
	mode: 'production',
	devtool: 'source-map',
	bail: true,
	output: {
		publicPath: `${staticUrl}webpack_bundles/`,
	},
});
