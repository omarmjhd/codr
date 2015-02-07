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
    $scope.like = function() {
        $http.get('/api/like/' + uid + '/' + $scope.person._id)
        .then(function(result) {
            $scope.matched = result.data;
            if ($scope.matched === 'true') {
                alert('You matched!');
            }
            console.log($scope.matched);
        });
        // find a new person
        $scope.find();
    };

    $scope.reject = function() {
        $http.get('/api/reject/' + uid + '/' + $scope.person._id);
        // find a new person
        $scope.find();
    };

    $scope.find = function() {
        $scope.person = {};
        $http.get('/api/find/' + uid)
        .then(function(result) {
            $scope.person = result.data;
            console.log($scope.person);
        });
    };

    // find an initial person
    $scope.find();
}]);
