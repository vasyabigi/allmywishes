'use strict';

angular.module('frontendApp', ['ezfb'])
  .config(['$routeProvider', '$FBProvider', function ($routeProvider, $FBProvider) {
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
      .otherwise({
        redirectTo: '/'
      });
  }]);
