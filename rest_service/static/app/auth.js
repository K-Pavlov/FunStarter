var AuthHandler = function () {
	"use strict";
    if (AuthHandler.prototype._singletonInstance) {
        return AuthHandler.prototype._singletonInstance;
    }
    
    AuthHandler.prototype._singletonInstance = this;

    this.configureLoggedOut = function () {
		addLogin();
    };

    this.logOut = function () {
		$.cookie('token', '');
		addLogin();
		$('#picture-link').remove();
		$('#story-link').remove();
    };

    this.configureLoggedIn = function () {
    	var self = this;

		$('#login-out').html('Logut');
		$('#login-out').off().click(function () {
			self.logOut();
			return false;
		});

		$('#register').hide();   
		addLoggedInLinks(); 	
    };

	this.setupHeaders = function () {
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

	function addLoggedInLinks() {
		var storyLink = $('<a/>');
		storyLink.attr('id', 'story-link')
			.attr('class', 'list-group-item')
			.attr('href', '#/create-story')
			.html('Create story');

		var pictureLink = $('<a/>');
		pictureLink.attr('id', 'picture-link')
			.attr('class', 'list-group-item')
			.attr('href', '#/create-picture')
			.html('Create picture');

		$('#main-content .list-group')
			.append(storyLink)
			.append(pictureLink);
	}
};

$(document).ready(function () {
	"use strict";
	var authHandler = new AuthHandler();
	authHandler.setupHeaders();

	$.get('/static/login.html', function (template) {
		$('#auth-modal .modal-content').html(template)
			.ready(function () {
				$('#login-form').submit(function () {
					$.ajax({
						url: '/api/token-auth/',
						data: $('#login-form').serialize(),
						type: 'POST',
					}).then(function (data) {
						authHandler.configureLoggedIn();
						$.cookie('token', data.token);
						$('#auth-modal').modal('hide');
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
		authHandler.configureLoggedIn();
	} else {
		authHandler.configureLoggedOut();
	}
});
