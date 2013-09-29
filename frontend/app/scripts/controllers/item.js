'use strict';

angular.module('frontendApp')
  .controller('ItemCtrl', ['$scope', '$rootScope', '$location', 'Restangular', '$validImg', '$wish',
    function ($scope, $rootScope, $location, Restangular, $validImg, $wish) {

      var account = Restangular.one('accounts', $rootScope.account.slug);

      $scope.secondStep = false;
      $scope.urlInProgress = false;
      $scope.imageSrc = '';
      $scope.item = {};

      $scope.saveItem = function() {
        account.post('wishes', $scope.item);
        $scope.item = {};
        $location.path('/wishes');
      };

      $scope.processUrl = function(url){
        $scope.urlInProgress = true;
        var promise = $wish.parse(url);

        promise.then(function(response) {
          $scope.item = response;
          $scope.secondStep = true;
          $scope.urlInProgress = false;
        });
      };

      $scope.$watch('item.image', function(newVal) {
        if (newVal !== undefined) {
          var validPromise = $validImg.valid(newVal);

          validPromise.then(function(valid) {
            $scope.imageSrc = valid ? newVal : false;
          });
        }
      });

      $scope.dirtyAndInvalid = function(o) {
        return o.$dirty && o.$invalid;
      };

    }]);
