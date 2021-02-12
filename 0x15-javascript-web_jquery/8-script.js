$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (films, status) {
    const data = films.results;
    for (const item of data) {
	$('UL#list_movies').append('<li>' + item.title + '</li>');
    }
});
