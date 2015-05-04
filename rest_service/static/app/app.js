$(document).ready(function () {
	crossroads.addRoute('', function () {
		crossroads.parse('stories/new')
	})
	crossroads.addRoute('{type}/new/', function (type) {
		loadNewest(type);
	});

	crossroads.addRoute('{type}/hot/', function (type) {
		loadHottest(type);
	});

	crossroads.addRoute('{type}/view/{id}', function (type, id) {
		loadSingle(type, id);
	});

	crossroads.addRoute('create-story', function () {
		loadStoryCreate();
	});

	crossroads.addRoute('create-picture', function () {
		loadPictureCreate();
	});

//	crossroads.routed.add(console.log, console); //log all routes

	hasher.initialized.add(parseHash); //parse initial hash
	hasher.changed.add(parseHash); //parse hash changes
	hasher.init(); //start listening for history change
	 
	//update URL fragment generating new history record
    //hasher.setHash('lorem/ipsum');

	//setup hasher
	function parseHash(newHash, oldHash){
	  crossroads.parse(newHash);
	}

	$('#link-back-top').click(function () {
		$("html, body").animate({ scrollTop: 0 }, 500);
	});
});