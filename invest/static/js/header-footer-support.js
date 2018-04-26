/*
 * BELOW CODE IS NOT CURRENTLY IN STATIC HEADER/FOOTER FILE
 * BUT REQUIRED TO SUPPORT THE STANDARD LANGUAGE SELECTOR.
 **********************************************************/


dit = headerFooter;

/*
 * JS content taken from - 
 * https://www.great.gov.uk/static/js/dit.class.modal.9301dc637113.js
 *
 *************************************************************************************/


/* Class: Modal
 * -------------------------
 * Create an area to use as popup/modal/lightbox effect.
 *
 * REQUIRES:
 * jquery
 * dit.js
 * dit.responsive.js
 *
 **/
(function($, utils, classes) {

  var ARIA_EXPANDED = "aria-expanded";
  var CSS_CLASS_CLOSE_BUTTON = "close";
  var CSS_CLASS_CONTAINER = "Modal-Container"
  var CSS_CLASS_CONTENT = "content";
  var CSS_CLASS_OPEN = "open";
  var CSS_CLASS_OVERLAY = "Modal-Overlay";

  /* Constructor
   * @options (Object) Allow some configurations
   **/
  classes.Modal = Modal;
  function Modal($container, options) {
    var modal = this;
    var config = $.extend({
      $activators: $(), // (optional) Element(s) to control the Modal
      closeOnBuild: true, // Whether intial Modal view is open or closed
      overlay: true,  // Whether it has an overlay or not
      closeButtonId: '', // Option to add custom close button id
      onClose: function() {} // (optional) Callback called on modal close
    }, options || {});

    // If no arguments, likely just being inherited
    if (arguments.length) {
      // Create the required elements
      if(config.overlay) {
        this.$overlay = Modal.createOverlay();
        Modal.bindResponsiveOverlaySizeListener.call(this);
      }

      this.$closeButton = Modal.createCloseButton(config.closeButtonId);
      this.$content = Modal.createContent();
      this.$container = Modal.enhanceModalContainer($container);
      this.onClose = config.onClose;

      // Add elements to DOM
      Modal.appendElements.call(this, config.overlay);

      // Add events
      Modal.bindCloseEvents.call(this);
      Modal.bindActivators.call(this, config.$activators);

      // Initial state
      if (config.closeOnBuild) {
        this.close();
      }
      else {
        this.open();
      }
    }
  }

  Modal.createOverlay = function() {
    var $overlay = $(document.createElement("div"));
    $overlay.addClass(CSS_CLASS_OVERLAY);
    return $overlay;
  }

  Modal.createCloseButton = function(closeButtonId) {
    var $button = $(document.createElement("button"));
    $button.text("Close");
    $button.addClass(CSS_CLASS_CLOSE_BUTTON);
    if (closeButtonId) $button.attr('id', closeButtonId);
    return $button;
  }

  Modal.createContent = function() {
    var $content = $(document.createElement("div"));
    $content.addClass(CSS_CLASS_CONTENT);
    return $content;
  }

  Modal.findFirstFocusElement = function($container) {
    return $container.find("video, a, button, input, select").eq(0);
  }

  Modal.findLastFocusElement = function($container) {
    return $container.find("video, a, button, input, select").last();
  }

  Modal.enhanceModalContainer = function($container) {
    $container.addClass(CSS_CLASS_CONTAINER);
    return $container;
  }

  Modal.appendElements = function(overlay) {
    this.$container.append(this.$content);
    this.$container.append(this.$closeButton);

    if (overlay) {
      $(document.body).append(this.$overlay);
    }
    $(document.body).append(this.$container);
  }

  // Handles open actions including whether additioal
  // ability to focus and remember activator if using
  // the keyboard for navigation.
  Modal.activate = function(activator, event) {
    this.activator = activator;
    this.open();
    switch(event.which) {
      case 1: // mouse
        this.shouldReturnFocusToActivator = false;
        break;
      case 13: // Enter
        this.shouldReturnFocusToActivator = true;
        this.focus();
        break;
    }
  }

  // Handles close including whether additional
  // ability to refocus on original activator
  // (e.g. if using keyboard for navigaiton).
  Modal.deactivate = function() {
    if(this.shouldReturnFocusToActivator) {
      this.activator.focus();
    }

    this.close();
    this.activator = null;
  }

  Modal.bindCloseEvents = function() {
    var self = this;

    self.$container.on("keydown", function(e) {
      // Close on Esc
      if(e.which === 27) {
        Modal.deactivate.call(self);
      }
    });

    self.$closeButton.on("click", function(e) {
      // Close on click
      Modal.deactivate.call(self);
      e.preventDefault();
    });

    if (self.$overlay && self.$overlay.length) {
      self.$overlay.on("click", function(e) {
        Modal.deactivate.call(self);
      });
    }
  }

  Modal.bindKeyboardFocusEvents = function() {
    var self = this;
    // Loop around to last element when pressing
    // shift+tab on first focusable element
    self.$firstFocusElement.off("keydown.modalfocus");
    self.$firstFocusElement.on("keydown.modalfocus", function(e) {
      if (e.shiftKey && e.which === 9) {
        e.preventDefault();
        self.$lastFocusElement.focus();
      }
    });
    // Loop around to first element when
    // pressing tab on last element
    self.$lastFocusElement.off("keydown.modalfocus");
    self.$lastFocusElement.on("keydown.modalfocus", function(e) {
      if (!e.shiftKey && e.which === 9) {
        e.preventDefault();
        self.$firstFocusElement.focus();
      }
    });
  }

  Modal.bindActivators = function($activators) {
    var self = this;
    $activators.on("click keydown", function(e) {
      // Click or Enter
      if(e.which === 1 || e.which === 13) {
        Modal.activate.call(self, this, e);
        e.preventDefault();
      }
    });
  }

  Modal.bindResponsiveOverlaySizeListener = function() {
    var self = this;
    // Resets the overlay height (once) on scroll because document
    // height changes with responsive resizing and the browser
    // needs a delay to redraw elements. Alternative was to have
    // a rubbish setTimeout with arbitrary delay.
    $(document.body).on(dit.responsive.reset, function(e, mode) {
      $(window).off("scroll.ModalOverlayResizer");
      $(window).one("scroll.ModalOverlayResizer", function() {
        Modal.setOverlayHeight(self.$overlay);
      });
    });
  }

  Modal.setOverlayHeight = function($overlay) {
    $overlay.get(0).style.height = ""; // Clear it first
    $overlay.height($(document).height());
  }

  Modal.prototype = {};
  Modal.prototype.close = function() {
    var self = this;
    self.$container.fadeOut(50, function () {
      self.$container.attr(ARIA_EXPANDED, false);
      self.$container.removeClass(CSS_CLASS_OPEN);
      self.onClose();
    });

    if (self.$overlay && self.$overlay.length) {
      self.$overlay.fadeOut(150);
    }

  }

  Modal.prototype.open = function() {
    var self = this;
    var top;
    if (window.pageYOffset) {
      top = window.pageYOffset;
    }
    else {
      top = document.documentElement.scrollTop;
    }

    self.$container.css("top", top + "px");
    self.$container.addClass(CSS_CLASS_OPEN);
    self.$container.fadeIn(250, function () {
      self.$container.attr(ARIA_EXPANDED, true);
    });

    if (self.$overlay && self.$overlay.length) {
      Modal.setOverlayHeight(self.$overlay);
      self.$overlay.fadeIn(0);
    }
  }

  Modal.prototype.setContent = function(content) {
    var self = this;
    self.$content.empty();
    self.$content.append(content);
    self.$firstFocusElement = Modal.findFirstFocusElement(self.$container);
    self.$lastFocusElement = Modal.findLastFocusElement(self.$container);
    Modal.bindKeyboardFocusEvents.call(self);
  }

  // Tries to add focus to the first found element allowed with natural focus ability.
  Modal.prototype.focus = function() {
    var self = this;
    self.$firstFocusElement.focus();
  }


})(jQuery, dit.utils, dit.classes);



