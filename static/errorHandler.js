angular.module("errorHandler", ["alert", "ui.bootstrap", "prAccordion"])
    .factory("errorHandler", ["$injector", function ($injector) {
        return {
            queue: [],
            limitQueue: function () {
                if (this.queue.length >= 3) {
                    this.queue.shift();
                }
            },
            sendToServer: function (type, data, datetime) {
                var $http = $injector.get("$http");
                var postData = {
                    type: type,
                    env: navigator.userAgent,
                    datetime: datetime,
                    data: data
                };
                $http.post("api/error", postData);
            },
            addHTTPError: function (status, method, msg, url, datetime) {
                this.limitQueue();
                this.queue.push({
                    title: "An HTTP error occurred (" + status + ")",
                    type: "error",
                    msgs: [
                        {
                            label: "Message: ",
                            data: msg
                        },
                        {
                            label: "HTTP Method: ",
                            data: method
                        },
                        {
                            label: "URL: ",
                            data: url
                        },
                        {
                            label: "Time: ",
                            data: datetime
                        }
                    ]
                });
                this.sendToServer("HTTP", {method: method, msg: msg, url: url}, datetime);
            },
            addTimeoutError: function (method, url, datetime) {
                this.limitQueue();
                this.queue.push({
                    title: "There was a problem connecting to the server!",
                    type: "error",
                    msgs: [
                        {
                            label: "HTTP Method: ",
                            data: method
                        },
                        {
                            label: "URL: ",
                            data: url
                        },
                        {
                            label: "Time: ",
                            data: datetime
                        }
                    ]
                });
                this.sendToServer("Timeout", {method: method, url: url}, datetime);
            }
        }
    }])
    .directive("errorAlerts", function() {
        return {
            restrict: "A",
            templateUrl: "/static/tmplts/errorAlerts.tmplt.html",
            controller: ["$scope", "errorHandler", function($scope, errorHandler) {
                $scope.$watch(function(){return errorHandler.queue}, function(n, o) {
                    $scope.queue = n;
                }, true);

                $scope.removeAlert = function (i) {
                    errorHandler.queue.splice(i, 1);
                }
            }]
        }
    });