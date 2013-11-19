//View for the links clicked on or "Course Content"

APP.CourseContent = Backbone.View.extend({
        tagName: 'p',
        render : function () {
                this.$el.html(this.model.get('courseContent'));
                return this;
        }
});