var my_app = angular.module('MyApp').config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
$interpolateProvider.startSymbol('{%');
    $interpolateProvider.endSymbol('%}');
});

