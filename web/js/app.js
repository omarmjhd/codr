angular.module('codr', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'templates/login.html',
        })
        .when('/match/:uid', {
            templateUrl: 'templates/match.html',
            controller: 'matchCtrl'
        });
}])

.controller('matchCtrl', ['$scope', '$http', '$sce', '$routeParams', function ($scope, $http, $sce, $routeParams) {
    var uid = $sce.trustAsResourceUrl($routeParams.uid);
    alert(uid);
    $scope.like = function() {
        $http.post('/api/like', {id: uid});
    };

    $scope.reject = function() {
        $http.post('/api/reject', {id: uid});
    };

    $http.get('/api/user?id=' + uid)
        .success(function(data) {
            $scope.person = data;
            console.log($scope.person);
        })
        .error(function(data, status) {
            console.log(data);
            console.log(status);
        });
}]);