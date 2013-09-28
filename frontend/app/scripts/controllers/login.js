'use strict';

angular.module('frontendApp')
  .controller('LoginCtrl', ['$scope', '$rootScope', '$account', function ($scope, $rootScope, $account) {

    var updateAside = function() {
          $scope.asideShown = $rootScope.account.isAuthenticated;
        };

    $scope.login = function() {
      var accountPromise = $account.login();

      accountPromise.then(function() {
        updateAside();
      });
    };

  }]);
