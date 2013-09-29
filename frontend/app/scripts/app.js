'use strict';

angular.module('frontendApp', ['ezfb', 'ngRoute', 'restangular', 'ui.bootstrap'])
  .config(['$routeProvider', '$FBProvider', 'RestangularProvider', function ($routeProvider, $FBProvider, RestangularProvider) {


    if (typeof String.prototype.startsWith !== 'function') {
      String.prototype.startsWith = function (str){
        return this.slice(0, str.length) === str;
      };
    }

    $FBProvider.setInitParams({
      appId: '107790869310294'
    });

    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/account', {
        templateUrl: 'views/account.html',
        controller: 'AccountCtrl'
      })
      .when('/item', {
        templateUrl: 'views/item.html',
        controller: 'ItemCtrl'
      })
      .when('/new-wish', {
        templateUrl: 'views/newWish.html',
        controller: 'NewWishCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });

    RestangularProvider.setBaseUrl('/api');

  }]).run(['$http', function($http) {

    // Django csrf token for POST
    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';

  }]);
