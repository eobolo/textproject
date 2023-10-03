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
