APP.Course = Backbone.Model.extend({
	//This model represents the various wikipedia pages being traversed in the app and how they relate to the wikiGolf game. 
	defaults: function (){
		return {
			startPage: null,
			endPage: null,
			current: null,
			next: null,
			id: null,
			gameOver: false,
			coursePath: null,
			courseContent: null
		};
	}

});


//This is related to the user model as the user will rely on data from this model in order to compute different stats for the user.
