'use strict';

angular.module('frontendApp', ['ezfb', 'ngRoute', 'ui.bootstrap'])
  .config(['$routeProvider', '$FBProvider', function ($routeProvider, $FBProvider) {


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
      .otherwise({
        redirectTo: '/'
      });
  }]);
