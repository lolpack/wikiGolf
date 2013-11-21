//Collection for different couse link models

APP.CoursesCollection = Backbone.Collection.extend({
	model : APP.Course,
	url: "/nextWiki"
});