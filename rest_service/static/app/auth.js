$(document).ready(function () {
	setupHeaders();
	$.get('/static/login.html', function (template) {
		$('#auth-modal .modal-content').html(template)
			.ready(function () {
				$('#login-form').submit(function () {
					$.ajax({
						url: '/api/token-auth/',
						data: $('#login-form').serialize(),
						type: 'POST',
					}).then(function (data) {
						removeLogin();
						$.cookie('token', data.token);
						$('#auth-modal').modal('hide');

						var storyLink = $('<a/>');
						storyLink.attr('id', 'story-link')
							.click(function () {
								crossroads.parse('/create-story');								
							})
							.attr('class', 'list-group-item')
							.attr('href', '#/create-story')
							.html('Create story');

						var pictureLink = $('<a/>');
						pictureLink.attr('id', 'picture-link')
							.click(function () {
								crossroads.parse('/create-picture');	
							})
							.attr('class', 'list-group-item')
							.attr('href', '#/create-picture')
							.html('Create picture');

						$('#main-content .list-group').append(storyLink)
							.append(pictureLink);
					});

					return false;
				});
			});
	});

	$.get('/static/register.html', function (template) {
		$('#register-modal .modal-content').html(template)
			.ready(function () {
				$('#register-form').submit(function () {
					$.ajax({
						url: '/api/register-user',
						data: $('#register-form').serialize(),
						type: 'POST',
					});

					return false;
				});
			});
	});

	if($.cookie('token')) {
		removeLogin();
	} else {
		addLogin();
	}
});

function addLogin () {
	$('#login-out').html('Login');
	$('#login-out').off().click(function () {
		$('#auth-modal').modal('show');
		return false;
	});

	$('#register').click(function () {
		$('#register-modal').modal('show');
	});

	$('#register').show();
}

function removeLogin () {
	$('#login-out').html('Logut');
	$('#login-out').off().click(function () {
		logOut();
		return false;
	});

	$('#register').hide();
}

function logOut () {
	$.cookie('token', '');
	addLogin();
	$('#picture-link').remove();
	$('#story-link').remove();
}

function setupHeaders () {
	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	function sameOrigin(url) {
	    // test that a given url is a same-origin URL
	    // url could be relative or scheme relative or absolute
	    var host = document.location.host; // host + port
	    var protocol = document.location.protocol;
	    var sr_origin = '//' + host;
	    var origin = protocol + sr_origin;
	    // Allow absolute or scheme relative URLs to same origin
	    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
	        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
	        // or any other URL that isn't scheme relative or absolute i.e relative.
	        !(/^(\/\/|http:|https:).*/.test(url));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
	            // Send the token to same-origin, relative URLs only.
	            // Send the token only if the method warrants CSRF protection
	            // Using the CSRFToken value acquired earlier
//	            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
	            xhr.setRequestHeader('Authorization', 'Token ' + $.cookie('token'));
	        }
	    }
	});
}