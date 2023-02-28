odoo.define('qr_generator.qr_systray', function (require) {
    "use strict";
    var core = require('web.core');
    var Widget = require('web.Widget');
    var SystrayMenu = require('web.SystrayMenu');
    var rpc = require('web.rpc')
    var _t = core._t;
    var QWeb = core.qweb
    var QRWidget = Widget.extend({
        // template: 'QRSystray',
        events: {
           "click": "on_click",
           "click #qr_clear": "fn_clear",
           "click #qr_generate": "fn_generate",
       },
       start: function(){
            this.$('#alert').hide();
            this.$('#ItemPreview').hide();
            this.$('#BtnDownload').hide();
        },
       on_click: function (event) {
            if ($(event.target).is('i') === false) {
                event.stopPropagation();
            }
        },
        fn_generate: function() {
            var data = $('#ip_link').val();
            if (data != "") {
                rpc.query({
                model: 'qr.code.generator',
                method: 'generate_qr',
                args: [data]
                }).then(function(result){
                console.log(result)
                    $('#ItemPreview').attr("src","data:image/png;base64," + result);
                    $('#b_download').attr("href","data:image/png;base64," + result);
                    $('#ItemPreview').show();
                    $('#BtnDownload').show();
                });
            }
            else {
                $('#ItemPreview').hide();
                $('#BtnDownload').hide();
            }
        },
       
    });
    SystrayMenu.Items.push(QRWidget);
    return {
        QRWidget: QRWidget,
    };
});
