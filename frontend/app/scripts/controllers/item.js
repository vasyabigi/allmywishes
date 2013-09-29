'use strict';

angular.module('frontendApp')
  .controller('ItemCtrl', [
    '$scope', '$rootScope', '$timeout',
    'Restangular', '$validImg', '$wish',
    function ($scope, $rootScope, $timeout,
        Restangular, $validImg, $wish) {

      var account = Restangular.one('accounts', $rootScope.account.slug);

      $scope.secondStep = false;
      $scope.item = {
        // image: '',
        // title: '',
        // price: ''
      };

      $scope.saveItem = function() {
        account.post('wishes', $scope.item);
        $scope.item = {};
      };

      $scope.processUrl = function(url){
        var promise = $wish.parse(url);

        promise.then(function(response) {
          $scope.item = response;
        });
      };

      $scope.itemImgUrl = '';

      $scope.$watch('item.image', function(newVal) {
        var validPromise = $validImg.valid(newVal);

        validPromise.then(function(valid) {
          $scope.imageSrc = valid ? newVal : false;
        });
      });

      $scope.dirtyAndInvalid = function(o) {
        return o.$dirty && o.$invalid;
      };

    }]);
