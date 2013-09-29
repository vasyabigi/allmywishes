'use strict';

angular.module('frontendApp', ['ezfb', 'ngRoute', 'restangular', 'ui.bootstrap'])
  .config(['$routeProvider', '$FBProvider', 'RestangularProvider',
    function ($routeProvider, $FBProvider, RestangularProvider) {

    if (typeof String.prototype.startsWith !== 'function') {
      String.prototype.startsWith = function (str){
        return this.slice(0, str.length) === str;
      };
    }

    $FBProvider.setInitParams({
      appId: '@@facebook_id'
    });

    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/wishes/new', {
        templateUrl: 'views/item.html',
        controller: 'ItemCtrl'
      })
      .when('/wishes', {
        templateUrl: 'views/wishes.html',
        controller: 'WishesCtrl'
      })
      .when('/:slug', {
        templateUrl: 'views/account.html',
        controller: 'AccountCtrl'
      })
      .when('/mine/:wishSlug', {
        templateUrl: 'views/myWishDetails.html',
        controller: 'MyWishDetailsCtrl'
      })
      .when('/:slug/wishes/:wishSlug', {
        templateUrl: 'views/wishDetails.html',
        controller: 'WishDetailsCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });

    RestangularProvider.setBaseUrl('/api');

    RestangularProvider.setResponseExtractor(function(response, operation) {
      if (operation === 'getList') {

        // Use results as the return type, and save the result metadata in _resultmeta
        var newResponse = response.results;
        newResponse._resultmeta = {
          'count': response.count,
          'next': response.next,
          'previous': response.previous
        };

        return newResponse;
      }

      return response;
    });

  }]).run(['$http', function($http) {

    // Django csrf token for POST
    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';

  }]);
