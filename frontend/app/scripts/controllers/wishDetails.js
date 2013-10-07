'use strict';

angular.module('frontendApp')
  .controller('WishDetailsCtrl', ['$scope', '$route', 'Restangular', '$window', function ($scope, $route, Restangular, $window) {
    $scope.pageUrl = $window.location.href;

    var account = Restangular.one('accounts', $route.current.params.slug),
        wish = account.one('wishes', $route.current.params.wishSlug);

    wish.get().then(function(response) {
      $scope.wish = response;
    });

  }]);
