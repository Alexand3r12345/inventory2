Vad har du använt för layouten i ditt GUI? Dvs. har du använt pack eller grid för att placera innehållet. Vilka skillnader har dessa?
jag använde pack för min layout. skilladen mellan pack och grid om jag har förstått det rätt att pack staplar widgets vertikalt eller horisonetl medans
grid fungerar som ett slags rutnät med rader och kolumner och man får mycket mer kontroll över sin layout om man använder grid. 
dock så är pakc enklare för mig och det var därför jag använde mig av pack.

Hur sparar vi innehållet i väskan? Hur fungerar datatypen och varför väljer vi att jobba med den i det här programmet?
det sparas i en lista. och använder append för att lägga till saker i listan. vi anänvder list i programmet eftersom man kan spara flera saker i listan

Hur fungerar kontroller i tkinter? Förklara tillexempel hur du lägger till en knapp och får den att fungera, vad krävs?
för att skapa en knapp använder man som exempel 
visa = tk.Button(root, text="visa innehål i påsen", command=visa_påsen)
visa.pack() 
text=det som står på knappen
command=saken som körs när man klickar knappen
pack=för att placera knappen

Finns det skillnader mellan ditt program som använder tkinter och terminalen? Vilka är det i så fall och varför skiljer det sig?
det är ju vädligt annorlunda grafiskt men rent tekniskt är det också annorlunda.
i terminalen så sker programmet steg för steg och väntar på input i en loop.
medans i tkinter så väntar den på saker som händer, alltså knapptrycken och programmet styrs av en mainloop() som väntar på saker som händer.

Jämför strukturen på programmen? Vad är det som driver programmet i terminal versionen och vad ersätts det med i tkinter?
terminalen drivs av en loop som frågar vad anvädaren ska göra medans tkinter drivs av en mainloop()
funktioner körs när användarern klickar på saker.och programmet körs inte stegvis

Föreslå en eller flera förbättringar på programmet.
Är det kodmässiga förbättringar eller förbättringar för användaren? Fundera kort på hur det skulle gå till att koda detta, kan du förklara?


ett exempel för att göra det bättre för användaren är att göra en knapp som tar bort en sak i påsen. 
gör en funtion som tar texten man skriver och tar bort motsvarande sak sedan koppla funtionen till en knapp med command =ta_bort



