APP.CourseTitle = Backbone.View.extend({
        tagName: 'h3',


        render : function () {
                this.$el.html('Displaying Wikipedia page for "' + this.model.get('current') + '"');
                return this;
        }
});