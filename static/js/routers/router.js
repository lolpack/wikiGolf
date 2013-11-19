APP.Router = Backbone.Router.extend({
	routes: {
		"first": "firstRoute",
		"second": "secondRouter",
		"wiki/:page" : "newPageLoader",
		"course/:courseChoice" : "pick_course",
		"stats" : "gameOver"
	},
	firstRoute: function() {
		alert("First route was hit");
		APP.userCollections = new APP.Users();

	},
	secondRouter: function () {
		APP.CourseCollection = new APP.CoursesCollection();
		APP.CourseCollection.fetch({
			success: function () {
					var link = APP.CourseCollection;
					var newView = new APP.CoursesView({
					collection: link
				
				});
				$('#linksGoHere').append(newView.render().el);
			
		}
	});
	},
	newPageLoader : function (page) {
		APP.couresCollection = new APP.CoursesCollection();
		APP.couresCollection.create({next:page});
		console.log(APP.couresCollection);
		$('#linksGoHere').html('');
		$('#wikiTitle').html('');
		$('#startFinish').html('');
		$('#strokes').html('');
		APP.course = new APP.Course();

		APP.couresCollection.fetch({
			success: function () {
				var gameState = APP.couresCollection.get(1);
				if (gameState.attributes.gameOver === true) {
					APP.router.navigate('#stats', {trigger: true, replace: true})//Check if game is over, send to congrats screen
					
				} else {
					$('#coursePath').html('');
					console.log(gameState.attributes.gameOver);
					var link = APP.couresCollection;
					APP.course1view = new APP.CoursesView({
						collection: link
					})
	                $('#linksGoHere').append(APP.course1view.render().el);
	                var currentCourse = link.get(1);
	                APP.courseTitle = new APP.CourseTitle({
	                	model: currentCourse
	                })
	                $('#wikiTitle').append(APP.courseTitle.render().el);
	                APP.startFinish = new APP.StartFinish({
	                	model: currentCourse
	                })
	                $('#startFinish').append(APP.startFinish.render().el);

	                APP.coursePath = new APP.CoursePath({
                	model: currentCourse
                	})
                	$('#coursePath').append(APP.coursePath.render().el);
					}
				}

			});
	
		APP.userCollection.fetch({
			success: function () {
				var collection = APP.userCollection;
				var strokes = collection.get(1);
				console.log(collection);
				APP.userView = new APP.UserView({
					model: strokes
				})
				$('#strokes').append(APP.userView.render().el)

			}
		})
	},
	pick_course: function (courseChoice) {
		APP.couresCollection = new APP.CoursesCollection();
		APP.couresCollection.create({next:courseChoice});
		console.log(APP.couresCollection);
		APP.couresCollection.fetch({
			success: function () {
				$('#strokes').html('');
				var link = APP.couresCollection;
				APP.course1view = new APP.CoursesView({
					collection: link
				})
				$('#courseForm').html('');
				$('#instructions').html('');
                $('#linksGoHere').append(APP.course1view.render().el);
                var currentCourse = link.get(1);
                APP.courseTitle = new APP.CourseTitle({
                	model: currentCourse
                })
                $('#wikiTitle').append(APP.courseTitle.render().el);
                APP.startFinish = new APP.StartFinish({
                	model: currentCourse
                })
                $('#startFinish').append(APP.startFinish.render().el);

                APP.coursePath = new APP.CoursePath({
                	model: currentCourse
                })
                $('#coursePath').append(APP.coursePath.render().el);
                APP.courseContent = new APP.CourseContent({
                	model: currentCourse
                })
                $('#wikiContent').append(APP.courseContent.render().el);
			}

			});
		APP.userCollection = new APP.UserCollection();
		APP.userCollection.fetch({
			success: function () {
				var collection = APP.userCollection;
				var strokes = collection.get(1);
				console.log(collection);
				APP.userView = new APP.UserView({
					model: strokes
				})
				$('#strokes').append(APP.userView.render().el)

			}
		})
	},
	gameOver: function () {
		var course = APP.couresCollection.get(1);
		console.log(APP.userCollection);
		$('#startFinish').html('<h2>Congrats! You made it from '+ course.get('startPage') + ' to ' + course.get('endPage')+ '</h2>');
		$('#wikiTitle').html('<h3><a href="/">Start Over!</a></h3>');
	}

});


APP.router = new APP.Router();
Backbone.history.start({root: "/"})