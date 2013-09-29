'use strict';

angular.module('frontendApp')
  .controller('WishesCtrl', ['$scope', '$rootScope', '$timeout', 'Restangular', function ($scope, $rootScope, $timeout, Restangular) {

    $scope.listView = 'list';

    var wishes = Restangular.one('wishes');

    wishes.getList('mine').then(function(response) {
      $scope.wishes = response;
    }, function() {
      console.log('error');
    });

    $scope.edit = function() {
      console.log('editing');
    };

    $scope.remove = function(index, wish) {
      wish.remove().then(function() {
        $scope.wishes.splice(index, 1);
      });
    };

  }]);
