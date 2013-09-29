'use strict';

angular.module('frontendApp')
  .controller('MyWishDetailsCtrl', ['$scope', '$route', 'Restangular', function ($scope, $route, Restangular) {
    var wish = Restangular.one('wishes/mine', $route.current.params.wishSlug);
    wish.get().then(function(response) {
      $scope.wish = response;
    });

  }]);
