angular.module('codr', [])

.controller('loginCtrl', function ($scope, $http, $location) {
     $scope.sendRequest = function() {
        var token = $location.search();
        alert(token['code']);
        if ("code" in token) {
            $http.post('api/login', {code: token['code']});
        }
    };
});