// Implementation filters from _includes/impl-filter.html, shared by the front
// page (rows) and the comparison tables (columns).
//
//   var filter = ImplFilter(form);
//   filter.matches(el)   // el carries the data-* attributes listed below
//
//   data-roles      "client:app server:lib ..."; kind is app, lib or unknown
//   data-platforms  "linux macos ..."; absent when none are recorded
//   data-languages  "C|Rust"; absent when none are recorded

window.ImplFilter = function (form) {
  'use strict';

  var UNKNOWN_LANG = '?';

  function ticked(name) {
    var out = [];
    Array.prototype.forEach.call(
      form.querySelectorAll('input[name="' + name + '"]:checked'),
      function (box) { out.push(box.value); }
    );
    return out;
  }

  function words(value, sep) {
    return value ? value.split(sep) : null;
  }

  function some(list, pred) {
    for (var i = 0; i < list.length; i++) if (pred(list[i])) return true;
    return false;
  }

  // Read the form once per apply, not once per element.
  function snapshot() {
    return {
      sides: ticked('side'),
      kinds: ticked('kind'),
      on: ticked('on'),
      off: ticked('off'),
      lang: form.elements.lang.value
    };
  }

  function matches(el, s) {
    s = s || snapshot();

    var roles = words(el.dataset.roles, ' ') || [];
    var roleOk = some(roles, function (token) {
      var parts = token.split(':');
      return s.sides.indexOf(parts[0]) !== -1 && s.kinds.indexOf(parts[1]) !== -1;
    });
    if (!roleOk) return false;

    // Unrecorded platforms cannot show that they are on a wanted platform,
    // nor that they are on an unwanted one.
    var platforms = words(el.dataset.platforms, ' ');
    if (s.on.length && !(platforms && some(s.on, function (p) { return platforms.indexOf(p) !== -1; }))) return false;
    if (s.off.length && platforms && some(s.off, function (p) { return platforms.indexOf(p) !== -1; })) return false;

    var langs = words(el.dataset.languages, '|');
    if (s.lang === UNKNOWN_LANG) return !langs;
    if (s.lang && !(langs && langs.indexOf(s.lang) !== -1)) return false;

    return true;
  }

  return { matches: matches, snapshot: snapshot };
};
