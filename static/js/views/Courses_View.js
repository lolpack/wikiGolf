//APP Courses multi item view

APP.CoursesView = Backbone.View.extend({
        tagName: 'ul',
        className: 'Float-Left',


        render : function () {
                this.collection.each(function(model) {
                        APP.courseItemView = new APP.CourseItemView({
                                model:model
                        });
                
                this.$el.append(APP.courseItemView.render().el);
        },this);
         return this; 
     }
});