/*
 * JS content taken from - 
 * https://www.great.gov.uk/static/js/dit.f20567117a1f.js
 *
 *************************************************************************************/


/* Class: Select Tracker
 * ---------------------
 * Adds a label element to mirror the matched selected option
 * text of a <select> input, for enhanced display purpose.
 *
 * REQUIRES:
 * jquery
 * dit.js
 * dit.classes.js
 *
 **/
(function($, classes) {
  
  /* Constructor
   * @$select (jQuery node) Target input element
   **/
  classes.SelectTracker = SelectTracker;
  function SelectTracker($select) {
    var SELECT_TRACKER = this;
    var button, code, lang;
    
    if(arguments.length && $select.length) {
      this.$node = $(document.createElement("p"));
      this.$node.attr("aria-hidden", "true");
      this.$node.addClass("SelectTracker");
      this.$select = $select;
      this.$select.addClass("SelectTracker-Select");
      this.$select.after(this.$node);
      this.$select.on("change.SelectTracker", function() {
        SELECT_TRACKER.update();
      });
      
      // Initial value
      this.update();
    }
  }
  SelectTracker.prototype = {};
  SelectTracker.prototype.update = function() {
    this.$node.text(this.$select.find(":selected").text());
  }
  
})(jQuery, dit.classes);



