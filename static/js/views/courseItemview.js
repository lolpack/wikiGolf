APP.CourseItemView = Backbone.View.extend({
        tagName: 'li',
        events: {
                "click li": "alertStatus",
                "dblclick" : "RemoveP",
                "mouseover h1" : "mouseoverH"

        },
        alertStatus: function(e){
                alert('Hey you clicked the li!');
        
        },
        RemoveP: function () {
                $('p').html("TEEHEE");
        },
        mouseoverH : function () {
                $('h1').console.log("See you");
        },
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
        //renders html for userView
        //template: _.template(list, {links: ['moe', 'curly', 'larry']}),
                template : _.template("<li> <a href='/#wiki/<%= name %>' ><%= name %></a> </li>"),

        render : function () {
                var html = this.model.toJSON();
                this.$el.html(this.template(html));
                return this
        }
});