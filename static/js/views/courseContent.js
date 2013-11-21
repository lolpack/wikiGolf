//View for the links clicked on or "Course Content"

APP.CourseContent = Backbone.View.extend({
        tagName: 'div',
        className: "pageEmbed",
        render : function () {
                this.$el.html(this.model.get('courseContent'));
                return this;
        }
});