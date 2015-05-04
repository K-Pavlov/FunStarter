var TYPES = {
	stories: 'stories',
	pictures: 'pictures',
};

function loadNewest (type, page) {
	loadData(type);
}

function loadHottest (type, page) {
	loadData(type);
}

function loadSingle (type, id) {
	if (checkIfValidType(type)) {
		$.get('api/' + type + '/' + id, function(data) {
			$.get('/static/view-item.html', function (source) {
				var template = Handlebars.compile(source),
				    $changeableContent = $('#changeable-content'),
					results = data,
					singleHtml,
					context,
					$html,
					i;

				dateTime = getDateTime(results.time);
				context = {
					title: results.title,
					text: results.content,
					date: dateTime.date,
					time: dateTime.time,
					comments: results.comments,
					id: id
				};

				$html = $(template(context));
				$html.find('#comment-form').submit(function () {
					var $form = $(this);
					$.post('/api/comments/' + type + '/' + id, 
						$form.serialize(), 
						function (data) {
							var commentDiv = $('<div/>'),
								usernameDiv = $('<div><strong>' + data.user.username 
											+ '</strong></div>');

							commentDiv.attr('class', 'comment col-md-12')
									 .append(usernameDiv)
									 .append(data.content);	
							$('#comments').append(commentDiv);
						});
					return false;
				});
				$changeableContent.html($html);
			});
		});
	}
}

function loadPictures (dataPath) {
	var $contentDiv = $('#changeable-content');
	$contentDiv.html('');

	$.get(dataPath, function(data) {
		$.get('/static/main-page-picture.html', function (source) {
			var template = Handlebars.compile(source),
				results = data,
				context,
				html,
				i;

			for(i = 0; i < results.length; i++) {
				context = {
					title: results[i].title,
					imageSource: results[i].image
				};

				$html = $(template(context));
				$contentDiv.append(html);
			}
		});
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
				time,
				$html,
				id,
				i;

			for(i = 0; i < results.length; i++) {
				id = results[i].id;
				dateTime = getDateTime(results[i].time);
				context = {
					title: results[i].title,
					text: results[i].content,
					date: dateTime.date,
					time: dateTime.time,
					id: id,
				};

				$html = $(template(context));
				$html.find('.title')
					.attr('href', '#/' + TYPES.stories + '/view/' + id);
				$contentDiv.append($html);
			}
		});
	});
}

function loadStoryCreate () {
	$.get('/static/create-story.html', function (data) {
		$('#changeable-content').html(data)
			.ready(function () {
				$('#create-story-form').submit(function () {
					$.ajax({
						url: '/api/create-story',
						data: $('#create-story-form').serialize(),
						type: 'POST',
					});
<<<<<<< HEAD

=======
					
>>>>>>> 7592dd499cd8f0f44efd82cfea882d21963161eb
					return false;
				});
			});
	});
}

<<<<<<< HEAD
function loadData (contentType, orderType) {
	if (checkIfValidType(contentType)) {
		var dataPath = 'api/' + contentType;
		if(contentType === TYPES.pictures) {
			loadPictures(dataPath, orderType);
		} else {
			loadStories(dataPath, orderType);
		}
	}
}

function checkIfValidType (type) {
	if(type === TYPES.stories || type === TYPES.pictures) {
		return true;
	}

	return false;
}

function getDateTime (pythonTime) {
	var dateTime = pythonTime.split('T'),
		date = dateTime[0],
		time = dateTime[1].substring(0, 5);

	return {
		date: date,
		time: time,
	};
=======
function loadPictureCreate () {
	$.get('/static/create-picture.html', function (data) {
		$('#changeable-content').html(data)
			.ready(function () {
				$('#create-picture-form').submit(function () {
					$.ajax({
						url: '/api/create-picture',
						data: $('#create-picture-form').serialize(),
						type: 'POST',
					});

					return false;
				});
			})
	});	
>>>>>>> 7592dd499cd8f0f44efd82cfea882d21963161eb
}