'use strict';

angular.module('frontendApp')
  .controller('ItemCtrl', function ($scope) {
    $scope.testItems = [
      "The first choice!",
      "And another choice for you.",
      "but wait! A third!"
    ];
  });
