'use strict';

angular.module('frontendApp')
  .factory('$account', ['$http', '$route', '$rootScope', '$q',
    function ($http, $route, $rootScope, $q) {

    var accountInfoUrl = '/api/accounts/info/',
        loginStatusDeferred = $q.defer();

    $rootScope.user = { 'isAuthenticated': false };

    $http.get(accountInfoUrl).success(function(response) {
      $rootScope.user = response;
      loginStatusDeferred.resolve($rootScope.user);
    }).error(function(reason) {
      console.log('Status error', reason);
      loginStatusDeferred.resolve(reason);
    });

    // Public API here
    return {
      getStatus: function() {
        return loginStatusDeferred.promise;
      }
    };
  }]);
