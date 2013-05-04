"use strict";

angular.module("app", [])
    .config(["$routeProvider", "$locationProvider", function ($routeProvider, $locationProvider) {
      //  $locationProvider.html5Mode(true);
        $routeProvider
            .when("/", {redirectTo: "/dash"})
            .when("/index.html", {redirectTo: "/dash"})
            .when("/dash", {templateUrl: "tmplts/dash.tmplt.html", controller: "DashCtrl"})
            .when("/confirmRegistration", {templateUrl: "tmplts/confirmRegistration.tmplt.html"})
            .when("/addLeads", {templateUrl: "tmplts/addLeads.tmplt.html"});
    }])
    .controller("DashCtrl", ["$scope", function ($scope) {
        $scope.people =
            [
                {
                    name: "Jesse Gray",
                    email: "jesse@gmail.com",
                    imageUrl: "http://www.atmnhs.host22.com/Pictures/silhouette-woman.png",
                    headline: "UX Guru",
                    event: "Changed job position",
                    timestamp: moment().subtract('m', Math.random()*10).fromNow()
                },
                {
                    name: "Sam Pepose",
                    email: "sam@gmail.com",
                    imageUrl: "http://www.atmnhs.host22.com/Pictures/silhouette-woman.png",
                    headline: "Developer",
                    event: "Updated Recommendations",
                    timestamp: moment().subtract('m', Math.random()*10).fromNow()
                }
            ];

        $scope.add = function() {
            $scope.people.push(
                {
                    name: "John Doe",
                    imageUrl: "http://www.atmnhs.host22.com/Pictures/silhouette-woman.png",
                    headline: "Developer",
                    event: "Updated ____",
                    timestamp: moment().subtract('m', Math.random()*10).fromNow()
                }
            );
        };
    }])
    .directive("streamItem", function() {
        return {
            restrict: "A",
            templateUrl: "tmplts/streamItem.tmplt.html",
            scope : {
                people: "=",
                person: "="
            },
            controller: function($scope) {
                $scope.removePerson = function() {
                    $scope.people.splice($scope.people.indexOf($scope.person), 1);
                };
            }
        }
    });