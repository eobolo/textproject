#!/usr/bin/node
/*
 we wre going to first create a top level function
 that would use a built in object called Request to
 create a request object from the url we want our json
 data from, then to obtain the json data which is a string
 containing valid javascript object we would use an API
 called fetch which is a function that helps request from
 the json data using te request object formed from the data
 being retrieved url and we await the response from the fetch
 after we get our response we also get the json data using .json
 from the response and also await that.
*/
async function populate() {
  const requestURL = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json";
  const request = new Request(requestURL);
  const response = await fetch(request);
  const superHeroes = await response.json();
  console.log(response);
  console.log(superHeroes);

  populateHeader(superHeroes);
  populateHeroes(superHeroes);
}
/*
 Note: The fetch() API is asynchronous.
 We'll learn a lot about asynchronous functions
 in the next module, but for now, we'll just say
 that we need to add the keyword async before the
 name of the function that uses the fetch API,
 and add the keyword await before the calls to
 any asynchronous functions.
*/
function populateHeader (obj) {
  const header = document.querySelector("Header");
  const myH1 = document.createElement("h1");
  myH1.textContent = obj.squadName;
  header.appendChild(myH1);
  
  const myPara = document.createElement("p");
  myPara.textContent = `Hometown: ${obj.homeTown} // Formed: ${obj.formed}`;
  header.appendChild(myPara);
}
function populateHeroes (obj) {
  const section = document.querySelector("section");
  const heroes = obj.members;

  for (const hero of heroes) {
    const myArticle = document.createElement("article");
    const myH2 = document.createElement("h2");
    const myPara1 = document.createElement("p");
    const myPara2 = document.createElement("p");
    const myPara3 = document.createElement("p");
    const myList = document.createElement("ul");

    myH2.textContent = hero.name;
    myPara1.textContent = `Secret identity: ${hero.secretIdentity}`;
    myPara2.textContent = `Age: ${hero.age}`;
    myPara3.textContent = "Superpowers:";
    
    const superPowers = hero.powers;
    for (const power of superPowers) {
      const listItem = document.createElement("li")
      listItem.textContent = power;
      myList.appendChild(listItem);
    }
    
    myArticle.appendChild(myH2);
    myArticle.appendChild(myPara1);
    myArticle.appendChild(myPara2);
    myArticle.appendChild(myPara3);
    myArticle.appendChild(myList);

    section.appendChild(myArticle);
  }
}

populate();
