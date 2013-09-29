'use strict';

angular.module('frontendApp')
  .controller('ItemCtrl', ['$scope', '$rootScope', '$timeout', 'Restangular', '$validImg',
    function ($scope, $rootScope, $timeout, Restangular, $validImg) {

      var account = Restangular.one('accounts', $rootScope.account.slug);

      $scope.item = {
        // image: '',
        // title: '',
        // price: ''
      };

      $scope.saveItem = function() {
        account.post('wishes', $scope.item);
        $scope.item = {};
      };

      $scope.itemImgUrl = '';

      $scope.$watch('itemImgUrl', function(newVal) {
        var validPromise = $validImg.valid(newVal);

        validPromise.then(function(valid) {
          $scope.item.image = valid ? newVal : false;
        });
      });

      $scope.dirtyAndInvalid = function(o) {
        return o.$dirty && o.$invalid;
      };

    }]);
