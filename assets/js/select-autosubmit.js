/* ===== Zeste de Savoir ====================================================
   Auto submit forms
   ---------------------------------
   Author: Alex-D / Alexandre Demode
   ========================================================================== */

(function($, undefined){
    "use strict";
    
    $("body").on("change", ".select-autosubmit", function() {
        $(this).parents("form:first").submit();
    });
})(jQuery);