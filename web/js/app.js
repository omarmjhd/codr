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

.controller('matchCtrl', ['$scope', '$http', '$sce', function ($scope, $http, $sce) {
    var uid = $sce.trustAsResourceUrl($routeParams.uid);
    $scope.like = function() {
        $http.post('/api/like', {id: uid});
    };

    $scope.reject = function() {
        $http.post('/api/reject', {id: uid});
    };

    $scope.person = $http.get('/api/user?id=' + uid);
    }
}])

.directive('populateProfile', function() {
    return {
        templateUrl: 'templates/match.html';
    }
})