"use strict";

angular.module("app", ["services", "ui.route", "ui.bootstrap"])
    .config(["$routeProvider", "$locationProvider", function ($routeProvider, $locationProvider) {
      //  $locationProvider.html5Mode(true);
        $routeProvider
            .when("/", {redirectTo: "/home"})
            .when("/home", {templateUrl: "/static/tmplts/home.tmplt.html"})
            .when("/dash", {templateUrl: "/static/tmplts/dash.tmplt.html", controller: "DashCtrl"})
            .when("/myAccount", {templateUrl: "/static/tmplts/myAccount.tmplt.html"})
			.when("/addLead", {templateUrl: "/static/tmplts/addLeads.tmplt.html", controller:"AddLeadsCtrl"});
    }])
    .controller("HeaderCtrl", ["$scope", "$http", "$location", "authService", "pingService",
        function ($scope, $http, $location, authService, pingService) {
            pingService.init();
            $scope.username = authService.username;

            $scope.$on("$routeChangeStart", function (next, current) {
                if (current && current.$$route.templateUrl == "/static/tmplts/home.tmplt.html" && authService.loggedIn) {
                    $location.path("/dash");
                }
            });

            $scope.logout = function () {
                $http.get("/api/logout/")
                    .success(function (data) {
                        $location.path("/home");
                        authService.loggedIn = false;
                    })
                    .error(function (data, status) {
                        //TODO: Error handling...
                    });
            };

            $scope.$watch(function(){return authService.username}, function(n,o) {
                if (n == o)
                    return;
                $scope.username = n;
            })
        }])
    .controller("DashCtrl", ["$scope", "$http", function ($scope, $http) {
        $scope.leads = [];

        $http.get("/api/leads/")
            .success(function (data) {
                $scope.leads = data.results;
            })
            .error(function (data, status) {
                //TODO: Error handling...
            });
    }])
    .controller("AddLeadsCtrl", ["$scope", "$http", function ($scope, $http) {
        $scope.lead = {
            url : ""
        };

        $scope.addLead = function () {
            $http.post("/api/leads/", $scope.lead)//TODO: POST OR GET?
                .success(function (data) {
                    //TODO: Show success
                    $scope.lead.url = "";
                })
                .error(function (data, status) {
                    //TODO: Error handling...
                });
        };

    }])
    .directive("streamItem", function($http) {
        return {
            restrict: "A",
            templateUrl: "/static/tmplts/streamItem.tmplt.html",
            scope : {
                leads: "=",
                lead: "="
            },
            controller: function($scope) {
                $scope.areEventsCollapsed = true;
                $scope.removeLead = function() {
                    $http.delete("/api/leads/" + $scope.lead.id)
                        .success(function (data) {
                            $scope.leads.splice($scope.leads.indexOf($scope.lead), 1);
                        })
                        .error(function (data, status) {
                            //TODO: Error handling...
                        });
                };
            }
        }
    })
    .directive("olarkChat", function () {
        return {
            restrict: "A",
            templateUrl: "/static/tmplts/olark.tmplt.html",
            link:function() {
                window.olark||(function(c){var f=window,d=document,l=f.location.protocol=="https:"?"https:":"http:",z=c.name,r="load";var nt=function(){
                    f[z]=function(){
                        (a.s=a.s||[]).push(arguments)};var a=f[z]._={
                    },q=c.methods.length;while(q--){(function(n){f[z][n]=function(){
                        f[z]("call",n,arguments)}})(c.methods[q])}a.l=c.loader;a.i=nt;a.p={
                        0:+new Date};a.P=function(u){
                        a.p[u]=new Date-a.p[0]};function s(){
                        a.P(r);f[z](r)}f.addEventListener?f.addEventListener(r,s,false):f.attachEvent("on"+r,s);var ld=function(){function p(hd){
                        hd="head";return["<",hd,"></",hd,"><",i,' onl' + 'oad="var d=',g,";d.getElementsByTagName('head')[0].",j,"(d.",h,"('script')).",k,"='",l,"//",a.l,"'",'"',"></",i,">"].join("")}var i="body",m=d[i];if(!m){
                        return setTimeout(ld,100)}a.P(1);var j="appendChild",h="createElement",k="src",n=d[h]("div"),v=n[j](d[h](z)),b=d[h]("iframe"),g="document",e="domain",o;n.style.display="none";m.insertBefore(n,m.firstChild).id=z;b.frameBorder="0";b.id=z+"-loader";if(/MSIE[ ]+6/.test(navigator.userAgent)){
                        b.src="javascript:false"}b.allowTransparency="true";v[j](b);try{
                        b.contentWindow[g].open()}catch(w){
                        c[e]=d[e];o="javascript:var d="+g+".open();d.domain='"+d.domain+"';";b[k]=o+"void(0);"}try{
                        var t=b.contentWindow[g];t.write(p());t.close()}catch(x){
                        b[k]=o+'d.write("'+p().replace(/"/g,String.fromCharCode(92)+'"')+'");d.close();'}a.P(2)};ld()};nt()})({
                    loader: "static.olark.com/jsclient/loader0.js",name:"olark",methods:["configure","extend","declare","identify"]});

                olark.identify('1097-357-10-9238');
            }
        }
    })
    .directive("registerModal", function() {
        return {
            restrict: "A",
            templateUrl: "/static/tmplts/registerModal.tmplt.html"
        }
    })
    .directive("loginModal", function() {
        return {
            restrict: "A",
            templateUrl: "/static/tmplts/loginModal.tmplt.html"
        }
    })
    .directive("paymentModal", function() {
        return {
            restrict: "A",
            templateUrl: "/static/tmplts/paymentModal.tmplt.html"
        }
    })
    .controller("LoginModalCtrl", function($scope, $http, $location, authService) {
        $scope.auth = {
            username: "",
            password: ""
        };

        $scope.open = function () {
            $scope.shouldBeOpen = true;
        };

        $scope.exit = function () {
            $scope.shouldBeOpen = false;
        };

        $scope.login = function () {
            $http.post("/api/login/", {username: $scope.auth.username, password: $scope.auth.password})
                .success(function (data) {
                    authService.username = data.username;
                    authService.loggedIn = true;
                    $location.path("/dash");
                })
                .error(function (data, status) {
                    //TODO: Error handling...
                })
        };

        $scope.opts = {
            backdropFade: true,
            dialogFade: true
        };
    })
    .controller("RegisterModalCtrl", function($scope, $http, $location, $rootScope) {
        $scope.user = {
            first_name: "",
            last_name: "",
            username: "",
            email: "",
            password: "",
            confirmPassword:""

        };

        $scope.open = function () {
            $scope.shouldBeOpen = true;
        };

        $scope.exit = function () {
            $scope.shouldBeOpen = false;
        };

        $scope.register = function () {
            var data = $.extend({}, $scope.user);
            delete data.confirmPassword;

            $http.post("/api/register/", data)
                .success(function (data) {
                    $scope.shouldBeOpen = false;
                    $location.path("/addLead");
                  //TODO: Add later  $rootScope.$broadcast("showPayModal", {message: "Thank you for registering"});
                })
                .error(function (data, status) {
                    //TODO: Error handling...
                })
        };

        $scope.opts = {
            backdropFade: true,
            dialogFade: true
        };
    })
    .controller("PaymentModalCtrl", function($scope, $http, $location, $rootScope, authService) {
        $rootScope.$on("showPayModal", function(scope, data) {
           $scope.message = data.message;
           $scope.open();
        });

        $scope.username = authService.username;

        $scope.open = function () {
            $scope.shouldBeOpen = true;
        };

        $scope.exit = function () {
            $scope.shouldBeOpen = false;
        };

        $scope.opts = {
            backdropFade: true,
            dialogFade: true
        };

        $scope.$watch(function(){return authService.username}, function(n,o) {
            if (n == o)
                return;
            $scope.username = n;
        })
    });