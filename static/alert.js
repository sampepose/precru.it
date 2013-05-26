angular.module("alert", [])
    .directive('afAlert', function () {
        return {
            restrict: 'EA',
            template: "<div class='alert' ng-class='type && \"alert-\" + type'>\n" +
             "<button ng-show='closeable' type='button' class='close' ng-click='close()'>&times;</button>\n" +
            "<div ng-transclude></div>\n</div>",
            transclude: true,
            replace: true,
            scope: {
                type: '=',
                close: '&'
            },
            link: function (scope, iElement, iAttrs, controller) {
                scope.closeable = "close" in iAttrs;
            }
        };
    });