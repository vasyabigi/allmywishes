'use strict';

angular.module('frontendApp')
  .controller('AsideCtrl', ['$scope', '$rootScope', '$account', function ($scope, $rootScope, $account) {
    var accountPromise = $account.getStatus(),
        updateAside = function() {
          $scope.asideShown = $rootScope.user.isAuthenticated;
        };

    accountPromise.then(function() {
      updateAside();
    });

  }]);
