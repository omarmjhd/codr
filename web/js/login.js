angular.module('codr', [])

.controller('loginCtrl', function ($scope, $http, $location) {
     $scope.sendRequest = function() {
        var token = $location.search();
        if ("code" in token) {
            $http.post('api/login', {code: token['code']});
            alert('i hate everything');
        }
    };
});