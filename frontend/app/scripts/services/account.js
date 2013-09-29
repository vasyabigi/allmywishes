'use strict';

angular.module('frontendApp')
  .factory('$account', ['$http', '$route', '$rootScope', '$q', '$FB',
    function ($http, $route, $rootScope, $q, $FB) {

    var accountInfoUrl = '/api/accounts/info',
        connectUrl = '/api/accounts/connect',
        logoutUrl = '/api/accounts/logout',
        loginStatusDeferred = $q.defer();

    $rootScope.account = { 'isAuthenticated': false };

    $http.get(accountInfoUrl).success(function(response) {
      $rootScope.account = response;
      loginStatusDeferred.resolve($rootScope.account);
    }).error(function(reason) {
      console.log('Status error');
      loginStatusDeferred.resolve(reason);
    });

    return {
      getStatus: function() {
        if ($rootScope.account.isAuthenticated) {
          var accountDeferred = $q.defer();
          accountDeferred.resolve($rootScope.account);
          return accountDeferred.promise;
        }

        return loginStatusDeferred.promise;
      },

      login: function () {
        var loginDeferred = $q.defer();

        $FB.login(function (loginResponse) {

          if (loginResponse.status === 'connected') {

            $FB.api('/me', function (meResponse) {
              var userData = {
                oauthToken: loginResponse.authResponse.accessToken,
                expiresIn: loginResponse.authResponse.expiresIn,
                facebookId: loginResponse.authResponse.userID,
                name: meResponse.name,
                email: meResponse.email
              };

              $http.post(connectUrl, userData).success(function(response) {
                $rootScope.account = response;
                loginDeferred.resolve(response);
              }).error(function(reason) {
                loginDeferred.reject(reason);
              });

            });
          } else {
            loginDeferred.reject();
          }

        }, {scope: 'email'});

        return loginDeferred.promise;
      },

      logout: function() {
        var logoutDeffered = $q.defer();

        $http.get(logoutUrl).success(function(response) {
          $rootScope.account = response;
          logoutDeffered.resolve(response);
        });

        return logoutDeffered.promise;
      }

    };
  }]);
