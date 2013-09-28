'use strict';

angular.module('frontendApp')
  .controller('AsideCtrl', ['$scope', '$rootScope', '$account', function ($scope, $rootScope, $account) {
    var accountPromise = $account.getStatus(),
        updateAside = function() {
          $scope.asideShown = $rootScope.account.isAuthenticated;
        };

    accountPromise.then(function() {
      updateAside();
    });

    $scope.login = function() {
      var accountPromise = $account.login();

      accountPromise.then(function() {
        updateAside();
      });
    };

  }]);
