"""Build only a public first-day aggregate from verified, local WFS evidence.
Usage: python scripts/prepare-municipal-snapshot.py /path/to/municipal-data-evidence
Raw source records never enter this repository.
"""
import json,sys,hashlib
from pathlib import Path
p=Path(sys.argv[1]);root=Path(__file__).resolve().parents[1]
aggregate=json.loads((p/'municipal-species-firsts-with-tamduva-2025-2026.json').read_text())
sources=[json.loads((p/f'wfs-astorp-{y}.json').read_text())['source'] for y in (2025,2026)]
for s in sources:
 assert s['completeForQuery'] and s['municipality']=='Åstorp' and s['organismGroup']=='Fåglar'
 assert s['countBefore']==s['countAfter']==s['recordCount']==s['queries']['full']['numberReturned']<5000
records=[]
for r in aggregate['records']:
 for id in r['occurrenceIds']:
  records.append({k:r[k] for k in ('taxonId','name','scientificName','rank')}|{'id':id,'day':r['firstDay']})
scope='Artnivå enligt AviList v2026 (20 oktober 2026). Underarter räknas till art; gråkråka och svartkråka är en art. Tamduva ingår i klippduva, inte som extra art. Ospecificerade taxa, skyddade och ännu inte registrerade fynd ingår inte.'
source={'complete':True,'municipality':'Åstorp','fromDay':'2025-01-01','toDay':'2026-10-29','retrievedAt':max(s['retrievedAt']for s in sources),'scopeNote':scope,'taxonomyPolicy':aggregate['taxonomyPolicy'],'endpoint':'https://sosgeo.artdata.slu.se/geoserver/SOS/ows','partitions':[{'fromDay':s['fromDay'],'toDay':s['toDay'],'countBefore':s['countBefore'],'countAfter':s['countAfter'],'fetchedCount':s['recordCount'],'query':s['queries']['full']['parameters']['CQL_FILTER'],'sourceRecordsSha256':s['recordsSha256']} for s in sources],'aggregation':'Earliest day per species and year; all public source references on that day; no coordinates or person fields.','atomicSnapshot':False}
source['taxonomyEvidence']=aggregate['taxonomyEvidence']
source['populationExceptionEvidence']={k:aggregate['populationExceptionEvidence'][k] for k in ('verifiedAt','childTaxonId','parentTaxonId','parentScientificName','source','observedParentHref','limitation')}
source['populationExceptionEvidence']['treatment']='Included as Columba livia under the existing feral-pigeon exception; never an additional species.'
source['taxonomyPolicy']='AviList-v2026-2026-10-20-with-existing-feral-pigeon-inclusion'
source['taxonomyReference']='https://www.avilist.org/checklist/v2026/'
source['sourceIdentifiers']='taxonId is the source Artfakta identifier, not an AviList taxonomic ID.'
for r in records:
 if r['scientificName']=='Troglodytes troglodytes':r['scientificName']='Nannus troglodytes'
 if r['scientificName']=='Emberiza schoeniclus':r['scientificName']='Schoeniclus schoeniclus'
source['exclusions']=aggregate['exclusions']
source['aggregateManifest']=[{'year':y,'records':sum(r['day'].startswith(str(y)) for r in records),'species':len({r['taxonId'] for r in records if r['day'].startswith(str(y))})} for y in (2025,2026)]
(root/'data/municipal-preview.json').write_text(json.dumps({'schemaVersion':1,'source':source,'records':records},ensure_ascii=False,separators=(',',':'))+'\n')
print('Published aggregate records:',len(records),'species/year:',len(aggregate['records']))
