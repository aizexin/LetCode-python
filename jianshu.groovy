// ==UserScript==
// @name         简书广告屏蔽
// @namespace    http://tampermonkey.net/
// @version      0.0.1
// @require      https://greasyfork.org/scripts/415668-zmquery3-5-1/code/zmQuery351.js?version=866815
// @description 【功能有】屏蔽简书夜游广告
// @author       aizexin
// @match        *://*.jianshu.com/p/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    function removeAlertRule3() {
        $$$("div[style]").each(function (index) {
            let attr = $$$(this).attr('style');
            let intZIndex = parseInt(attr.indexOf("z-index"))
            console.log('intZIndex--->',intZIndex)
            if (intZIndex > 10) {
                console.log('attr--->',attr)
                $$$(this).remove();
                $$$('body').css("overflow", 'auto');
            }

        })
    }

    var $$$ = $ || window._$ || zmQuery;
    var href = window.location.href

     if (href.indexOf('jianshu.com') != -1) { //jianshu.com
         let interval = setInterval(function () {
            // console.log("轮训检测...jianshu.com ")
            removeAlertRule3()

        }, 1000)
    }
})();