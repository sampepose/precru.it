angular.module("services", [])
    .factory("authService", function() {
       return {
           loggedIn : false
       }
    });