//View for Start and Finish pages on the course. 

APP.StartFinish = Backbone.View.extend({
        tagName: 'h2',
        render : function () {
                this.$el.html('Starting from "'+ this.model.get('startPage') + '," get to "' + this.model.get('endPage')+'"');
                return this;
        }
});