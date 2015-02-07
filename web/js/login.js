angular.module('codr', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'templates/login.html',
            controller: 'loginCtrl'
        });
}])

.controller('loginCtrl', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {
    $scope.sendRequest = function() {
        console.log($routeParams);
        if ('code' in $routeParams) {
        $http.post('api/login', {code: $routeParams['code']});
        }
    };
}]);

/* .controller('loginCtrl', function ($scope, $http, $location) {
     $scope.sendRequest = function() {
        var token = $location.search();
        alert(token['code']);
        if ("code" in token) {
            $http.post('api/login', {code: token['code']});
        }
    };
}); */