'use strict';

angular.module('frontendApp')
  .controller('AccountCtrl', ['$scope', '$route', 'Restangular', function ($scope, $route, Restangular) {

    var account = Restangular.one('accounts', $route.current.params.slug);

    account.get().then(function(response) {
      $scope.currentAccount = response;
      console.log(response);
    });

  }]);
