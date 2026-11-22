// Filtering for the comparison tables (issue #6); sorting is table-sort.js.
//
// The table arrives complete in the HTML; this script only reorders and hides
// what is already there. Nothing is fetched, so the page is readable without
// JavaScript and the rows stay linkable and indexable.
//
// Hidden rows are moved into a second, hidden <tbody> rather than given
// display:none, so that the tr:nth-child striping of the remaining rows keeps
// alternating. Hidden columns are classed instead, since no colour rule
// depends on cell position.

(function () {
  'use strict';

  var FIRST_IMPL_COL = 2;             // after id and Specification
  var HIDDEN_COL_CLASS = 'col-hidden';

  var form = document.getElementById('cmp-controls');
  var table = document.querySelector('.impl-comparison');
  if (!form || !table) return;

  var head = table.tHead.rows[0];
  var body = table.tBodies[0];
  var spill = document.getElementById('cmp-filtered-out');
  var counts = document.getElementById('cmp-counts');

  var rows = Array.prototype.slice.call(body.rows);
  var headCells = Array.prototype.slice.call(head.cells);
  var implCols = headCells.filter(function (th) {
    return th.classList.contains('col-impl');
  });
  var countCol = headCells.length - 1;

  // ---------------------------------------------------------------- filtering

  function wanted(name) {
    var out = {};
    Array.prototype.forEach.call(
      form.querySelectorAll('input[name="' + name + '"]:checked'),
      function (box) { out[box.value] = true; }
    );
    return out;
  }

  function shownColumns() {
    var roles = wanted('role');
    var shown = [];
    implCols.forEach(function (th, i) {
      var isClient = th.dataset.client === '1';
      var isServer = th.dataset.server === '1';
      if ((roles.client && isClient) || (roles.server && isServer)) {
        shown.push(FIRST_IMPL_COL + i);
      }
    });
    return shown;
  }

  // Cell classes that mean supported; "default-off" is supported but disabled.
  var SUPPORTED = { 'yes': true, 'default-off': true };

  // Number of shown implementations each row says Yes or Off to. Also the
  // value the count column is rewritten to, so it tracks the column filter.
  function supportCount(row, shown) {
    var n = 0;
    for (var i = 0; i < shown.length; i++) {
      var cell = row.cells[shown[i]];
      if (SUPPORTED[cell.classList[0]]) n++;
    }
    return n;
  }

  function shownRows(shown) {
    var q = form.elements.q.value.trim().toLowerCase();
    var hideEmpty = form.elements['hide-empty'].checked;

    return rows.filter(function (row) {
      if (q && row.cells[0].textContent.toLowerCase().indexOf(q) === -1) return false;
      if (hideEmpty && supportCount(row, shown) === 0) return false;
      return true;
    });
  }

  // ------------------------------------------------------------------ applying

  var appliedCols = null;   // the last column set written to the DOM

  // Hiding a column touches one cell per row, and the count column has to be
  // rewritten with it. Both are skipped while only the row filters change,
  // which is what typing in the search box does.
  function applyColumns(shown) {
    var key = shown.join(',');
    if (key === appliedCols) return;
    appliedCols = key;

    var visible = new Set(shown);
    implCols.forEach(function (th, i) {
      var col = FIRST_IMPL_COL + i;
      var hide = !visible.has(col);
      th.classList.toggle(HIDDEN_COL_CLASS, hide);
      rows.forEach(function (row) {
        row.cells[col].classList.toggle(HIDDEN_COL_CLASS, hide);
      });
    });

    rows.forEach(function (row) {
      row.cells[countCol].textContent = supportCount(row, shown);
    });
  }

  function apply() {
    var shown = shownColumns();
    applyColumns(shown);

    var keep = sorter.sorted(shownRows(shown));
    var kept = new Set(keep);
    var drop = rows.filter(function (r) { return !kept.has(r); });

    var into = document.createDocumentFragment();
    keep.forEach(function (row) { into.appendChild(row); });
    body.appendChild(into);

    var out = document.createDocumentFragment();
    drop.forEach(function (row) { out.appendChild(row); });
    spill.appendChild(out);

    counts.textContent = keep.length + ' of ' + rows.length + ' algorithms, ' +
      shown.length + ' of ' + implCols.length + ' implementations';
  }

  // --------------------------------------------------------------------- wire

  form.addEventListener('input', apply);
  form.addEventListener('reset', function () {
    // The reset has not reached the controls yet when this fires.
    setTimeout(function () { sorter.reset(); apply(); }, 0);
  });

  var sorter = TableSort(table, apply);

  form.hidden = false;
  apply();
})();
