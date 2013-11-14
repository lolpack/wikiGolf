//APP Courses multi item view

APP.CoursesView = Backbone.View.extend({
        tagName: 'ul',
        className: 'Float-Left',
/*        events: {

        },
        initialize: function () {
        
        },
        //destroy user method
        destroyUser : function () {
                this.model.destroy();
        },
        //edit user method
        editUser : function () {
                if (edit_open == 'false') {
                        new editView ({model: this.model}); //instantiates new editView
                        edit_open = 'true'; //prevents multiple 'edit_users' from being instantiated
                }        
        }, */
        //renders html for userView
        //template: _.template(list, {links: ['moe', 'curly', 'larry']}),


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