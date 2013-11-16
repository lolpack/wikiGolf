APP.CourseTitle = Backbone.View.extend({
        tagName: 'h2',
/*        initialize: function () {
        
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


        render : function () {
                this.$el.html('Displaying Wikipedia page for "' + this.model.get('current') + '"');
                return this;
        }
});