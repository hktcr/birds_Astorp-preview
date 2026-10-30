# Funktionell kontroll · 29 oktober 2026

Gäller endast den separata kommunförhandsvisningen, inte astorpsfaglar.se.
Basrevision: 502e9cdeb875e67494d5ad21324ebd1bbe8633f3.

| Område | Faktisk kontroll | Status / begränsning |
|---|---|---|
| Kommunurval | Exakt Åstorp, Artportalen, fåglar, positiva/naturliga/säkra offentliga fynd; geografiska och flaggfel i tester | Godkänt för detta offentliga urval, inte skyddade fynd |
| Full hämtning | Antal före/efter, disjunkta tidsdelar vid 5000-tak, dubbletter, drift, budgetstopp | Regression rättad: barnsumma under förälderns observerade minimiantal förkastas |
| Taxonomi | AviList v2026, verifierade Artfakta-parentkopplingar, grå-/svartkråka, tamduva, okänd mappning | Okänd artmappning stoppar nya totaler; inga tysta bortfall |
| Årsprogress | Faktisk SLU-hämtning 29 oktober;155 mot146 samma datum;1januari16 mot6 | 2026 jämförs med2025, inte föregående helår |
| Datum | Gränsdatum, ogiltigt datum, skottdag, Stockholm sommar-/vintertid | Default följer ny datadag; uttryckligt användarval bevaras även under pågående uppdatering |
| Förstafynd | Sökning, nollträff, återhämtning,2025/2026, källänkar, tangentbordsaktivering | Samma dags flera fynd bevaras; ingen ensam först utses utan tid |
| Kreditering | Faktisk offentlig källa för ett av användaren angivet fynd; separata roller; fel/återförsök; textinjektionstest | Källans namntext, inte verifierade unika personer; inga namn i cache/repo |
| Historik | Verklig hämtning tidigare i samma release:18901 offentliga fynd före2026,200 arter, nollträff före1900 | Inte bevis för kommunens första verkliga fynd någonsin; skyddade/orapporterade fynd okända |
| Cache | Färsk, för gammal, framtida, ogiltig; statisk fil otillgänglig | Verifierad cache kan användas utan beroende av fallbackfilen |
| Fel/timeout | HTTP-fel, ändrade antal, initial15s-timeout, live120s-abort, kontroller återaktiveras, nästa försök lyckas | Fel simulerade i deterministiska tester; inte injicerade i offentlig tjänst |
| Tangentbord | Navigationslänk med Enter, Tab till datum, namnknapp med Enter, synlig fokusmarkering | Faktiskt desktopprov; inte full skärmläsarrevision |
| Responsiv layout | Vanlig Chromium vid100/175/300% zoom, ned till393 CSS-pixlar; ingen sidövergripande horisontell överströmning | Tabell har egen horisontell rullning; verklig telefon/touch ej verifierad |
| Mobil-emulering | DevTools försöktes men nekades av organisationens browserpolicy | Ej kringgånget; ingen påstådd emulerad mobilkontroll |
| Rapportörsstatistik | Periodval och tydliga blockeringsbesked | Ranking saknas avsiktligt: stabil personidentitet och tillämplig källtäckning är inte verifierade |
| Framtida år | Årsversionsgrind | Denna prototyp är explicit2026;2027 kräver ny versionskontroll |

Kör alla fem tester med `for f in scripts/test-municipal*.cjs; do node "$f" || exit; done`.
Feltester ersätter inte faktisk källkontroll. Godkänd teknisk funktion betyder inte
fullständig biologisk inventering eller verifierad personidentitet.

## 30 oktober: förenklad Artportalen-ingång

Ny gren från remote 753ec064, inte från den lokala P71-namnrankingen. Fyra direkta offentliga länkar ersätter den blockerade rapportörsvyn. Kommunårsdata/förstafynd behålls. Länksidan är scriptfri; ingen namninsamling, internendpoint eller proxy.

Samtliga fem befintliga municipaltestskript samt test-artportalen-links.cjs passerar. Den nya kontrollen verifierar exakta kommun-/taxongrupp-/periodlänkar, skillnad observatör/rapportör och att länksidan inte laddar skript eller rankingtabell. Oberoende granskare har kontrollerat diff och alla fyra länkar med HTTP200 och rätt rubriker. Utloggad webbläsarkontroll gjordes samma morgon för källans listor. Det är inte en visuell kontroll av den nya lokala layouten.

Visuell desktop-/mobilkontroll av den nya layouten återstår före slutligt verifierad leverans; den lokala browserstarten var tidigare blockerad av miljön. Produktion och personlig fågelårssida är oförändrade.
