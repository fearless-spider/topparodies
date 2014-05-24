/**
 * Created with PyCharm.
 * User: fearless
 * Date: 9/2/13
 * Time: 3:05 PM
 * To change this template use File | Settings | File Templates.
 */
django.sitesngine = {
    domainToFolderName: function() {
        var domain = django.jQuery('#id_domain').val();
        if (domain) {
            return this.folderNameCheck = domain.toLowerCase().replace(/[\s\-.]/g,'_').replace(/[^a-z0-9_]/g,'');
        }
        return '';
    },
    folderNameCheck: ''
}

django.jQuery(document).ready(function() {
    var domainEl = django.jQuery('#id_domain');
    var folderNameEl = django.jQuery('#id_folder_name');
    django.sitesngine.domainCheck = domainEl.val();
    django.sitesngine.folderNameCheck = folderNameEl.val();
    if (django.sitesngine.domainToFolderName() != folderNameEl.val()) {
        django.sitesngine.folderNameEdited = true;
    }

    // Mark folder name as having been edited when its changed.
    folderNameEl.change(function() {
        // If the name is the same as the transformed domain, assume the
        // user did not edit the field, otherwise assume it was.
        if (folderNameEl.val() != django.sitesngine.domainToFolderName()) {
            django.sitesngine.folderNameEdited = true;
        }
    });

    // If the folder name has not been edited, auto-generate folder name from
    // domain name as a convenience.
    if (!django.sitesngine.folderNameEdited) {
        domainEl.change(function() {
            var folder_name = folderNameEl.val();
            // If the folder name has not been edited, then set to transformed
            // domain.
            if (!django.sitesngine.folderNameEdited) {
                folderNameEl.val(django.sitesngine.domainToFolderName());
            }
        });
    }
});