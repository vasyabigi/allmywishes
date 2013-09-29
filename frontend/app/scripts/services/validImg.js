'use strict';

angular.module('frontendApp')
  .factory('$validImg', ['$q', function ($q) {
    return {
      valid : function(url) {
        var image = new Image();

        var imageLoaded = $q.defer();

        image.onload = function() {
          imageLoaded.resolve(true);
        };

        image.onerror = function() {
          imageLoaded.resolve(false);
        };

        image.src = url;

        return imageLoaded.promise;
      }
    };
  }]);
