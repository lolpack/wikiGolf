APP.Course = Backbone.Model.extend({
	defaults: {
		wikiCourse: {
			startPage: null,
			endPage: null,
			par: null,

		}

});

//This model will represent the various wikipedia pages being traversed in the app and how they relate to the wikiGolf game. 
//This is related to the user model as the user will rely on data from this model in order to compute different stats for the user.
