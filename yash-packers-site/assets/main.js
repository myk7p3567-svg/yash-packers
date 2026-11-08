
(function () {
  var btn = document.querySelector('.menu-btn'), nav = document.getElementById('mainnav');
  if (btn && nav) btn.addEventListener('click', function () { var open = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', open); btn.textContent = open ? '✕' : '☰'; });

  function fieldMessage(form) {
    var g = function (id) { var el = form.querySelector('#' + id); return el && el.value ? el.value.trim() : ''; };
    var lines = ['Quotation request from the website', '',
      'Product: ' + g('f-product'), 'Quantity: ' + g('f-qty'), 'Dimensions: ' + g('f-dims'), 'Industry: ' + g('f-industry'),
      'Details: ' + g('f-notes'), '', 'Name: ' + g('f-name'), 'Company: ' + g('f-company'), 'Phone: ' + g('f-phone'), 'Email: ' + g('f-email')];
    return lines.join('\n');
  }
  document.querySelectorAll('form.rfq').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var url = 'https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(fieldMessage(form));
      window.open(url, '_blank', 'noopener');
    });
    var em = form.querySelector('#rfq-email');
    if (em) em.addEventListener('click', function () {
      if (!form.reportValidity()) return;
      location.href = 'mailto:' + form.dataset.email + '?subject=' + encodeURIComponent('Quotation request: ' + (form.querySelector('#f-product').value || 'packaging')) + '&body=' + encodeURIComponent(fieldMessage(form));
    });
  });
})();
