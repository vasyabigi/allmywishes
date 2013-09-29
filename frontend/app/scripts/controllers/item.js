'use strict';

angular.module('frontendApp')
  .controller('ItemCtrl', ['$scope', '$validImg', function ($scope, $validImg) {
    $scope.item = {
      // image: '',
      // title: '',
      // price: ''
    };
    $scope.itemImgUrl = '';

    $scope.$watch('itemImgUrl', function(newVal, oldVal) {
      var validPromise = $validImg.valid(newVal);

      validPromise.then(function(valid) {
        $scope.item.image = valid ? newVal : false;
      });
    });


  }]);
