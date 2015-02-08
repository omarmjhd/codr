var App = angular.module('Knob', []);
App.controller('myCtrl', function($scope) {
    $scope.dom = '&lt;!DOCTYPE html&gt;&lt;html lang="en"&gt;&lt;/html&gt;'
})

App.directive('prettyprint', function() {
    return {
        restrict: 'C',
        link: function postLink(scope, element, attrs) {
              element.html(prettyPrintOne(scope.dom));
        }
    };
});