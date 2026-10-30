const fs=require('node:fs'),assert=require('node:assert/strict');
const html=fs.readFileSync('kommun/index.html','utf8');
const links=[...html.matchAll(/href="(https:\/\/www.artportalen.se\/List\/[^\"]+)"/g)].map(x=>new URL(x[1]));
assert.equal(links.length,4);for(const u of links){const p=decodeURIComponent(u.pathname);assert(p.includes('/Kommun/Åstorp'));assert(p.includes('Fåglar'));assert(p.includes('/2026/')||p.includes('/Total/'));}
assert(links.some(u=>u.pathname.includes('/Top/User/')&&u.pathname.includes('/Total/')));
assert(links.some(u=>u.pathname.includes('/Top/User/')&&u.pathname.includes('/2026/')));
assert(links.some(u=>u.pathname.includes('/Top/Species/')));assert(links.some(u=>u.pathname.includes('/CompareSpecies/')));
assert(!/<script|<table|reporter-period|refresh-data|TopUserPager|reportedBy/.test(html));
assert(html.includes('Observatör och rapportör är olika roller'));assert(html.includes('AviList v2026'));
for(const file of ['index.html','forstafynd/index.html'])assert(fs.readFileSync(file,'utf8').includes('Listor hos Artportalen'));
console.log('PASS external links: exact municipality/birds/periods, observer semantics, script-free page, no internal endpoint or ranking.');
