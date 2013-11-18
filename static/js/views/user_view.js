APP.UserView = Backbone.View.extend({
        tagName: 'p',

        render : function () {
			this.$el.html("Stroke Count: " + this.model.get('strokes'));
            return this;
        }
});



