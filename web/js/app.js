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
            controller: 'profileCtrl'
        })
        .when('/list', {
            templateUrl: 'templates/list.html',
            controller: 'mainCtrl'
        })
        .when('/chat/:uid', {
            templateUrl: 'templates/chat.html',
            controller: 'chatCtrl'
        })
        .otherwise({
            templateUrl: '/404.html'
        });
}])

.controller('mainCtrl', ['$scope', '$http', '$sce', '$routeParams',
    '$location', function ($scope, $http, $sce, $routeParams, $location) {

    // web sockets
    var notes_ws = new WebSocket("ws://codr.cloudapp.net:8888/api/notifications");

    // notifications
    notes_ws.onmessage = function (evt) {
        alert('You matched with ' + evt.data);
    };

    var uid = $sce.trustAsResourceUrl($routeParams.uid);
    $scope.like = function() {
        $http.get('/api/like/' + $scope.person._id)
        .then(function(result) {
            $scope.matched = result.data;
            if ($scope.matched === 'true') {
                // send a web socket alert when you match
                notes_ws.send($scope.person._id);
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
                $scope.profiles();
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
        $scope.matches = [];
        $http.get('/api/matches/')
        .then(function(result) {
            $scope.matches = result.data;
        });
    };

    $scope.go = function(path) {
        $location.path(path);
    };

    // find an initial person
    $scope.find();
}])

.controller('profileCtrl', ['$scope', '$http', '$sce', '$routeParams',
    '$location', function ($scope, $http, $sce, $routeParams, $location) {
    var uid = $sce.trustAsResourceUrl($routeParams.uid);

    $scope.go = function(path) {
        $location.path(path);
    };

    $scope.user = function() {
        $scope.user = {};
        $http.get('/api/profile/' + uid)
        .then(function(result) {
            $scope.user = result.data;
            if ($scope.user) {
                var languages = '';
                var keys = Object.keys($scope.user.languages);
                for (l in keys) {
                    languages = languages.concat(keys[l], ', ');
                }
                $scope.user.languages = languages.substring(
                    0, languages.length - 2);

                // update sample snippet
                $scope.sampleSnippet();
            };
        });
    };

    $scope.sampleSnippet = function() {
        $scope.user.code_snippet = '';
        $http.get('/api/snippet/' + $scope.user._id)
        .then(function(result) {
            $scope.user.code_snippet = result.data;
        });
    };

    $scope.user();
}])

.controller('chatCtrl', ['$scope', '$sce', '$routeParams',
    function ($scope, $sce, $routeParams) {
    var uid = $sce.trustAsResourceUrl($routeParams.uid);

    var chat_ws = new WebSocket("ws://codr.cloudapp.net:8888/api/chat");
    $scope.msgs = []
    chat_ws.onopen = function() {
        //$scope.msgs.push('you are now chatting, say hi!');
        $scope.$apply();
    };
    chat_ws.onmessage = function(evt) {
        console.log(evt);
        $scope.msgs.push(evt);
        $scope.$apply();
    }

    $scope.send = function() {
        chat_ws.send(angular.toJson(
            {'target': uid.toString(), 'msg' : $scope.userMsg})
        );
    }
}]);
