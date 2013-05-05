angular.module("services", [])
    .factory("authService", function() {
       return {
           loggedIn : false,
           has_paid: false,
           username:""
       }
    })
    .config(['$httpProvider', function ($httpProvider) {
        var interceptor = ['$location', '$q', "authService", "$rootScope", function ($location, $q, authService, $rootScope) {
            return function (promise) {
                return promise.then(function (response) {
                    return response;
                }, function (response) {
                    if (response.status === 403 && !authService.has_paid && authService.loggedIn) {
                        $location.path("/home");
                       //TODO: Add later $rootScope.$broadcast("showPayModal", {message: "Your subscription has expired"});
                        return response;
                    }
                    if (response.status === 401 || response.status === 403)  {
                        // Forbidden: No access
                        $location.path("/home");
                    }
                    return $q.reject(response);
                });
            }
        }];
        $httpProvider.responseInterceptors.push(interceptor);
    }])
    .factory('pingService', ['$http', '$timeout', "$location", "authService", function ($http, $timeout, $location, authService) {
        return {
            didInit: false,
            init: function () {
                if (this.didInit)
                    return;

                function timeout() {
                    $http.get("/api/ping/")
                        .success(function (data) {
                            if (!authService.username) {
                                authService.username = data.username;
                            }
                            $timeout(timeout, 30000);
                        })
                        .error(function (data, status) {
                            if (status === 401 || status === 403)  {
                                // Forbidden: No access
                                $location.path("/home");
                            }
                        })
                }
                $timeout(timeout, 30000);
                timeout();
                this.didInit = true;
            }
        };
    }]);