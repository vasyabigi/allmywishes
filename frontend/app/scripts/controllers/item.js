'use strict';

angular.module('frontendApp')
  .controller('ItemCtrl', ['$scope', '$rootScope', '$timeout', 'Restangular', function ($scope, $rootScope, $timeout, Restangular) {

    var account = Restangular.one('accounts', $rootScope.account.slug);

    $scope.saveItem = function() {
      account.post('wishes', $scope.item);
      $scope.item = null;
    };

  }]);
