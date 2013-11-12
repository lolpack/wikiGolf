APP.UserView = Backbone.View.extend({
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
        template : _.template("<% _.each(name, function(link) { %> <li> <a href='/#wiki/<%= link %>' ><%= link %></a> </li> <% }); %>"),

        render : function () {

                var html = this.model.toJSON();
                this.$el.html(this.template(html));
        }
});



