const { useState } = React;

/* =========================
   TEXTE CORRIGÉ
========================= */
function CorrectedText({ text }) {
  return React.createElement(
    "div",
    { className: "glass-card" },
    React.createElement("h3", null, "✅ Corrected Text"),
    React.createElement("p", { className: "corrected-text" }, text),
  );
}

/* =========================
   CARTE ERREUR
========================= */
function ErrorCard({ error }) {
  return React.createElement(
    "div",
    { className: "error-card" },

    React.createElement(
      "div",
      { className: "error-header" },
      React.createElement("strong", null, `'${error.error}'`),
      React.createElement(
        "span",
        { className: "error-category" },
        error.category,
      ),
    ),

    React.createElement("p", { className: "error-message" }, error.message),

    error.suggestions &&
      error.suggestions.length > 0 &&
      React.createElement(
        "div",
        { className: "suggestions" },
        React.createElement("span", null, "Suggestions: "),
        error.suggestions.map((s, i) =>
          React.createElement(
            "span",
            { key: i, className: "suggestion-badge" },
            s,
          ),
        ),
      ),
  );
}

/* =========================
   STATISTIQUES
========================= */
function Statistics({ stats }) {
  return React.createElement(
    "div",
    { className: "glass-card stats-grid" },

    React.createElement(
      "div",
      { className: "stat-card" },
      React.createElement("div", { className: "stat-value" }, stats.word_count),
      React.createElement("div", { className: "stat-label" }, "Words"),
    ),

    React.createElement(
      "div",
      { className: "stat-card" },
      React.createElement(
        "div",
        { className: "stat-value" },
        stats.error_count,
      ),
      React.createElement("div", { className: "stat-label" }, "Errors"),
    ),
  );
}

/* =========================
   APP PRINCIPALE
========================= */
function CorrecteurApp() {
  const [texte, setTexte] = useState("");
  const [loading, setLoading] = useState(false);
  const [resultats, setResultats] = useState(null);
  const [erreur, setErreur] = useState(null);

  async function handleCorrection() {
    if (!texte.trim()) {
      alert("Please enter some text");
      return;
    }

    setLoading(true);
    setErreur(null);
    setResultats(null);

    try {
      const data = await corrigerTexte(texte);
      setResultats(data);
    } catch (err) {
      console.error(err);
      setErreur("Unable to connect to the server.");
    } finally {
      setLoading(false);
    }
  }

  function handleClear() {
    setTexte("");
    setResultats(null);
    setErreur(null);
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
        placeholder: "Enter your text here for AI-powered correction...",
        onChange: (e) => setTexte(e.target.value),
      }),
    ),

    React.createElement(
      "div",
      { className: "buttons" },
      React.createElement(Button, {
        label: loading ? "⏳ Analyzing..." : "🎯 Correct",
        onClick: handleCorrection,
        disabled: loading,
        className: "btn-primary",
      }),
      React.createElement(Button, {
        label: "🗑️ Clear",
        onClick: handleClear,
        disabled: loading,
        className: "btn-secondary",
      }),
    ),

    erreur &&
      React.createElement(
        "p",
        { style: { color: "#ff6b6b", textAlign: "center" } },
        erreur,
      ),

    resultats &&
      React.createElement(
        "div",
        { className: "results" },

        React.createElement(CorrectedText, {
          text: resultats.corrected_text,
        }),

        resultats.errors && resultats.errors.length > 0
          ? React.createElement(
              "div",
              { className: "glass-card" },
              React.createElement("h3", null, "🔍 Errors detected"),
              resultats.errors.map((err) =>
                React.createElement(ErrorCard, {
                  key: err.id,
                  error: err,
                }),
              ),
            )
          : React.createElement(
              "div",
              { className: "glass-card success" },
              React.createElement("h2", null, "🎉 Perfect!"),
              React.createElement(
                "p",
                null,
                "No errors detected in your text.",
              ),
            ),

        React.createElement(Statistics, {
          stats: resultats.statistics,
        }),
      ),
  );
}