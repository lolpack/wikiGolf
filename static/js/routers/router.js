APP.Router = Backbone.Router.extend({
	routes: {
		"first": "firstRoute",
		"second": "secondRouter",
		"wiki/:page" : "newPageLoader"
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
		APP.couresCollection.fetch({
			success: function () {
				APP.course = APP.CourseCollection;
				APP.course1view = new APP.CoursesView({
					model: APP.course
				})
                $('#linksGoHere').append(APP.course1view.render.el);
			}

	});

}

});


APP.router = new APP.Router();
Backbone.history.start({root: "/"})