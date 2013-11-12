APP.Router = Backbone.Router.extend({
	routes: {
		"first": "firstRoute",
		"second": "secondRouter"
	},
	firstRoute: function() {
		alert("First route was hit");
		APP.userCollections = new APP.Users();

		APP.userCollections.create({name:"colin", strokes: 5});
		APP.userCollections.create({name:"dan", facebookPointer: null});
	},
	secondRouter: function () {
		APP.usersCollection = new APP.Users();
		var t= APP.usersCollection.fetch();
		console.dir(APP.usersCollection);
		

	}

});

var sum = _.reduce([1, 2, 3], function(memo, num){ return memo + num; }, 0);
console.log(sum)

APP.router = new APP.Router();
Backbone.history.start({root: "/"})