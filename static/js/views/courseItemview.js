APP.CourseItemView = Backbone.View.extend({
        tagName: 'li',
        events: {
                "click li": "alertStatus"

        },
        alertStatus: function(e){
                console.log('Hey you clicked the li!');

        },
        template : _.template("<li> <a href='/#wiki/<%= name %>' ><%= name %></a> </li>"),

        render : function () {
                var html = this.model.toJSON();
                this.$el.html(this.template(html));
                return this
        }
});