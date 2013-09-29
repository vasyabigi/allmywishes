'use strict';

angular.module('frontendApp')
  .controller('WishDetailsCtrl', ['$scope', '$route', 'Restangular', function ($scope, $route, Restangular) {
    var account = Restangular.one('accounts', $route.params.slug),
        wish = account.one('wishes', $route.params.wishSlug);

    wish.get().then(function(response) {
      console.log(response);
    });

  }]);
