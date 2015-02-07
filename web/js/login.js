angular.module('codr', [])

.controller('loginCtrl', function ($scope, $http) {
     $scope.sendRequest = function() {
        var token = $location.search()['code'];
        $http.post('api/login', {code: token});
        alert('WORK, YOU SHIT');
    };
});