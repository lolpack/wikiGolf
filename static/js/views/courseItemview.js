//Course view that displays an individual link on a page. Not in use for now. 

APP.CourseItemView = Backbone.View.extend({
        tagName: 'li',
        events: {
                "click li": "alertStatus"

        },
        template : _.template("<li> <a href='/#wiki/<%= name %>' ><%= name %></a> </li>"),

        render : function () {
                var html = this.model.toJSON();
                this.$el.html(this.template(html));
                return this
        }
});