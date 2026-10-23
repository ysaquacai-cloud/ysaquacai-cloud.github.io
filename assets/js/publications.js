const tools = document.querySelector('.publication-tools');
if (tools) {
  tools.hidden = false;
  const search = document.querySelector('#paper-search');
  const status = document.querySelector('#paper-status');
  const papers = [...document.querySelectorAll('[data-publication]')];
  function filter() {
    const query = search.value.trim().toLocaleLowerCase();
    let count = 0;
    papers.forEach(paper => {
      const show = paper.dataset.search.toLocaleLowerCase().includes(query) && (status.value === 'all' || status.value === paper.dataset.status);
      paper.hidden = !show; if (show) count++;
    });
    document.querySelectorAll('[data-year], [data-group]').forEach(group => { group.hidden = ![...group.querySelectorAll('[data-publication]')].some(p => !p.hidden); });
    document.querySelectorAll('.year-nav a').forEach(link => { const year = document.getElementById(link.hash.slice(1)); link.hidden = year ? year.hidden : false; });
    document.querySelector('#result-count').textContent = `${count} ${count === 1 ? 'publication' : 'publications'}`;
    document.querySelector('#no-results').hidden = count !== 0;
  }
  search.addEventListener('input', filter); status.addEventListener('change', filter); filter();
}
