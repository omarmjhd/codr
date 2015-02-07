angular.module('codr', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'templates/login.html',
        })
        .when('/match', {
            templateUrl: 'templates/match.html',
            controller: 'mainCtrl'
        })
        .when('/profile/:uid', {
            templateUrl: 'templates/profile.html',
            controller: 'mainCtrl'
        });
}])

.controller('mainCtrl', ['$scope', '$http', '$sce', '$routeParams',
    function ($scope, $http, $sce, $routeParams) {
    var uid = $sce.trustAsResourceUrl($routeParams.uid);
    $scope.like = function() {
        $http.get('/api/like/' + $scope.person._id)
        .then(function(result) {
            $scope.matched = result.data;
            if ($scope.matched === 'true') {
                // send a web socket alert when you matech
                ws.send($scope.person._id);
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
            if ($scope.person) {
                var languages = '';
                var keys = Object.keys($scope.person.languages);
                for (l in keys) {
                    languages = languages.concat(keys[l], ', ');
                }
                $scope.person.languages = languages.substring(
                    0, languages.length - 2);

                // update sample snippet
                $scope.sampleSnippet();
            }
        });
    };

    $scope.sampleSnippet = function() {
        $scope.person.code_snippet = '';
        $http.get('/api/snippet/' + $scope.person._id)
        .then(function(result) {
            $scope.person.code_snippet = result.data;
        });
    };

    $scope.profiles = function() {
        $scope.person.matches = [];
        $http.get('/api/user/' + uid)
        .then(function(result) {
            $scope.person.matches = result.data;
        });
    };

    $scope.go = function(path) {
        $location.path(path);
    };

    // find an initial person
    $scope.find();
}]);
