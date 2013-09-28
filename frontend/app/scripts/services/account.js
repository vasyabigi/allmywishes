'use strict';

angular.module('frontendApp')
  .factory('$account', ['$http', '$route', '$rootScope', '$q',
    function ($http, $route, $rootScope, $q) {

    var accountInfoUrl = '/api/accounts/info/',
        loginStatusDeferred = $q.defer();

    $rootScope.account = { 'isAuthenticated': false };

    $http.get(accountInfoUrl).success(function(response) {
      $rootScope.account = response;
      loginStatusDeferred.resolve($rootScope.account);
    }).error(function(reason) {
      console.log('Status error', reason);
      loginStatusDeferred.resolve(reason);
    });

    // Public API here
    return {
      getStatus: function() {
        if ($rootScope.account.isAuthenticated) {
          var accountDeferred = $q.defer();
          accountDeferred.resolve($rootScope.account);
          return accountDeferred.promise;
        }

        return loginStatusDeferred.promise;
      },

      login: function() {
        var loginDeferred = $q.defer();

        $rootScope.account = { 'isAuthenticated': true };
        loginDeferred.resolve($rootScope.account);

        return loginDeferred.promise;
      },

      logout: function() {
        var loginDeferred = $q.defer();

        $rootScope.account = { 'isAuthenticated': false };
        loginDeferred.resolve($rootScope.account);

        return loginDeferred.promise;
      }
    };
  }]);
