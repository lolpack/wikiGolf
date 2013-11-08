APP.Router = Backbone.Router.extend({
	routes: {
		"first": "firstRoute",
		"second": "secondRouter"
	},
	firstRoute: function() {
		console.log("First route was hit");
		APP.userCollections = new APP.Users();

		APP.userCollections.create({name:"colin", phone: "5555555555"});
		APP.userCollections.create({name:"dan", address: "seattle"});
	},
	secondRouter: function () {
		console.log("Second route was hit");
	}
});

APP.router = new APP.Router();
Backbone.history.start({root: "/"})