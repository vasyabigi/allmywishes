'use strict';

angular.module('frontendApp')
  .controller('WishesCtrl', ['$scope', '$rootScope', '$timeout', 'Restangular', function ($scope, $rootScope, $timeout, Restangular) {
    var account = Restangular.one('accounts', $rootScope.account.slug);

    account.getList('wishes').then(function(response) {
      $scope.wishes = response;
    }, function(reason) {
      console.log(reason);
    });

  }]);
