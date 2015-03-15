var devops = window.devops || {};

devops.profile = {
    init: function() {
        devops.profile.setupCreateInstanceButton();
    },

    setupCreateInstanceButton: function() {
        $(document).on('click', '.create-instance', function() {
            devops.profile.createInstance($(this));
        });
    },

    createInstance: function(button) {
        $('#create-instance').submit(function(event) {
            event.preventDefault();
        });
    }
}

$(document).ready(function() {
    devops.profile.init();
});
