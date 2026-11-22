// Click-to-sort for any table whose header cells carry data-sort="text",
// "number" or "support". aria-sort marks the active column; the CSS draws the
// direction arrows from it.
//
//   var sorter = TableSort(table, onChange);
//
// Without onChange, a header click reorders the first tbody. With it, the
// caller does the reordering, using sorter.sorted(rows), so that sorting can
// be combined with filtering.

window.TableSort = function (table, onChange) {
  'use strict';

  var ID_COL = 0;
  var headCells = Array.prototype.slice.call(table.tHead.rows[0].cells);
  var body = table.tBodies[0];
  var sort = defaultSort();

  function defaultSort() {
    return { col: ID_COL, kind: headCells[ID_COL].dataset.sort, dir: 1 };
  }

  // Rank of a support cell by its first class; anything else is "?".
  var SUPPORT_RANK = { 'yes': 3, 'default-off': 2, 'no': 1 };

  function sortKey(row, col, kind) {
    if (kind === 'number') return Number(row.cells[col].textContent);
    if (kind === 'support') {
      return SUPPORT_RANK[row.cells[col].classList[0]] || 0;
    }
    return row.cells[col].textContent.trim();
  }

  // Numeric runs compare as numbers, so version 10.0 sorts after 9.9.
  var collator = new Intl.Collator('en', { numeric: true, sensitivity: 'base' });

  function compare(a, b) {
    return sort.kind === 'text' ? collator.compare(a, b) : a - b;
  }

  function sorted(list) {
    var decorated = list.map(function (row, i) {
      return { row: row, key: sortKey(row, sort.col, sort.kind), i: i };
    });
    decorated.sort(function (a, b) {
      // Empty cells mean "not known" and go last in either direction.
      if ((a.key === '') !== (b.key === '')) return a.key === '' ? 1 : -1;
      return compare(a.key, b.key) * sort.dir || a.i - b.i;   // stable within ties
    });
    return decorated.map(function (d) { return d.row; });
  }

  function reorder() {
    var into = document.createDocumentFragment();
    sorted(Array.prototype.slice.call(body.rows)).forEach(function (row) {
      into.appendChild(row);
    });
    body.appendChild(into);
  }

  var changed = onChange || reorder;

  function markSort() {
    headCells.forEach(function (th) { th.removeAttribute('aria-sort'); });
    headCells[sort.col].setAttribute('aria-sort', sort.dir === 1 ? 'ascending' : 'descending');
  }

  function setSort(col) {
    var kind = headCells[col].dataset.sort;
    // Yes/No and counts are most useful largest-first, names A-Z.
    var firstDir = (kind === 'text') ? 1 : -1;
    if (sort.col === col) sort.dir = -sort.dir;
    else sort = { col: col, kind: kind, dir: firstDir };

    markSort();
    changed();
  }

  headCells.forEach(function (th, col) {
    if (!th.dataset.sort) return;
    th.classList.add('sortable');
    th.tabIndex = 0;
    th.addEventListener('click', function () { setSort(col); });
    th.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); setSort(col); }
    });
  });

  markSort();
  if (!onChange) reorder();

  return {
    sorted: sorted,
    reset: function () { sort = defaultSort(); markSort(); }
  };
};
