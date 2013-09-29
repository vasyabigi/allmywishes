'use strict';

angular.module('frontendApp')
  .controller('MainCtrl', ['$scope', '$FB', 'Restangular', '_', function ($scope, $FB, Restangular, _) {
    var wishes = Restangular.one('wishes');

    $scope.listView = 'list';

    $FB.api('/me/friends?fields=installed', function (response) {

      var friendsIds = _.pluck(_.filter(response.data, function(item) { return item.installed; }), 'id');

      wishes.getList('discover', {ids: friendsIds}).then(function(response) {
        $scope.wishes = response;
      }, function() {
        console.log('error');
      });

    });

  }]);
