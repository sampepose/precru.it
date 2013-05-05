angular.module("services", [])
    .factory("authService", function() {
       return {
           loggedIn : false,
           has_paid: false,
           username:""
       }
    })
    .config(['$httpProvider', function ($httpProvider) {
        var interceptor = ['$location', '$q', "authService", function ($location, $q, authService) {
            return function (promise) {
                return promise.then(function (response) {
                    return response;
                }, function (response) {
                    if (response.status === 403 && !authService.has_paid) {
                        $location.path("/home");
                        //TODO: Open payment modal...
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
    .factory('pingService', ['$http', '$timeout', "$location", function ($http, $timeout, $location) {
        return {
            didInit: false,
            init: function () {
                if (this.didInit)
                    return;

                function timeout() {
                    $http.get("/api/ping/")
                        .success(function (data) {
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