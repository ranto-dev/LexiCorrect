async function corrigerTexte(texte) {
  const response = await fetch("http://localhost:8000/correct", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: texte }),
  });

  if (!response.ok) {
    const err = await response.text();
    throw new Error(err);
  }

  const data = await response.json();
  console.log("Données API :", data);

  return data;
}
