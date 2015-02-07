angular.module('codr', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'templates/login.html',
        })
        .when('/match', {
            templateUrl: 'templates/match.html',
            controller: 'matchCtrl'
        })
        .when('/profile/:uid', {
            templateUrl: 'templates/profile.html',
            controller: 'profileCtrl'
        });
}])

.controller('matchCtrl', ['$scope', '$http', '$sce', '$routeParams',
    function ($scope, $http, $sce, $routeParams) {
    var uid = $sce.trustAsResourceUrl($routeParams.uid);
    $scope.like = function() {
        $http.get('/api/like/' + $scope.person._id)
        .then(function(result) {
            $scope.matched = result.data;
            if ($scope.matched === 'true') {
                alert('You matched!');
            }
            // find a new person
            $scope.find();
        });
    };

    $scope.reject = function() {
        $http.get('/api/reject/' + $scope.person._id)
        .then(function(result) {
            // find a new person
            $scope.find();
        });
    };

    $scope.find = function() {
        $scope.person = {};
        $http.get('/api/find')
        .then(function(result) {
            $scope.person = result.data;
        });
    };

    $scope.languages = '';
    console.log($scope.person.languages);
    for (l in $scope.person.languages.keys()) {
        $scope.languages.concat(l);
        $scope.languages.concat(', ');
    }
    $scope.languages = $scope.languages.substring(
        0, $scope.languages.length - 2);

    // find an initial person
    $scope.find();
}])

.controller('profileCtrl', ['$scope', '$http', '$sce', '$routeParams',
    function ($scope, $http, $sce, $routeParams) {
    var uid = $sce.trustAsResourceUrl($routeParams.uid);
    $scope.profiles = function() {
        $scope.matches = [];
        $http.get('/api/user/' + uid)
        .then(function(result) {
            $scope.matches = result.data;
        });
    };
}]);
