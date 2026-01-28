const API_URL = `http://${window.location.hostname}:8000/correct`;

async function corrigerTexte(texte) {
  const response = await axios.post(API_URL, { texte });
  return response.data;
}
