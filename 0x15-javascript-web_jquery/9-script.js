url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.get(url, function (data, status) {
  $('div#hello').text(data.hello);
});
