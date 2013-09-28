'use strict';

angular.module('frontendApp')
  .controller('AsideCtrl', ['$scope', '$rootScope', '$account', '$location', '_', function ($scope, $rootScope, $account, $location, _) {
    $scope.navVert = false;

    $scope.panes = [
      {
        text: 'Discover',
        icon: 'icon-eye-open',
        href: '/discover'
      },
      {
        text: 'New item',
        icon: 'icon-beaker',
        href: '/item'
      }
    ];

    $scope.select = function(pane) {
      angular.forEach($scope.panes, function(pane) {
        pane.selected = false;
      });
      pane.selected = true;
    };

    var initialPane = _.find($scope.panes, function(pane) {
      return $location.path().startsWith(pane.href);
    });

    $scope.selectInitial = function(){
      $scope.select(initialPane || $scope.panes[0]);
    };

    $scope.select(initialPane || $scope.panes[0]);

    var updateAside = function() {
          $scope.asideShown = $rootScope.account.isAuthenticated;
        };

    $scope.logout = function() {
      var accountPromise = $account.logout();

      accountPromise.then(function() {
        updateAside();
      });
    };

  }]);
