odoo.define("event_latest.event_details", function (require) {
  "use strict";
  var core = require("web.core");
  var Widget = require("web.Widget");
  console.log("aaaaa");

   $(document).on("mouseover", "#popover", function (event) {
//$(document).ready(function(event) {
console.log("start");
    var self = this;
//    console.log("sssss", event);
//    console.log("11", self.parentElement.parentElement);
    var item_text = "";
//    console.log("event.target.parentElement.children", event.target);
    if (self.parentElement.parentElement.children[3]) {
//      console.log("1111", self.parentElement.children);
      item_text =
        "Name : "+ self.parentElement.parentElement.children[1].outerText +"<br/>"+
        "Start Date : "+ self.parentElement.parentElement.children[2].outerText +"<br/>"+
        "End Date : "+ self.parentElement.parentElement.children[3].outerText +"<br/>"+
        "Organizer : "+ self.parentElement.parentElement.children[4].outerText +"<br/>"+
        "Responsible : "+ self.parentElement.parentElement.children[5].outerText;
    }

    $(this).popover({
      html: true,
      placement: "right",
      trigger: "hover",
      title: "Event Details",
      content: "<span>" + item_text + "</span>",
    });

//    console.log("test1");
    //   $('[data-toggle="popover"]').popover();
  });
});
