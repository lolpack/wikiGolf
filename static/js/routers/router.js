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
		APP.usersCollection = new APP.Users();
		APP.usersCollection.fetch({
			success: function () {
				APP.user1 = APP.usersCollection.get(3);
				APP.user1view = new APP.UserView({
					model: APP.user1
				})
				APP.user1view.render();
                $('#main').append(APP.user1view.$el);
                console.log(APP.usersCollection.get(3));
			}
		});

		

	},
	newPageLoader : function (page) {
		APP.coureseCollection = new APP.CoursesCollection();
		APP.coureseCollection.add([page]);
		console.log(APP.coureseCollection);

	}

});


APP.router = new APP.Router();
Backbone.history.start({root: "/"})