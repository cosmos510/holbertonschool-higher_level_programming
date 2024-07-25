async function getMovies(){
  const rep = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
  const data = await rep.json();

  let myMovieList = document.getElementById("list_movies");

  for (const movie of data.results) {
    let newListItem = document.createElement("li");
    newListItem.textContent = movie.title;
    myMovieList.appendChild(newListItem);
  }
}
getMovies();
