odoo.define('event_latest.event_details', function (require) {
"use strict";

var form_widget = require('web.form_widgets');
var core = require('web.core');
var _t = core._t;
var QWeb = core.qweb;

form_widget.WidgetButton.include({
    on_click: function() {
         if(this.node.attrs.custom === "click"){
         console.log("hahaha")
         alert("Hello! I am an alert box!!");

            // YOUR CODE

            return;
         }
         this._super();
    },
});
});
//odoo.define('event_latest.generator', function (require) {
//    "use strict";
//
//    var core = require('web.core');
//    var Widget = require('web.Widget');
//    var SystrayMenu = require('web.SystrayMenu');
//    var rpc = require('web.rpc')
//
//    var _t = core._t;
//    var QWeb = core.qweb
//
//    var QRGeneratorItem = Widget.extend({
//        template:'event_latest.GeneratorItem',
//        events: {
//            "click": "on_click",
//            "click #b_clear": "f_clear",
//            "click #b_short": "f_short",
//        },
//
//        start: function(){
//            this.$('#alert').hide();
//            this.$('#ItemPreview').hide();
//            this.$('#BtnDownload').hide();
//        },
//
//        on_click: function (event) {
//            if ($(event.target).is('i') === false) {
//                event.stopPropagation();
//            }
//        },
//
//        f_short: function() {
//            var data = $('#ip_link').val();
//            if (data != "") {
//                rpc.query({
//                model: 'qr.generator',
//                method: 'get_qr_code',
//                args: [data]
//                }).then(function(result){
//                    document.getElementById("ItemPreview").src = "data:image/png;base64," + result;
//                    document.getElementById("b_download").href = "data:image/png;base64," + result;
//                    $('#ItemPreview').show();
//                    $('#BtnDownload').show();
//                });
//            }
//            else {
//                $('#ItemPreview').hide();
//                $('#BtnDownload').hide();
//            }
//        },
//
//        f_clear: function() {
//            $("#ip_link").val("");
//            $('#ItemPreview').hide();
//            $('#BtnDownload').hide();
//        },
//
//    });
//
//    SystrayMenu.Items.push(QRGeneratorItem);
//
//    return {
//        QRGeneratorItem: QRGeneratorItem,
//    };
//});