/*
 * JS content taken from - 
 * https://www.great.gov.uk/static/js/dit.components.languageSelector.d85ae70b6ed0.js
 *
 *************************************************************************************/


// Language Selector Component Functionality.
//
// Requires...
// dit.js
// dit.utils.js
// dit.class.modal.js

// Usage
// --------------------------------------------------------------------
// To find all Language Selector components and enhance using
// the default settings.
//
// dit.components.languageSelector.init()
//
// For greater control, use either of the individual enhance functions
// for Language Selector Control or Language Selector Dialog components.
// This also allow passing options to customise the output.
//
// dit.components.languageSelector.enhanceControl()
// dit.components.languageSelector.enhanceDialog()
//
dit.components.languageSelector = (new function() {

  var SelectTracker = dit.classes.SelectTracker;
  var LANG_SELECT_CLOSE_BUTTON_ID = "header-language-selector-close";

  /* Extends SelectTracker to meet additional display requirement
   * @$select (jQuery node) Target input element
   * @options (Object) Configurable options
   **/
  function LanguageSelectorControl($select, options) {
    SelectTracker.call(this, $select);
    if(this.$node) {
      this.$node.addClass("SelectTraker-Tracker");
      $select.parents("form").addClass("enhancedLanguageSelector");
      $select.on("change", function() {
        this.form.submit();
      })
    }
  }
  LanguageSelectorControl.prototype = new SelectTracker;
  LanguageSelectorControl.prototype.update = function() {
    var $code = $(document.createElement("span"));
    var $lang = $(document.createElement("span"));
    SelectTracker.prototype.update.call(this);
    $lang.addClass("lang");
    $code.addClass("code");
    $lang.text(this.$node.text());
    $code.text(this.$select.val());
    this.$node.empty();
    this.$node.append($code);
    this.$node.append($lang);
  }

  /* Contructor
   * Displays control and dialog enhancement for language-selector-dialog element.
   * @$dialog (jQuery node) Element displaying list of selective links
   * @options (Object) Configurable options
   **/
  function LanguageSelectorDialog($dialog, options) {
    var LANGUAGE_SELECTOR_DISPLAY = this;
    var id = dit.utils.generateUniqueStr("LanguageSelectorDialog_");
    var $control = LanguageSelectorDialog.createControl($dialog, id);
    dit.classes.Modal.call(LANGUAGE_SELECTOR_DISPLAY, $dialog, {
      $activators: $control,
      closeButtonId: LANG_SELECT_CLOSE_BUTTON_ID
    });
    this.config = $.extend({
      $controlContainer: $dialog.parent() // Where to append the generated control
    }, options);


    if(arguments.length > 0 && $dialog.length) {
      this.$container.attr("id", id);
      this.$container.addClass("LanguageSelectorDialog-Modal");
      this.config.$controlContainer.append($control);
      this.setContent($dialog.children());
    }
  }

  LanguageSelectorDialog.createControl = function($node, id) {
    var $controlContainer = $(document.createElement("li"));
    var $control = $(document.createElement("a"));
    var $lang = $(document.createElement("span"));
    var $country = $(document.createElement("span"));
    $lang.addClass("lang");
    $lang.text($node.attr("data-lang"));
    $country.addClass("label");
    $country.text($node.attr("data-label"));
    $control.append($lang);
    $control.append($country);
    $control.addClass("LanguageSelectorDialog-Tracker bidi-ltr");
    $control.attr("href", ("#" + id));
    $control.attr("aria-controls", id);
    $controlContainer.append($control);
    return $controlContainer;
  }

  LanguageSelectorDialog.prototype = new dit.classes.Modal


  // Just finds all available Language Selector components
  // and enhances using the any default settings.
  this.init = function() {
    $("[data-component='language-selector-control'] select").each(function() {
      new LanguageSelectorControl($(this));
    });

    $("[data-component='language-selector-dialog']").each(function() {
      new LanguageSelectorDialog($(this));
    });
  }

  // Selective enhancement for individual Language Selector Control views
  // Allows passing of custom options.
  // @$control (jQuery object) Something like this: $("[data-component='language-selector-control'] select")
  // @options (Object) Configurable options for class used.
  this.enhanceControl = function($control, options) {
    if ($control.length) {
      new LanguageSelectorControl($control, options);
    }
    else {
      console.error("Language Selector Control missing or not passed")
    }
  }

  // Selective enhancement for individual Language Selector Dialog views
  // Allows passing of custom options.
  // @$control (jQuery object) Something like this: $("[data-component='language-selector-dialog']")
  // @options (Object) Configurable options for class used.
  this.enhanceDialog = function($dialog , options) {
    if ($dialog.length) {
      new LanguageSelectorDialog($dialog, options);
    }
    else {
      console.error("Language Selector Dialog missing or not passed");
    }
  }

});


