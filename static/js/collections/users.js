//User collection

APP.UserCollection = Backbone.Collection.extend({
	model : APP.UserModel,
	url: "/user"
});

