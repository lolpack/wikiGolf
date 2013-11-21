APP.Router = Backbone.Router.extend({
	routes: {
		"wiki/:page" : "newPageLoader", //Get's called when someone clicks on a wikipedia link. Loads next wiki page
		"course/:courseChoice" : "pick_course", //Get's called when someone makes a course choice
		"stats" : "gameOver" //Called if backbone tries to load the correct ending course. Renders game over page.
	},
	newPageLoader : function (page) {
		APP.courseCollection = new APP.CoursesCollection();
		APP.courseCollection.create({next:page});

		//Clear content from screen
		$('#wikiContent').html('');
		$('#wikiTitle').html('');
		$('#startFinish').html('');
		$('#strokes').html('');

		var target = document.getElementById('wikiContent'); //Spinner logic and view
		var spinner = new Spinner().spin();
		target.appendChild(spinner.el);

		APP.course = new APP.Course();

		APP.courseCollection.fetch({
			success: function () {
				spinner.stop(); //Stop spinner
				var gameState = APP.courseCollection.get(1);
				if (gameState.attributes.gameOver === true) {
					APP.router.navigate('#stats', {trigger: true, replace: true})//Check if game is over, send to congrats screen
					
				} else {
					$('#coursePath').html('');
					var link = APP.courseCollection;
					APP.course1view = new APP.CoursesView({
						collection: link
					})
	                //$('#linksGoHere').append(APP.course1view.render().el); //Render's just the links
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
				}

			});
	
		APP.userCollection.fetch({ //Render user information 
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
		$('#strokes').html('');

		var target = document.getElementById('wikiContent');
		var spinner = new Spinner().spin();
		target.appendChild(spinner.el);

		APP.courseCollection = new APP.CoursesCollection();
		APP.courseCollection.create({next:courseChoice});
		console.log(APP.courseCollection);
		APP.courseCollection.fetch({
			success: function () {
				spinner.stop();
				$("#coursePickerForm").html('');
				var link = APP.courseCollection;
				APP.course1view = new APP.CoursesView({
					collection: link
				})
				$('#courseForm').html('');
				$('#instructions').html('');
                //$('#linksGoHere').append(APP.course1view.render().el);
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
		var course = APP.courseCollection.get(1);
		console.log(APP.userCollection);
		FB.api('/me', function(response) {
			if (response.first_name) {
				$('#startFinish').html('<h2>Congrats ' + response.first_name + '! You made it from '+ course.get('startPage') + ' to ' + course.get('endPage')+ '</h2>');
				$('#wikiTitle').html('<h3><a href="/">Start Over!</a></h3>');
			} else {
				$('#startFinish').html('<h2>Congrats! You made it from '+ course.get('startPage') + ' to ' + course.get('endPage')+ '</h2>');
				$('#wikiTitle').html('<h3><a href="/">Start Over!</a></h3>');
			}
			});
		}
		


});


APP.router = new APP.Router(); //Instantiate APP.Router
Backbone.history.start({root: "/"})