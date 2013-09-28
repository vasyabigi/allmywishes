'use strict';

angular.module('frontendApp')
  .controller('AsideCtrl', function ($scope) {
    $scope.navVert = false;

    $scope.testContent = 'Text from ctrl';
  });
