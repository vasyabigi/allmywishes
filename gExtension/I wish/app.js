$(document).ready(function() {
    var siteUrl = "http://allmywish.es";

    $('#getCookies').on('click', function(e) {
        chrome.cookies.getAll({url: siteUrl}, function(cookie) {
            console.log('cookies: ', cookie);

            $('#cookies').html(cookie);
        });
    });

    $('#getTabUrl').on('click', function(e) {
        chrome.tabs.getSelected(null, function(tab) {
            console.log(tab);

            $('#tabUrl').html(tab.url);
        });
    });

    $('#makeRequest').on('click', function() {
        var url = 'http://allmywish.es';

        $.ajax({
            method: 'GET',
            url: url,
            success: function(resp) {
                console.log(resp);
            }
        });
    });



});
