function loadNewest (type, page) {
	loadData(type);
}

function loadHottest (type, page) {
	loadData(type);
}

function loadSingle (type, id) {
	if (checkIfValidType(type)) {
		$.get("ajax/test.html", function(data) {
		});
	}
}

function checkIfValidType (type) {
	var TYPES = {
		stories: 'stories',
		pictures: 'pictures',
	};

	if(type === TYPES.stories || type === TYPES.pictures) {
		return true;
	}

	return false;
}

function loadPictures (dataPath) {
	var $contentDiv = $('#changeable-content');
	$contentDiv.html('');

	$.get(dataPath, function(data) {
		$.get('/static/main-page-picture.html', function (source) {
			var template = Handlebars.compile(source),
				results = data,
				context,
				i;

			for(i = 0; i < results.length; i++) {
				context = {
					title: results[i].title,
					imageSource: results[i].image
				}

				var html = template(context);
				$contentDiv.append(html);
			}
		})
	});
}

function loadStories (dataPath) {
	var $contentDiv = $('#changeable-content');
	$contentDiv.html('');

	$.get(dataPath, function(data) {
		$.get('/static/main-page-story.html', function (source) {
			var template = Handlebars.compile(source),
				results = data,
				context,
				i;

			for(i = 0; i < results.length; i++) {
				context = {
					title: results[i].title,
					text: results[i].content
				}

				var html = template(context);
				$contentDiv.append(html);
			}
		})
	});
}

function loadData (contentType, orderType) {
	if (checkIfValidType(contentType)) {
		var dataPath = 'api/' + contentType;
		if(contentType === 'pictures') {
			loadPictures(dataPath, orderType);
		} else {
			loadStories(dataPath, orderType);
		}
	}
}