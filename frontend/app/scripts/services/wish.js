'use strict';

angular.module('frontendApp')
  .factory('$wish', ['$http', '$route', '$rootScope', '$q',
    function ($http, $route, $rootScope, $q) {

      var parseApiUrl = '/api/wishes/parse';

      return {
        parse: function(url) {
          var parseDeffered = $q.defer();

          $http.get(parseApiUrl, {params: {url: url}}).success(function(response) {
            var addaptedData = {
              title: response.title,
              image: response.imageSrc,
              description: response.description
            };

            parseDeffered.resolve(addaptedData);
          });

          return parseDeffered.promise;
        }
      };
    }]);
