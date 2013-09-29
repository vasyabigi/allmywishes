'use strict';

describe('Controller: NewwishCtrl', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var NewwishCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    NewwishCtrl = $controller('NewwishCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