/*
 * JS content taken from - 
 * https://www.great.gov.uk/static/js/home.45e81242d934.js
 *
 **********************************************************/
dit.home = (new function () {
  this.init = function() {

    /* ALREADY IN header-footer.js SO DISABLING HERE
    dit.responsive.init({
      "desktop": "min-width: 768px",
      "tablet" : "max-width: 767px",
      "mobile" : "max-width: 480px"
    });
    */

    enhanceLanguageSelector();
    delete this.init; // Run once
  }

  /* Find and enhance any Language Selector Dialog view
   **/
  function enhanceLanguageSelector() {
    var $dialog = $("[data-component='language-selector-dialog']");
    dit.components.languageSelector.enhanceDialog($dialog, {
      $controlContainer: $("#header-bar .account-links")
    });

    languageSelectorViewInhibitor(false);
  }

  /* Because non-JS view is to show all, we might see a brief glimpse of
   * the open language selector before JS has kicked in to add functionality.
   * We are preventing this by immediately calling a view inhibitor function,
   * and then the enhanceLanguageSelector() function will switch of the
   * inhibitor by calling when component has been enhanced and is ready.
   **/
  languageSelectorViewInhibitor(true);
  function languageSelectorViewInhibitor(activate) {
    var rule = "[data-component='language-selector-dialog'] { display: none; }";
    var style;
    if (arguments.length && activate) {
      // Hide it.
      style = document.createElement("style");
      style.setAttribute("type", "text/css");
      style.setAttribute("id", "language-dialog-view-inhibitor");
      style.appendChild(document.createTextNode(rule));
      document.head.appendChild(style);
    }
    else {
      // Reveal it.
      document.head.removeChild(document.getElementById("language-dialog-view-inhibitor"));
    }
  }
});

$(document).ready(function() {
  dit.home.init();
});
