//View for the links clicked on or "Course Path"

APP.CoursePath = Backbone.View.extend({
        tagName: 'p',
        render : function () {
                this.$el.html("Course Path: " + this.model.get('coursePath'));
                return this;
        }
});