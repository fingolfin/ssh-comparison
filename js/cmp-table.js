// Sorting and filtering for the comparison tables (issue #6).
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

  // Liquid emits the rows sorted by id, so that is the starting state.
  var ID_COL = 0;
  var sort = defaultSort();

  function defaultSort() {
    return { col: ID_COL, kind: 'text', dir: 1 };
  }

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

  // Number of shown implementations each row says Yes to. Also the value the
  // count column is rewritten to, so it tracks the column filter.
  function supportCount(row, shown) {
    var n = 0;
    for (var i = 0; i < shown.length; i++) {
      if (row.cells[shown[i]].className === 'yes') n++;
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

  // ------------------------------------------------------------------ sorting

  function sortKey(row, col, kind) {
    if (kind === 'number') return Number(row.cells[col].textContent);
    if (kind === 'support') {
      var cls = row.cells[col].className;
      return cls === 'yes' ? 2 : cls === 'no' ? 1 : 0;
    }
    return row.cells[col].textContent.trim().toLowerCase();
  }

  function sorted(list) {
    var decorated = list.map(function (row, i) {
      return { row: row, key: sortKey(row, sort.col, sort.kind), i: i };
    });
    decorated.sort(function (a, b) {
      if (a.key < b.key) return -sort.dir;
      if (a.key > b.key) return sort.dir;
      return a.i - b.i;                 // stable: keep id order within ties
    });
    return decorated.map(function (d) { return d.row; });
  }

  function setSort(col) {
    var kind = headCells[col].dataset.sort;
    // Yes/No and counts are most useful largest-first, names A-Z.
    var firstDir = (kind === 'text') ? 1 : -1;
    if (sort && sort.col === col) sort.dir = -sort.dir;
    else sort = { col: col, kind: kind, dir: firstDir };

    markSort();
    apply();
  }

  // aria-sort is also what the CSS draws the direction arrows from.
  function markSort() {
    headCells.forEach(function (th) { th.removeAttribute('aria-sort'); });
    headCells[sort.col].setAttribute('aria-sort', sort.dir === 1 ? 'ascending' : 'descending');
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

    var keep = sorted(shownRows(shown));
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
    setTimeout(function () { sort = defaultSort(); markSort(); apply(); }, 0);
  });

  headCells.forEach(function (th, col) {
    if (!th.dataset.sort) return;
    th.classList.add('sortable');
    th.tabIndex = 0;
    th.addEventListener('click', function () { setSort(col); });
    th.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); setSort(col); }
    });
  });

  form.hidden = false;
  markSort();
  apply();
})();
