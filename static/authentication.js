angular.module("authentication", ["errorHandler"])
    .run(["$http", "authService", function ($http, authService) {
        $http.get("api/ping")
            .success(function (data) {
                if (!authService.username) {
                    authService.username = data.username;
                }
                authService.loggedIn = true;
            })
    }])
    .config(['$httpProvider', function ($httpProvider) {
        var interceptor = ['$q', "$location", "errorHandler", "$injector", function ($q, $location, errorHandler, $injector) {
            return function (promise) {
                return promise.then(function (response) {
                    return response;
                }, function (response) {
                    if (response.config.url == "api/error") {
                        return response;
                    }
                    if (response.status === 0) {
                        errorHandler.addTimeoutError(response.config.method, response.config.url, new Date());
                    } else if (response.status === 401 || response.status === 403) {
                        $location.path("/home");
                    } else {
                        errorHandler.addHTTPError(response.status, response.config.method, response.data.detail, response.config.url, new Date());
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
            showOverlay: true,
            init: function () {
                if (this.didInit)
                    return;

                function timeout() {
                    $http.get("/api/ping/")
                        .success(function (data) {
                            if (!authService.username) {
                                authService.username = data.username;
                            }
                            authService.loggedIn = true;
                            $timeout(timeout, 30000);
                        });
                }
                $timeout(timeout, 30000);
                this.didInit = true;
            }
        };
    }])
    .directive("afOverlay", ["pingService", function (pingService) {
        return {
            restrict: "A",
            template: '<div id="overlay"><ul><li class="li1"></li>' +
                '<li class="li2"></li><li class="li3"></li><li class="li4">' +
                '</li><li class="li5"></li><li class="li6"></li></ul></div>',
            link: function (scope, el) {
                scope.$watch(function () {
                    return pingService.showOverlay
                }, function (n, o) {
                    if (n == o)
                        return;
                    if (!n) {
                        el.delay(1250).fadeOut(500);
                    }
                });
            }
        }
    }]);