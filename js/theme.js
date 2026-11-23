//
// The header switch picks the system, light or dark theme. Light and dark
// are stored, and _includes/head.html applies them on load; "system" clears
// the stored choice.
//
(function () {
  var KEY = 'theme';
  var root = document.documentElement;
  var group = document.getElementById('theme-switch');
  var buttons = group.querySelectorAll('button');

  function render() {
    var mode = root.getAttribute('data-theme') || 'system';
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].setAttribute('aria-pressed', String(buttons[i].value === mode));
    }
  }

  group.addEventListener('click', function (event) {
    var button = event.target.closest('button');
    if (!button) return;

    var mode = button.value;
    if (mode === 'system') root.removeAttribute('data-theme');
    else root.setAttribute('data-theme', mode);

    try {
      if (mode === 'system') localStorage.removeItem(KEY);
      else localStorage.setItem(KEY, mode);
    } catch (e) {}

    render();
  });

  render();
  group.hidden = false;
})();
