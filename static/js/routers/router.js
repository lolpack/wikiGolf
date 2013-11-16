APP.Router = Backbone.Router.extend({
	routes: {
		"first": "firstRoute",
		"second": "secondRouter",
		"wiki/:page" : "newPageLoader",
		"course/:courseChoice" : "pick_course"
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
				console.log(newView);
			
		}
	});
	},
	newPageLoader : function (page) {
		APP.couresCollection = new APP.CoursesCollection();
		APP.couresCollection.create({next:page});
		console.log(APP.couresCollection);
		$('#linksGoHere').html('');
		$('#wikiTitle').html('');
		APP.course = new APP.Course();

		APP.couresCollection.fetch({
			success: function () {
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
			}

	});
	},
	pick_course: function (courseChoice) {
		APP.couresCollection = new APP.CoursesCollection();
		APP.couresCollection.create({next:courseChoice});
		console.log(APP.couresCollection);
		APP.couresCollection.fetch({
			success: function () {
				var link = APP.couresCollection;
				APP.course1view = new APP.CoursesView({
					collection: link
				})
				$('#courseForm').html('');
				$('#instructions').html('');
                $('#linksGoHere').append(APP.course1view.render().el);
			}

	});
	}

});


APP.router = new APP.Router();
Backbone.history.start({root: "/"})