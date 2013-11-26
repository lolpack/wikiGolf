APP.UserModel = Backbone.Model.extend({

	defaults: function () {
		return {
		id: 1,
		name: null,
		strokes: 0,
		facebookPointer: null,
		history: null
		};
	},
		url: "/user"
});



APP.createUser = function () {
	FB.api('/me', function(response) {
			APP.fbInfo = {id: response.id, name : response.name};
	});
	APP.insertUser = new APP.UserModel;
	APP.insertUser.create({facebookPointer: APP.fbInfo.id, name : APP.fbInfo.name})

};
//The model should hold basic data about the user's identity (grabbed from facebook). And also his/her gamer stats.
//This is relates to the course model as it will need to know if the player succesfully made it from the begging to the end 
//Also, in order to calculate strokes, it will need to know how many pages the user went through. 