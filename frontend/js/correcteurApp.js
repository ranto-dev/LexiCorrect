const { useState } = React;

function CorrecteurApp() {
  const [texte, setTexte] = useState("");
  const [loading, setLoading] = useState(false);
  const [resultats, setResultats] = useState(null);
  const [erreur, setErreur] = useState(null);

  async function handleCorrection() {
    if (!texte.trim()) return alert("Veuillez entrer un texte");

    setLoading(true);
    setErreur(null);

    try {
      const data = await corrigerTexte(texte);
      setResultats(data);
    } catch {
      setErreur("Erreur de connexion au serveur");
    } finally {
      setLoading(false);
    }
  }

  return React.createElement(
    "div",
    { className: "container" },

    React.createElement(ThreeBackground),
    React.createElement(Header),

    React.createElement(
      "div",
      { className: "glass-card" },
      React.createElement(TextArea, {
        value: texte,
        onChange: (e) => setTexte(e.target.value),
      }),
    ),

    React.createElement(
      "div",
      { className: "buttons" },
      React.createElement(Button, {
        label: loading ? "⏳ Analyse..." : "🎯 Corriger",
        onClick: handleCorrection,
        disabled: loading,
        className: "btn-primary",
      }),
      React.createElement(Button, {
        label: "🗑️ Effacer",
        onClick: () => setTexte(""),
        disabled: loading,
        className: "btn-secondary",
      }),
    ),

    erreur &&
      React.createElement(
        "p",
        { style: { color: "red", textAlign: "center" } },
        erreur,
      ),

    resultats &&
      React.createElement(
        "pre",
        { style: { color: "white" } },
        JSON.stringify(resultats, null, 2),
      ),
  );
}
