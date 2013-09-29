'use strict';

angular.module('frontendApp')
  .filter('moment', function () {
    return function (input) {
      return moment(input).fromNow();
    };
  });
